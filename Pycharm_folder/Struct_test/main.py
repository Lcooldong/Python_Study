import sys
import ctypes
import time
from ctypes import *
from enum import Enum
import serial
import serial.tools.list_ports
import numpy as np


class Packet(Structure):
    _pack = 1  # 1byte 정렬

    _fields_ = [("led_number", c_uint8),
                ("RGB_buffer", POINTER(c_uint8)),
                ("style", c_uint8),
                ("brightness", c_uint8),
                ("checksum", c_uint8)]


class STYLE(Enum):
    oneColor = 1
    chase = 2
    rainbow = 3


RGB = [255, 123, 45]
RGB_tuple = (22, 33, 11)
# (자료형 * 개수)(* 리스트 또는 튜플)
arr = (ctypes.c_int * len(RGB))(*RGB)

#arr = (ctypes.c_int * len(RGB_tuple))(*RGB_tuple)
#arr = (ctypes.c_int * len(RGB_tuple))(3, 5, 7)

# print(arr[1])
# print(type(arr[1]))
# print(sizeof(arr))
#
# RGB_list = [x for x in arr]
# for i in RGB_list:
#     print(i)
#
# print(RGB_list)

data = Packet(0, cast(arr, POINTER(c_uint8)), STYLE.oneColor.value, 50, 0)


print("------------------packet------------------------")
print(f"led_number : {data.led_number}\n" +
      f"RGB_buffer : {list(map(int, [x for x in arr]))}\n" +
      f"style : {data.style}\n" +
      f"brightness : {data.brightness}\n" +
      f"checksum : {data.checksum}")
print("------------------------------------------------")





def read_serial(num_char = 1):
    string = py_serial.read(num_char)
    return string.decode()


def read_serial_data():
    while True:
        print("insert char data : ", end='')
        command = input()
        py_serial.write(command.encode())

        time.sleep(0.1)

        if py_serial.readable():
            res = py_serial.readline()
            print(res[:len(res)-1].decode('utf-8').rstrip())


def serial_ports():
    ports = serial.tools.list_ports.comports()
    uart_port = ['CP210x', 'CH340', 'CH340K', 'CH9102']
    dic = {}

    for port, desc, hwid in sorted(ports):
        # print("{}: {} [{}]".format(port, desc, hwid))
        for uart in uart_port:
            if uart in desc:
                # print(uart)
                dic[port] = uart
                # print(dic)

    if len(dic.items()) > 0:
        return dic


def connect_port():

    connected_ports = serial_ports()
    board_port = list(connected_ports.keys())

    # print(board_port[0])

    py_serial = serial.Serial(
        port=board_port[0],
        baudrate=115200,
    )


if __name__ == '__main__':
    print(serial_ports())
    connect_port()

    #read_serial_data()
    #string = read_serial(BUFF_SIZE)
    #print(string)

