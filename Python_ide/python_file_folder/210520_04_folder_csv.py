# utf-8 말고 기본 csv 파일

import csv
in_file=open('exdata2.csv', 'r')
data=csv.reader(in_file)
for line in data:
    print(line)

in_file.close()


out_file=open('exdata3.csv', 'w', encoding='utf-8-sig', newline='')
data = csv.writer(out_file, delimiter=',')
data.writerow(['1', '2', '3'])
data.writerow(['10', '20', '30'])
out_file.close()






