import sys
import re   # 파이썬 정규 표현식 regular expression
import paho.mqtt.client as mqtt
import threading
from parse import *

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import uic
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget
from mqttClient import MqttClient

#from tcpClient import TcpClient

client_pub = mqtt.Client()
# client_sub = mqtt.Client()
# t_pub = None
# t_sub = None


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

        self.client = MqttClient(self)


        self.client.stateChanged.connect(self.on_stateChanged)
        #self.client.messageSignal.connect(self.on_messageSignal)

        self.client.hostname = "broker.mqtt-dashboard.com"
        self.publish_topic = "MP/Polytech/server1"
        #self.client.connectToHost()


        # 클라이언트 설정 후 연결 시도

        direction_list = ['front', 'left', 'right', 'rear', 'stop']
        #self.broker_connect_btn.clicked.connect(self.client.disconnectFromHost)  # 연결버튼 클릭 시 브로커 연결 -> 연결 풀기 어떻게?
        self.broker_connect_btn.clicked[bool].connect(self.connect)
        self.client.connected.connect(lambda: self.broker_connect_btn.setText('종료'))
        self.client.disconnected.connect(lambda: self.broker_connect_btn.setText('연결'))
        # 메세지 전송 시작, 문제점 -> 한 번 누를 때마다 반복됨
        self.broker_start_btn.clicked.connect(lambda: self.client.messageSignal.connect(self.on_messageSignal))
        for i, btn in enumerate((getattr(self, f'{name}_btn') for name in direction_list), 1):
            btn.clicked.connect(lambda x=i: self.client.m_client.publish(self.publish_topic, f"{x}"))

        self.front_btn.clicked.connect(lambda: self.client.m_client.publish(self.publish_topic, "1"))
        self.left_btn.clicked.connect(lambda: self.client.m_client.publish(self.publish_topic, "2"))
        self.right_btn.clicked.connect(lambda: self.client.m_client.publish(self.publish_topic, "3"))
        self.rear_btn.clicked.connect(lambda: self.client.m_client.publish(self.publish_topic, "4"))
        self.stop_btn.clicked.connect(lambda: self.client.m_client.publish(self.publish_topic, "5"))


    def connect(self, state):
        if state:
            self.client.connectToHost()
            self.lineEdit.setText(self.client.hostname)
            self.lineEdit_2.setText(str(self.client.m_port))
            self.lineEdit_3.setText(self.publish_topic)
        else:
            self.client.disconnectFromHost()
            self.lineEdit.setText("")
            self.lineEdit_2.setText("")
            self.lineEdit_3.setText("")

    # MQTT 구독 부분
    @QtCore.pyqtSlot(int)
    def on_stateChanged(self, state):
        if state == MqttClient.Connected:
            print(state)    # 처음 프린트 되는 부분(연결 상태)
            self.client.subscribe("MP/Polytech/car1")

    @QtCore.pyqtSlot(str)
    def on_messageSignal(self, msg):
        try:
            #print(msg)
            self.textEdit.moveCursor(11)  # 커서를 끝으로
            result = parse("{\"distance\":\"{}\"}", msg)
            #print(result[0])
            val = int(result[0])
            self.widget1.update_value(val)
            if len(msg) > 200:
                val = val[1:]
            self.textEdit.append(result[0])  # 메시지 전달
            self.plot1.setData(range(len(msg), val))

            #print(val)  # 정수 출력
        except ValueError:
            print("error: Not is number")


if __name__ == '__main__':
    app = QApplication([])
    WiFi_Dashboard().show()
    sys.exit(app.exec_())

