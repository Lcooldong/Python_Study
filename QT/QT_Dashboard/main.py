import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic   # xml

from analoggaugewidget import AnalogGaugeWidget as GaugeWidget


class Dashboard(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = uic.loadUi("test.ui", self)

        self.widget1 = GaugeWidget(parent=self.widget1)
        self.widget1.set_MaxValue(100)

        self.graphicsView1.setBackground('w')
        self.graphicsView1.setYRange(0, 100)
        self.graphicsView1.showGrid(x=True, y=True, alpha=1.0)  # alpha 진함정도

        self.data1 = []
        self.plot = self.graphicsView1.plot(pen='k')  # k 는 검은색

        self.slider1.valueChanged.connect(self.on_slider1)

    def on_slider1(self, value):
        self.widget1.update_value(value)


if __name__ == '__main__':
    app = QApplication([])
    Dashboard().show()
    sys.exit(app.exec_())
