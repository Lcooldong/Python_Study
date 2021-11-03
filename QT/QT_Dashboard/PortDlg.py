import sys
import serial
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QEvent


class PortDlg(QDialog):
    def __init__(self):
        QDialog.__init__(self, None)

        self.btn1 = QPushButton("OK")
        self.cb1 = QComboBox(self)

        grid = QGridLayout()
        grid.addWidget(self.cb1, 0, 0)
        grid.addWidget(self.btn1, 1, 0)
        self.setLayout(grid)

        # modal dialog 리턴 값-> accept 슬롯에 연결 <-> reject() 슬롯에 연결 cancel 버튼
        self.btn1.clicked.connect(self.accept)
        self.cb1.installEventFilter(self)

    def eventFilter(self, target, event):   # 자식 이벤트 부모가 처리
        if target == self.cb1 and event.type() == QEvent.MouseButtonPress:
            self.cb1.clear()
            self.cb1.insertItems(0, self._available_port())  # 리스트 나열
        return False

    @staticmethod
    def get_port_path():
        import sys
        return {'linux': 'dev/ttyS', 'win32': 'COM'}[sys.platform]  # 대문자 프리픽스

    def _available_port(self):
        available_port = list()
        port_path = self.get_port_path()
        _s = serial.Serial()

        for number in range(32):
            _s.port = port_path + str(number)
            try:
                _s.open()
            except:
                continue
            else:
                if not _s.is_open: continue
                available_port.append(_s.port)
            _s.close()
        del _s
        return available_port


if __name__ == '__main__':
    app = QApplication([])
    w = PortDlg()
    w.show()
    sys.exit(app.exec_())
