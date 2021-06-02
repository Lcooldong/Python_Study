import csv

out_file = open('exdata4.csv', 'w', encoding='utf-8-sig', newline='')
data = csv.DictWriter(out_file, fieldnames=["name", "age"])
data.writeheader()
data.writerow({'name':'hong', 'age':10})
data.writerow({'name':'kim' , 'age':18})
out_file.close()


out_file2 = open("exdata5.csv", "w", encoding="utf-8-sig", newline="")
data = csv.DictWriter(out_file2, fieldnames=['name', 'age'])
data.writeheader()
data.writerow({"name": "hong", "age": 10})
data.writerow({"name": "kim", "age": 18})
out_file2.close()


in_file = open("exdata5.csv", "r", encoding="utf-8-sig")
data = csv.DictReader(in_file)
for line in data:                       # 한 row 씩
    print(line['name'],line['age'])     # 이름 나이 순으로

in_file.close()
