import serial
import time
import threading


portName = 'COM14'
baud_rate = 115200

line = []


can_pro = serial.Serial(
        port = portName,
        baudrate=baud_rate,
        parity='N',
        stopbits=1,
        bytesize=8,
        timeout=0
)


class can_pro_thread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name
    def run(self):
        try:
            print("try")
        finally:
            print("finally")

    def can_read(self):



num = 0
def count():
    global num
    num += 1
    print(f"[{num}][{can_pro.is_open}]")
    threading.Timer(1, count).start()

def can_read(event):
    while not event.is_set():
        if can_pro.in_waiting:
            data = can_pro.readline().decode('utf-8').strip()
            print(data)


def can_command(event):
        while True:
            command = input()
            if command == '1':
                if(can_pro.is_open == True):
                    can_pro.close()
                    can_pro.open()
                    print('CAN is Alread Opened')
                else:
                    can_pro.open()
                    print('Open CAN')
                time.sleep(0.5)
                can_pro.write("S6\r".encode('utf-8'))  # Nominal 500k
                can_pro.write("Y2\r".encode('utf-8'))  # CANFD 2M
                can_pro.write("O\r".encode('utf-8'))  # Start CAN
            elif command == '2':
                can_pro.close()
                # can_read_thread.join()

                print('Close CAN')
            elif command == '4':
                if(can_pro.is_open == True):
                    can_read_thread.start()

                print('Start Read CAN')
            elif command == '5':
                event.set()
                can_read_thread.join()
            elif command == '6':
                print('Write CAN')
            elif command == '7':
                for id, thread in list(threading._active.items()):
                    print(f"[ID:{id}]=>[{thread.name}]")





if __name__ == "__main__":
    print("Start UART Program")
    # 시리얼포트 번호 출력
    print(can_pro.name)

    stop_event = threading.Event()

    count_thread =  threading.Thread(target=count, args=())
    can_read_thread = threading.Thread(target=can_read, args=(stop_event,))
    can_command_thread = threading.Thread(target=can_command, args=(stop_event,))

    count_thread.start()
    can_command_thread.start()
