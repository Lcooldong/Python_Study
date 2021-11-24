import sys
import re   # 파이썬 정규 표현식 regular expression

from PyQt5.QtWidgets import *
from PyQt5 import uic
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget
from tcpClient import TcpClient

#accept 받을 때까지 무한루프(thread) breaking 함수
class WiFi_Dashboard(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = uic.loadUi('sonarCar.ui', self)

        self.widget1 = GaugeWidget(parent=self.widget1)   # 자신의 사이즈 입력
        self.widget1.set_MaxValue(300)

        self.graph1.setBackground('w')
        self.graph1.setYRange(0, 300)
        self.graph1.showGrid(x=True, y=True)
        self.plot1 = self.graph1.plot(pen='k')
        self.data1 = []

        self.client = TcpClient()

        self.TCP_connect_btn.clicked.connect(self.connect)
        self.client.recv_signal.connect(lambda v: self.receive(v))
        self.client.conn_signal.connect(lambda: self.TCP_connect_btn.setText('종료'))
        self.client.disc_signal.connect(lambda: self.TCP_connect_btn.setText('연결'))

        # 튜플() 열거(enumerate), i 버튼순서, b 버튼, 1은 i 순서시작, 내부 getattr i(4~8)와 다름
        # for i, b in enumerate((getattr(self, f'button_{i}') for i in range(4, 9)), 1):
        #     b.clicked.connect(lambda _, x=i: self.client.send(f'{x}\r\n'))

        # 틀 만듬, + 1개 이상, * 0개 이상, digit(숫자), space, raw
        self._pattern = re.compile(r'(:\s+\d+[\r\n]\d*|,\s+\d+[\r\n]\d*)', re.DOTALL)

    def connect(self):
        if self.TCP_IP_comboBox.currentText() and self.TCP_port_lineEdit.Text():
            self.client.connect(self.TCP_IP_comboBox.currentText(), self.TCP_port_lineEdit.text())

    def receive(self, data):
        try:
            ascii_data = str(data, 'ascii', 'replace')   # 아스키로 변환하고 아스키가 아니면 대체해라
            self.textEdit.append(ascii_data.translate({ord('\r'): '', ord('\n'): ''}))
            self.textEdit.moveCursor(11)    # 커서를 끝으로
            for pattern_data in self._pattern.findall(data):
                if pattern_data:
                    try:
                        n = int(pattern_data.translate({ord(':'): '', ord(','): '', ord(' '): '',
                                                        ord('\n'): '', ord('\r'): ''}))
                    except EnvironmentError as e:
                        print(e)
                    else:
                        self.widget1.update_value(n)
                        if len(self.data1) > 200:
                            self.data1 = self.data1[1:]
                        self.data1.append(n)
                        self.plot1.setData(range(len(self.data1)), self.data1)
        except EnvironmentError as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    WiFi_Dashboard().show()
    sys.exit(app.exec_())
