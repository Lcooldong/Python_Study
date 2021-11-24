import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget
from tcpClient import TcpClient


class ESP12S(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = uic.loadUi("dashboard.ui", self)

        self.widget1 = GaugeWidget(parent=self.widget1)  # parent 에 자기 자신 사이즈 정보 전달

        # 그래프 설정, 플롯 생성
        # self.graph1.setBackground('w')
        # self.graph1.setYRange(0, 300)
        # self.graph1.showGrid(x=True, y=True)
        # self.plot1 = self.graph1.plot(pen='k')


if __name__ == '__main__':
    app = QApplication([])
    ESP12S().show()
    sys.exit(app.exec_())


