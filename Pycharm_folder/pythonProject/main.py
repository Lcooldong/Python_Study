import ctypes

import serial
import time
from ctypes import *
from enum import Enum


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
#arr = (ctypes.c_int * len(RGB))(*RGB)

arr = (ctypes.c_int * len(RGB_tuple))(*RGB_tuple)
#arr = (ctypes.c_int * len(RGB_tuple))(3, 5, 7)

print(arr[1])
print(type(arr[1]))
print(sizeof(arr))


data = Packet(0, cast(arr, POINTER(c_uint8)), STYLE.oneColor.value, 50, 0)

RGB_list = [2, 4, 6]

print(sizeof(data.RGB_buffer))

print(f"led_number : {data.led_number}\
        RGB_buffer : {list(lambda : data.RGB_buffer[i] for i in range(int(sizeof(data.RGB_buffer)/sizeof(c_int8))))}\
        style : {data.style}\
        brightness : {data.brightness}\
        checksum : {data.checksum}")


py_serial = serial.Serial(
    port='COM5',
    baudrate=115200,
)

BUFF_SIZE = 255

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


if __name__ == '__main__':
    pass
    #read_serial_data()
    #string = read_serial(BUFF_SIZE)
    #print(string)

