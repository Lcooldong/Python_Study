import json
data = {'id': '01', 'language': {'java': 'advance'}, 'edition': 'third', 'author': 'Herberts'}

with open('test.json', 'w', encoding='utf-8-sig')as file:
    json.dump(data, file, indent=2)  # indent 들여쓰기
    print('--FileSaved--')
    str_data = json.dumps(data, indent=2)   # dumps -> 문자열로 변환
    print(str_data)

print(type(str_data))
