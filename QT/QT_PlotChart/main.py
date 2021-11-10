# 고정 저항 r1과 가변 저항 r2의 크기에 따른 전압 신호 크기
# 저항이 큰 쪽이 전압을 많이 분배 받음
# r2 저항이 클 수록 r1의 분배 전압이 작아짐
# 조도 센서의 경우 어두울 때 저항이 커짐 -> 전압 신호 커짐 -> LED 밝아짐
# 비선형 구조라서 일정한 크기로 비례하게 하려면 특정 식이 필요함


import sys

from PyQt5.QtWidgets import *
from PyQt5 import uic


class PlotChart(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.ui = uic.loadUi('resistor_selection.ui', self)

        self.graph1.setBackground('w')
        self.graph1.setYRange(0, 5)
        self.graph1.showGrid(x=True, y=True)
        self.plot1 = self.graph1.plot(pen='k')

        # 값 변화 적용, 내부에 함수명만 넣기
        self.slider1.valueChanged.connect(self.on_slider1)
        # 값 전달, str->int, 받은 값을 넣는 함수를 재정의
        self.edit1.returnPressed.connect(lambda: self.on_slider1(int(self.edit1.text())))


    def on_slider1(self, value):
        try:
            self.slider1.setValue(value)
            self.edit1.setText(str(value))
            r1 = float(value) * {'Ω': 1.0, 'KΩ': 1000.0}\
                .get(self.combo1.currentText(), 1)   # 고정저항 r1,  default : 1

            xl = range(5000, 200000)  # x축 r2 저항 범위
            
            # (x, y) 5.0 입력 전압,  r1/ (r1+r2)-> 분배된 전압, r2(가변저항)에 걸린 전압이 신호 전압
            self.plot1.setData(xl, [5.0 * (r2/(r1+r2)) for r2 in xl])    

        except:
            pass


if __name__ == '__main__':
    app = QApplication([])  # frame
    PlotChart().show()
    sys.exit(app.exec_())   # event loop


