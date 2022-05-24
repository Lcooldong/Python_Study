import sys
import time
from ctypes import *
from enum import Enum
import serial
import serial.tools.list_ports


class Packet(Structure):

    _pack = 1  # 1byte 정렬

    _fields_ = [("device_led", c_uint8),
                ("RED", c_uint8),
                ("GREEN", c_uint8),
                ("BLUE", c_uint8),
                ("brightness", c_uint8),
                ("style", c_uint8),
                ("wait_time", c_uint8),
                ("checksum", c_uint8)]


def read_packet_data(fields):
    print("------------------packet------------------------")
    print(f"device_led : {fields.device_led}\n" +
          f"RED   : {fields.RED}\n" +
          f"GREEN : {fields.GREEN}\n" +
          f"BLUE  : {fields.BLUE}\n" +
          f"brightness : {fields.brightness}\n" +
          f"style : {fields.style}\n" +
          f"wait_time : {fields.wait_time}\n" +
          f"checksum : {fields.checksum}")
    print("------------------------------------------------")
    print(f"bytes : {bytes(fields)}")


class STYLE(Enum):
    NONE = 0
    oneColor = 1
    chase = 2
    rainbow = 3
    colorWipe = 4
    chase_rainbow = 5


def set_packet(device_led, rgb_list, brightness, style, wait_time):
    data = Packet(device_led, rgb_list[0], rgb_list[1], rgb_list[2], brightness, style, wait_time, 0)
    read_packet_data(data)
    return data


# 세팅 끝 알려주는 메서드
def readUntilString(ser, exitcode=b'Setup_Done'):
    count = 0
    while True:
        data = ser.read_until()
        print(data)
        # print(count)
        if data == b'':
            count = count + 1
        else:
            count = 0

        if exitcode in data or count > 50:
            return print("====Serial Now available====")


def serial_ports(com_port=None):
    ports = serial.tools.list_ports.comports()
    uart_port = ['CP210x', 'CH340', 'CH340K', 'CH9102']
    dic = {}

    if com_port is not None:
        dic[com_port] = "manually"
        return dic

    for port, desc, hwid in sorted(ports):
        # print("{}: {} [{}]".format(port, desc, hwid))
        for uart in uart_port:
            if uart in desc:
                # print(uart)
                dic[port] = uart
                # print(dic)

    if len(dic.items()) > 0:
        return dic


def connect_port(com_port=None):
    connected_ports = serial_ports(com_port)
    board_port = list(connected_ports.keys())
    # print(board_port[0])
    return board_port[0]


def serial_receive_callback(ser, data):
    recv_data = ser.read(data)
    recv_data = Packet.from_buffer_copy(recv_data)
    read_packet_data(recv_data)
   # return recv_data


if __name__ == '__main__':
    # print(serial_ports())
    # py_serial = serial.Serial(port=connect_port('COM7'), baudrate=115200, timeout=0.1)
    py_serial = serial.Serial(port=connect_port(), baudrate=115200, timeout=0.1)    # 포트 연결

    readUntilString(py_serial)

    time.sleep(1)
    # led_num, rgb_list, brightness, style, wait
    cnt = 0

    trans = set_packet(0x20, [255, 43, 123], 100, STYLE.chase.value, 100)
    send_data = py_serial.write(bytes(trans))


    # change WiFi
    # trans = set_packet(255, 255, [0, 0, 0], 0, 1, 20)
    # send_data = py_serial.write(bytes(trans))

    # serial_receive_callback(py_serial, send_data)

    py_serial.close()