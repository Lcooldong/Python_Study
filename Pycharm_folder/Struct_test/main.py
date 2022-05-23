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


# def readUntilExitCode(ser, exitcode=b'\x03'):
# def readUntilExitCode(ser, exitcode=b'\xFF'):
def readUntilExitCode(ser, exitcode=b'\xFF'):
    readed = b''
    while True:
        data = ser.read()   # 1byte , 영문 1개, 숫자 0x00
        print(data)
        readed += data
        if exitcode in data:
            print(readed[:1])
            print(readed)
            return readed[:1]   # 가장 마지막 문자

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



def read_serial_data(ser):
    while True:
        if ser.readable():
            res = ser.readline()
            # res = res[:len(res) - 1].decode('utf-8').rstrip()
            res = res[:len(res) - 1].decode()
            print(res)

            connection_string = "WIFI_CONNECTED"
            esp_now_string = "ESP_NOW_CONNECTED"
            esp_now_broadcast = "Setup_Done"
            if re.match(res, esp_now_broadcast):
                print("WiFi_connected from ESP32")
                return res


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
        # print(res[:len(res)-1].decode('utf-8').rstrip()
        print(res[:len(res) - 1].decode().rstrip())

        if time.time() > close_time:
            break


def serial_receive_callback(ser, data):
    recv_data = ser.read(data)
    recv_data = Packet.from_buffer_copy(recv_data)
    read_packet_data(recv_data)
   # return recv_data


if __name__ == '__main__':
    print(serial_ports())
    # py_serial = serial.Serial(port=connect_port('COM7'), baudrate=115200, timeout=0.1)
    py_serial = serial.Serial(port=connect_port(), baudrate=115200, timeout=0.1)

    # readUntilExitCode(py_serial)
    readUntilString(py_serial)

    # read_serial_data(py_serial)
    # clear_serial_buffer(py_serial, 0.5)

    time.sleep(1)
    # led_num, rgb_list, brightness, style, wait
    cnt = 0

    while True:

        # x = input("0~255 brightness : ")
        #
        # if x == "x":
        #     print("Get out of while")
        #     break
        #
        # trans = set_packet(0x10, [255, 43, 123], int(x), STYLE.oneColor.value, 50)
        # send_data = py_serial.write(bytes(trans))
        #
        # trans = set_packet(0x20, [255, 43, 123], int(x), STYLE.oneColor.value, 50)
        # send_data = py_serial.write(bytes(trans))

        if cnt > 1:
            cnt = 0

        time.sleep(0.5)

        trans = set_packet(0x20, [255, 43, 123], 50*cnt, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))



        time.sleep(0.5)

        trans = set_packet(0x21, [255, 43, 123], 50*cnt, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(0.5)

        trans = set_packet(0x22, [255, 43, 123], 50*cnt, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(0.5)

        trans = set_packet(0x24, [255, 43, 123], 50*cnt, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(0.5)

        trans = set_packet(0x28, [255, 43, 123], 50*cnt, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(0.5)





        cnt = cnt + 1

    for i in range(30):
        trans = set_packet(0x10, [255, 43, 123], 50, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(1)

        trans = set_packet(0x20, [255, 43, 123], 10, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(1)

        trans = set_packet(0x10, [10, 43, 220], 5, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))

        time.sleep(1)

        trans = set_packet(0x20, [34, 255, 123], 70, STYLE.oneColor.value, 50)
        send_data = py_serial.write(bytes(trans))


    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.chase.value, 50)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.rainbow.value, 2)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.colorWipe.value, 250)
    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.chase_rainbow.value, 10)
    # trans = set_packet(0, 0, [255, 43, 123], 10, 0, 10)  # make error style (shut down)

    # trans = set_packet(0, 0, [255, 43, 123], 10, STYLE.oneColor.value, 50)
    # for i in range(10):
    #     trans = set_packet(0x10, [10, 255, 123], 50, STYLE.oneColor.value, 50)
    #     send_data = py_serial.write(bytes(trans))
    #
    #     time.sleep(0.1)
    #
    #     trans = set_packet(0x10, [255, 43, 123], 20, STYLE.oneColor.value, 50)
    #     send_data = py_serial.write(bytes(trans))

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