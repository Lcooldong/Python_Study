import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


class QTcalculate(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        self.ui = uic.loadUi('calculateQT.ui', self)

        # ctrl + B  method 세부사항 확인
        for n in (getattr(self, f'pushButton_{i}') for i in range(1, 21)):
            n.clicked.connect(lambda _, x=n.text(): self.on_button(_, x))   # 함수명과 인자 구분 : 시그니쳐

    # 상위에 이미 있는 메소드를 재정의(상속 무시) -> 오버라이딩/ parameter 2개 짜리밖에 없음, 오버로딩이기도 함(parameter 변형, 같은 scope)
    def on_button(self, _, x):
        #print(x)
        if x not in '◀C=':
            self.lineEdit_2.setText(self.lineEdit_2.text() + x)
        elif x == '◀':
            self.lineEdit_2.setText(self.lineEdit_2.text()[:-1])
        elif x == 'C':
            self.lineEdit_2.clear(); self.lineEdit_1.setText('0')
        else:
            try:    # run 계속 하고자 할 때  안그럼 runtime error 발생
                self.lineEdit_1.setText(
                    str(eval(self.lineEdit_2.text()))
                )
            except:
                self.lineEdit_1.setText('0')
            finally:
                self.lineEdit_2.clear()


if __name__ == '__main__':
    app = QApplication([])
    QTcalculate().show()
    sys.exit(app.exec_())   # exec_() 리턴 할 때 종료


