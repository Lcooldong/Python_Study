import sys
import re   # 파이썬 정규 표현식 regular expression
import paho.mqtt.client as mqtt
import threading


from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import uic
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget
from mqttClient import MqttClient

#from tcpClient import TcpClient

client_pub = mqtt.Client()
client_sub = mqtt.Client()
t_pub = None
t_sub = None


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
        #self.client.connectToHost()

        # 클라이언트 설정 후 연결 시도
        
        self.broker_connect_btn.clicked.connect(self.client.connectToHost)  # 연결버튼 클릭 시 브로커 연결 -> 연결 풀기 어떻게?
        self.client.connected.connect(lambda: self.broker_connect_btn.setText('종료'))
        self.client.disconnected.connect(lambda: self.broker_connect_btn.setText('연결'))
        # 메세지 전송 시작, 문제점 -> 한 번 누를 때마다 반복됨
        self.broker_start_btn.clicked.connect(lambda: self.client.messageSignal.connect(self.on_messageSignal))  

        # 메시지 한번 보내보기
        #self.mqttc.publish(self.publish_topic, "5")

        # 틀 만듬, + 1개 이상, * 0개 이상, digit(숫자), space, raw
        self._pattern = re.compile(r'(:\s+\d+[\r\n]\d*|,\s+\d+[\r\n]\d*)', re.DOTALL)
    
    # MQTT 구독 부분
    @QtCore.pyqtSlot(int)
    def on_stateChanged(self, state):
        if state == MqttClient.Connected:
            print(state)    # 처음 프린트 되는 부분(연결 상태)
            self.client.subscribe("214hoSmartHome/out")

    @QtCore.pyqtSlot(str)
    def on_messageSignal(self, msg):
        try:
            #val = float(msg)   # 받은 메세지
            #self.lcd_number.display(val)
            val = int(msg)
            self.textEdit.append(msg)   # 메시지 전달
            self.textEdit.moveCursor(11)
            print(val)  # 정수 출력 
            #self.broker_lineEdit.text(val)
        except ValueError:
            print("error: Not is number")





if __name__ == '__main__':
    app = QApplication([])
    WiFi_Dashboard().show()
    sys.exit(app.exec_())

