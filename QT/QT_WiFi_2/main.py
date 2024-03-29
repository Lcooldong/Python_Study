import sys
import re   # 파이썬 정규 표현식 regular expression
import paho.mqtt.client as mqtt
import threading


from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import uic
from analoggaugewidget import AnalogGaugeWidget as GaugeWidget
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
        self.client.messageSignal.connect(self.on_messageSignal)

        self.client.hostname = "broker.mqtt-dashboard.com"
        self.client.connectToHost()


        # 클라이언트 설정 후 연결 시도
        self.broker_connect_btn.clicked.connect(lambda: self.broker_lineEdit.setText(str(MqttClient.state)))

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


class MqttClient(QtCore.QObject):
    Disconnected = 0
    Connecting = 1
    Connected = 2

    MQTT_3_1 = mqtt.MQTTv31
    MQTT_3_1_1 = mqtt.MQTTv311

    connected = QtCore.pyqtSignal()
    disconnected = QtCore.pyqtSignal()

    stateChanged = QtCore.pyqtSignal(int)
    hostnameChanged = QtCore.pyqtSignal(str)
    portChanged = QtCore.pyqtSignal(int)
    keepAliveChanged = QtCore.pyqtSignal(int)
    cleanSessionChanged = QtCore.pyqtSignal(bool)
    protocolVersionChanged = QtCore.pyqtSignal(int)

    messageSignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(MqttClient, self).__init__(parent)

        self.m_hostname = ""
        self.m_port = 1883
        self.m_keepAlive = 60
        self.m_cleanSession = True
        self.m_protocolVersion = MqttClient.MQTT_3_1

        self.m_state = MqttClient.Disconnected

        self.m_client = mqtt.Client(clean_session=self.m_cleanSession,
            protocol=self.protocolVersion)

        self.m_client.on_connect = self.on_connect
        self.m_client.on_message = self.on_message
        self.m_client.on_disconnect = self.on_disconnect


    @QtCore.pyqtProperty(int, notify=stateChanged)
    def state(self):
        return self.m_state

    @state.setter
    def state(self, state):
        if self.m_state == state: return
        self.m_state = state
        self.stateChanged.emit(state)

    @QtCore.pyqtProperty(str, notify=hostnameChanged)
    def hostname(self):
        return self.m_hostname

    @hostname.setter
    def hostname(self, hostname):
        if self.m_hostname == hostname: return
        self.m_hostname = hostname
        self.hostnameChanged.emit(hostname)

    @QtCore.pyqtProperty(int, notify=portChanged)
    def port(self):
        return self.m_port

    @port.setter
    def port(self, port):
        if self.m_port == port: return
        self.m_port = port
        self.portChanged.emit(port)

    @QtCore.pyqtProperty(int, notify=keepAliveChanged)
    def keepAlive(self):
        return self.m_keepAlive

    @keepAlive.setter
    def keepAlive(self, keepAlive):
        if self.m_keepAlive == keepAlive: return
        self.m_keepAlive = keepAlive
        self.keepAliveChanged.emit(keepAlive)

    @QtCore.pyqtProperty(bool, notify=cleanSessionChanged)
    def cleanSession(self):
        return self.m_cleanSession

    @cleanSession.setter
    def cleanSession(self, cleanSession):
        if self.m_cleanSession == cleanSession: return
        self.m_cleanSession = cleanSession
        self.cleanSessionChanged.emit(cleanSession)

    @QtCore.pyqtProperty(int, notify=protocolVersionChanged)
    def protocolVersion(self):
        return self.m_protocolVersion

    @protocolVersion.setter
    def protocolVersion(self, protocolVersion):
        if self.m_protocolVersion == protocolVersion: return
        if protocolVersion in (MqttClient.MQTT_3_1, MQTT_3_1_1):
            self.m_protocolVersion = protocolVersion
            self.protocolVersionChanged.emit(protocolVersion)

    #################################################################
    @QtCore.pyqtSlot()
    def connectToHost(self):
        if self.m_hostname:
            self.m_client.connect(self.m_hostname,
                port=self.port,
                keepalive=self.keepAlive)

            self.state = MqttClient.Connecting
            self.m_client.loop_start()

    @QtCore.pyqtSlot()
    def disconnectFromHost(self):
        self.m_client.disconnect()

    def subscribe(self, path):
        if self.state == MqttClient.Connected:
            self.m_client.subscribe(path)

    #################################################################
    # callbacks
    def on_message(self, mqttc, obj, msg):
        mstr = msg.payload.decode("ascii")
        # print("on_message", mstr, obj, mqttc)
        self.messageSignal.emit(mstr)

    def on_connect(self, *args):
        # print("on_connect", args)
        self.state = MqttClient.Connected
        self.connected.emit()

    def on_disconnect(self, *args):
        # print("on_disconnect", args)
        self.state = MqttClient.Disconnected
        self.disconnected.emit()


if __name__ == '__main__':
    app = QApplication([])
    WiFi_Dashboard().show()
    sys.exit(app.exec_())

