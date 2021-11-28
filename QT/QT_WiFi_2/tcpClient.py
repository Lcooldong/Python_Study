import threading
import socket
from PyQt5.QtCore import pyqtSignal, pyqtSlot, QObject, QByteArray


class TcpClient(QObject):
    recv_signal = pyqtSignal(QByteArray)
    conn_signal = pyqtSignal()
    disc_signal = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)  # __ 시스템 사용
        self._staus = False     
        self._client = None  # 내부에서 사용한다는 약속 _ 한개

    def connect(self, ip, port):
        if self._staus:
            self.stop()
            return False    # 구분용, 사용X

        self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self._client.connect((ip, int(port)))   # 튜플
        except EnvironmentError as e:
            print('connect Error : ', e)
            return False

        self._staus = True  # 접속되었음
        self.conn_signal.emit()  # 연결되었음 알림
        
        threading.Thread(target=self.receive, args=(lambda: self._staus,), daemon=True).start()    # 튜플 ', '붙여야함
        return True

    def receive(self, stop):    # self.stop이랑 다름, stop은 위 람다 함수임
        while stop():   # 연결되었을 때
            try:
                buf = self._client.recv(1024)
            except EnvironmentError as e:
                print('recv Error : ', e)
            else:
                if buf:
                    self.recv_signal.emit(buf)
        self.stop()

    def stop(self):
        if hasattr(self, '_client') and isinstance(self._client, socket.socket): # _client 이름이 있으면 그리고 socket.socket 변수가 있는지
            self._client.close()    # 클라이언트 종료
        self._staus = False         # 연결 상태 해제
        self.disc_signal.emit()     # disconnect 신호 전달
        
    def send(self, msg):
        if not self._staus:     # 연결 안됬으면
            return
        try:
            self._client.send(msg.encode())
        except EnvironmentError as e:
            print('send Error : ', e)

    def __del__(self):  # 메모리에서 사라질 때
        self.stop()

            