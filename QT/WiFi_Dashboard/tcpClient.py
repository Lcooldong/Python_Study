import threading
import socket
from PyQt5.QtCore import pyqtSlot, pyqtSignal, QObject, QByteArray


class TcpClient(QObject):  # signal-> main 통신
    recv_signal = pyqtSignal(QByteArray)
    conn_signal = pyqtSignal()  # on off
    disc_signal = pyqtSignal()  # on off

    def __init__(self, widgets):    # widgets : groupbox(부모)의 child
        QObject.__init__()

        self.ip = widgets[0]
        self.port = widgets[1]

        self.bConn = False
        self.client = None

    def connect(self, ip, port):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # instance
        try:
            self.client.connect((ip, port))
        except EnvironmentError as e:
            print(e)
            return False
        else:   # except 미 발생 시 실행
            self.bConn = True
            threading.Thread(target=self.receive, arge=(lambda: self.bConn,), daemon=True).start()

    def receive(self, stop):    # thread로 데이터 주고 받음
        while stop():   # stop()지역함수  bConn True(연결되어있는 동안) 일 동안 receive 함
            try:
                buf = self.client.recv(1024)    # 버퍼 받음
            except EnvironmentError as e:
                print(e)
                break
            else:
                if buf:  # 받은 데이터가 있을 때
                    self.recv_signal.emit(buf)  # QByteArray로 buf(받은 signal쪽으로) 들어감

        self.stop()  # 인스턴스

    def stop(self):
        self.bConn = False
        if hasattr(self, 'client') and isinstance(self.client, socket.socket):  # 클라이언트가 있고 socket instance가 있을때
            self.client.close()
            self.disc_signal.emit()

    def send(self, msg):
        if not self.bConn:
            return
        try:
            self.client.send(msg.encode())
        except EnvironmentError as e:
            print(e)

    def __del__(self):  # 종료할 때(system) 정리
        self.stop()
