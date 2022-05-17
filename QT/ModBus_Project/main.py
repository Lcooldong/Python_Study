from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import uic
# import resources
from PyQt5.QtCore import QTimer, QRect, Qt
from PyQt5.QtGui import QIcon, QPainter, QPen

from PyQt5.QtWidgets import QDialog, QWidget
#from PyQt5.QtWidgets import *
from PySide2.QtCore import QPoint   # framegeometry
from pyModbusTCP.client import ModbusClient
import sys
import time
import threading


class Controller_UI(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        QDialog.resize(self, 800, 600)
        self.ui = uic.loadUi("./UI/Controller.ui", self)
        self.setup_Ui()

        client = ModbusClient(host="192.168.56.101", port=502, auto_open=True, unit_id=1, auto_close=False)



        #dot_point = self.mapToGlobal(self.point_widget.frame)

    def setup_Ui(self):
        self.setWindowTitle("ModBus_Controller")
        self.setGeometry(560, 200, 800, 500)  # 왼쪽 위 (0,0) 처음위치 + 크기 (0, 0)
        self.setWindowIcon(QIcon('./picture/ur_icon.png'))


        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.mouse_event_check())
        self.held_time = 0

        self.timer_button = QTimer()
        self.timer_button.timeout.connect(lambda: self.button_event_check())
        self.button_held_time = 0

        self.X_Inc.pressed.connect(self.X_Inc_Btn_pressed)
        self.X_Inc.released.connect(self.X_Inc_Btn_released)
        self.X_Dec.pressed.connect(self.X_Dec_Btn_pressed)
        self.X_Dec.released.connect(self.X_Dec_Btn_released)

        self.Y_Inc.pressed.connect(self.Y_Inc_Btn_pressed)
        self.Y_Inc.released.connect(self.Y_Inc_Btn_released)
        self.Y_Dec.pressed.connect(self.Y_Dec_Btn_pressed)
        self.Y_Dec.released.connect(self.Y_Dec_Btn_released)

        self.Z_Inc.pressed.connect(self.Z_Inc_Btn_pressed)
        self.Z_Inc.released.connect(self.Z_Inc_Btn_released)
        self.Z_Dec.pressed.connect(self.Z_Dec_Btn_pressed)
        self.Z_Dec.released.connect(self.Z_Dec_Btn_released)

        self.stopBtn.clicked.connect(self.stopBtn_clicked)

        self.position_data = [0 for i in range(3)]
        self.saveBtn.clicked.connect(self.saveBtn_clicked)


       # x = self.groupBox.geometry().width() -1
        x = self.groupBox.point_grid.geometry().x() - 1

        y = self.groupBox.geometry().height() -1


        print("X : ", x, " Y :", y)

    def X_Inc_Btn_pressed(self):
        self.timer_button.start(50)
        print("X+")

    def X_Inc_Btn_released(self):
        self.Btn_released()

    def X_Dec_Btn_pressed(self):
        self.timer_button.start(50)
        print("X-")

    def X_Dec_Btn_released(self):
        self.Btn_released()



    def Y_Inc_Btn_pressed(self):
        self.timer_button.start(50)
        print("Y+")

    def Y_Inc_Btn_released(self):
        self.Btn_released()

    def Y_Dec_Btn_pressed(self):
        self.timer_button.start(50)
        print("Y-")

    def Y_Dec_Btn_released(self):
        self.Btn_released()


    def Z_Inc_Btn_pressed(self):
        self.timer_button.start(50)
        print("Z+")

    def Z_Inc_Btn_released(self):
        self.Btn_released()

    def Z_Dec_Btn_pressed(self):
        self.timer_button.start(50)
        print("Z-")

    def Z_Dec_Btn_released(self):
        self.Btn_released()


    def stopBtn_clicked(self):
        print("stopBtn clicked")

    def Btn_released(self):
        self.timer_button.stop()
        print("Button Held for {:4f} seconds".format(self.button_held_time))
        self.button_held_time = 0

    def button_event_check(self):
        self.button_held_time += 0.075


    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.darkGreen, 8))
        x = self.groupBox.geometry().width() - 1
        y = self.groupBox.geometry().height() - 1
        qp.drawPoint(x, y)

    # 마우스 이벤트
    def mousePressEvent(self, mouse_event):  # 일반 창에서 작동
        self.timer.start(50)
        print("test: {}-{}".format(mouse_event.pos().x(), mouse_event.pos().y()))

    def mouse_event_check(self):
        self.held_time += 0.075

    def mouseReleaseEvent(self, mouse_event):
        self.timer.stop()
        print("Mouse Held for {:4f} seconds".format(self.held_time))
        self.held_time = 0

    def saveBtn_clicked(self):
        self.position_data[0] = round(float(self.X_lineEdit.text()), 2)
        self.position_data[1] = round(float(self.Y_lineEdit.text()), 2)
        self.position_data[2] = round(float(self.Z_lineEdit.text()), 2)
        #print(self.X_lineEdit.text())

        print(self.position_data)
        self.position_data = [0 for i in range(3)]
        print(self.position_data)
        print("saveBtn clicked")




    def read_port(self, addr):
        return self.client.read_holding_registers(addr, 1)

    def __del__(self):
        self.client.close()
        print("App Exiting..")

def read_handler():
    old_value = [1]
    while True:
        new_value = Controller_UI.read_port(130)
        if(new_value != old_value):
            print("Done", new_value)

        old_value = new_value
        time.sleep(0.1)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller_UI()
    controller.show()

    t = threading.Thread(target=read_handler)
    #t.start()

    sys.exit(app.exec_())
