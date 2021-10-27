import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Ex1(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.lbl1 = QLabel('Button 1')
        self.lbl2 = QLabel('Current value 0')
        self.btn1 = QPushButton('Button 1')
        self.btn2 = QPushButton('Button 2')
        self.sld1 = QSlider(Qt.Horizontal)

        hbx = QHBoxLayout()
        hbx.addWidget(self.btn1)
        hbx.addWidget(self.btn2)

        vbx = QVBoxLayout()
        vbx.addWidget(self.lbl1)
        vbx.addLayout(hbx)
        vbx.addWidget(self.lbl2)
        vbx.addWidget(self.sld1)

        self.setLayout(vbx)

        self.btn1.clicked.connect(lambda: self.lbl1.setText('Button 1'))
        self.btn2.clicked.connect(lambda: self.lbl1.setText('Button 2'))
        self.sld1.valueChanged.connect(lambda x: self.lbl2.setText(f'Current value : {x}'))


if __name__ == '__main__':
    app = QApplication([])
    Ex1().show()
    sys.exit(app.exec_())
