import sys
import threading
import serial

from PyQt5.QtWidgets import *
from PyQt5 import uic   # xml

from PortDlg import PortDlg
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget


class Dashboard(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = uic.loadUi("dashboard2.ui", self)

        self.widget1 = GaugeWidget(parent=self.widget1)
        self.widget1.set_MaxValue(100)

        self.graphicsView1.setBackground('w')
        self.graphicsView1.setYRange(0, 100)
        self.graphicsView1.showGrid(x=True, y=True, alpha=1.0)  # alpha 진함정도

        self.data1 = []
        self.plot = self.graphicsView1.plot(pen='k')  # k 는 검은색

        #self.slider1.valueChanged.connect(self.on_slider1)
        dlg = PortDlg()
        if dlg.exec_() and dlg.cb1.currentText():
            threading.Thread(target=self.connect_serial, args=(dlg.cb1.currentText(),), daemon=True).start()  # args 튜플

    def connect_serial(self, port):
        ser = serial.Serial(port, 115200, timeout=1)     # 클래스 생성
        while True:
            if ser.readable():
                _data = ser.readline()
                # 받은 데이터 -> 아스키 문자열로, 못바꾸는건 무시, 문자열 형변환 불가능 -1 리턴 -> 숫자
                _data = int(str(_data, 'ascii', 'ignore') or -1)
                self.on_slider1(_data)
        ser.close()

    def on_slider1(self, value):    # value 슬라이더 값
        self.widget1.update_value(value)    # widget1에 값 변화 적용
        self.txtbox1.append(str(value))
        self.txtbox1.moveCursor(11)  # 맨위 2, 맨 아래 11
        try:
            if 200 < len(self.data1):   # 최대 범위 200 -> 200보다 커지면
                self.data1 = self.data1[1:]  # 첫번째 값 제거하며 표시

            self.data1.append(value)    # 추가
            self.plot.setData(range(len(self.data1)), self.data1)   # 가로, 세로

        except EnvironmentError as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    Dashboard().show()
    sys.exit(app.exec_())
