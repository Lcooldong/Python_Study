import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic

from analoggaugewidget import AnalogGaugeWidget as GaugeWidet


class JoinQt2(QDialog):
    def __init__(self, _=None):
        QDialog.__init__(self, None)

        self.ui = uic.loadUi("JoinQt2.ui", self)

        self.widget1 = GaugeWidet(parent=self.widget1)
        self.widget1.set_MaxValue(100)

        self.graphView1.setYRange(0, 100)
        self.graphView1.showGrid(x=True, y=True)
        self.plot_data = []  # {'x': [], 'y': []}
        self.data_line = self.graphView1.plot(pen='w')

        self.slider1.valueChanged.connect(self.on_slider1)

    def on_slider1(self, a):
        self.widget1.update_value(a)
        try:
            if 200 < len(self.plot_data):
                self.plot_data = self.plot_data[1:]  # del self.plot_data[0]

            self.plot_data.append(a)
            self.data_line.setData(range(len(self.plot_data)), self.plot_data)
        except EnvironmentError as e:
            print(e)


if __name__ == '__main__':
    app = QApplication([])
    JoinQt2().show()
    sys.exit(app.exec_())
