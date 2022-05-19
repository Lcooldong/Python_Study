import sys
import ctypes
import time
from ctypes import *
from enum import Enum
import serial
import serial.tools.list_ports
import re


class Packet(Structure):

    _pack = 1  # 1byte 정렬

    _fields_ = [("device_led", c_uint8),
                ("RED", c_uint8),
                ("GREEN", c_uint8),
                ("BLUE", c_uint8),
                #("RGB_buffer", POINTER(c_uint8)),
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
          #f"RGB_buffer : {list(map(int, [x for x in arr]))}\n" +
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
    # c_array = (ctypes.c_int * len(packet_rgb))(*packet_rgb)
    # data = Packet(led_num, cast(c_array, POINTER(c_uint8)), style, brightness, 0)
    data = Packet(device_led, rgb_list[0], rgb_list[1], rgb_list[2], brightness, style, wait_time, 0)
    read_packet_data(data)
    return data


def read_serial_data():
    while True:
        if py_serial.readable():
            res = py_serial.readline()
            # res = res[:len(res) - 1].decode('utf-8').rstrip()
            res = res[:len(res) - 1].decode()
            print(res)

            connection_string = "WIFI_CONNECTED"
            esp_now_string = "ESP_NOW_CONNECTED"
            if re.match(res, esp_now_string):
                print("WiFi_connected from ESP32")
                break


        # print("insert char data : ", end='')
        # command = input()
        # py_serial.write(command.encode())
        #
        # time.sleep(0.1)


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


def clear_serial_buffer(ser, delay):
    close_time = time.time() + delay
    while True:
        # if py_serial.readable():
        res = ser.readline()
        print(res[:len(res)-1].decode('utf-8').rstrip())

        if time.time() > close_time:
            break


def serial_receive_callback(ser, data):
    recv_data = ser.read(data)
    recv_data = Packet.from_buffer_copy(recv_data)
    read_packet_data(recv_data)
   # return recv_data


if __name__ == '__main__':
    print(serial_ports())
    py_serial = serial.Serial(port=connect_port('COM7'), baudrate=115200, timeout=0.1)
    # py_serial = serial.Serial(port=connect_port(), baudrate=115200, timeout=0.5)

    read_serial_data()
    clear_serial_buffer(py_serial, 0.5)
    print("===========clear_Buffer===========")
    time.sleep(1)
    # # led_num, rgb_list, brightness, style, wait
    # while True:
    #
    #     x = int(input("0~255 brightness : "))
    #
    #     trans = set_packet(0, 0, [255, 43, 123], x, STYLE.oneColor.value, 50)
    #     send_data = py_serial.write(bytes(trans))

    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.chase.value, 50)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.rainbow.value, 2)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.colorWipe.value, 250)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.chase_rainbow.value, 10)
    # trans = set_packet(0, 0, [255, 43, 123], 10, 0, 10)  # make error style (shut down)

    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.oneColor.value, 50)

    trans = set_packet(0x10, [10, 255, 123], 10, STYLE.oneColor.value, 50)
    send_data = py_serial.write(bytes(trans))

    time.sleep(1)

    trans = set_packet(0x10, [255, 43, 123], 10, STYLE.oneColor.value, 50)
    send_data = py_serial.write(bytes(trans))

    # for i in range(50):
    #     trans = set_packet(0, 0, [255, 0, 0], 100, 1, 20)
    #     send_data = py_serial.write(bytes(trans))
    #
    #     # time.sleep(0.5)
    #
    #     trans = set_packet(0, 0, [0, 255, 0], 5, 1, 20)
    #     send_data = py_serial.write(bytes(trans))
    #
    #     # time.sleep(0.5)
    #
    #     trans = set_packet(0, 0, [0, 0, 255], 200, 1, 20)
    #     send_data = py_serial.write(bytes(trans))


    # change WiFi
    # trans = set_packet(255, 255, [0, 0, 0], 0, 1, 20)
    # send_data = py_serial.write(bytes(trans))

    # serial_receive_callback(py_serial, send_data)

    #
    # for i in range(200, 1, -1):
    #     trans = set_packet(0, 0, [255, 0, 0], i , STYLE.oneColor.value, 20)
    #     send_data = py_serial.write(bytes(trans))
    #     time.sleep(0.1)



    py_serial.close()


    #read_serial_data()
    #string = read_serial(BUFF_SIZE)
    #print(string)


#################참고#####################
# RGB = [255, 123, 45]
# RGB_tuple = (22, 33, 11)
# # (자료형 * 개수)(* 리스트 또는 튜플)
# arr = (ctypes.c_int * len(RGB))(*RGB)
# arr = (ctypes.c_int * len(RGB_tuple))(*RGB_tuple)
# arr = (ctypes.c_int * len(RGB_tuple))(3, 5, 7)
# RGB_list = [x for x in arr]