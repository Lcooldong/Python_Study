for i in range(1, 51):
    with open("제" + str(i) + "주차.txt", 'w', encoding="utf-8") as file:
        file.write('{}주차 보고서\n')
        file.write('학번 : 00000' + str(i) + '\n')
        file.write('이름: A\n')

import os
os.remove('제25주차.txt')

for i in range(10, 23):
    str_name = '제' + str(i) + '주차.txt'
    os.remove(str_name)