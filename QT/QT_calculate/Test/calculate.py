from PyQt5.QtWidgets import *
from PyQt5 import uic

class calculate(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = uic.loadUi('calculate.ui', self)

if __name__ == '__main__':
    app = QApplication([])
    calculate().show()
    sys.exit(app.exec_())


