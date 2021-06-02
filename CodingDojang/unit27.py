# 파일

# 파일에 문자열 쓰기
# file = open('hi.txt', 'w')
# file.write('hi5')
# file.close()

# 파일 문자열 읽기
file = open('hi.txt', 'r')
s = file.read()
print(s)
file.close()


# 자동으로 파일 객체 닫기
with open('hi.txt', 'r') as file:
    s = file.read()
    print(s)

# 반복문으로 문자열 여러줄 쓰기

# for
# with open('hi2.txt', 'w') as file:
#     for i in range(3):
#         file.write('hihi! {0}\n'.format(i))
#
# # 리스트, .writelines()
# lines = ['hi\n', 'hello\n', 'gombangwa\n']
# with open('hi3.txt', 'w') as file:
#     file.writelines(lines)


# 파일 한줄씩 리스트로 가져오기
with open('hi3.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# 파일 내용 한 줄씩 읽기
# while
with open('hi2.txt', 'r') as file:
    line = None     # line 변수 초기화
    while line != '':   # None은 빈 문자열이 아님
        line = file.readline()  # 읽을게 없을 때 빈문자열("") 반환
        print(line.strip('\n')) # 문자열 읽으면 \n 문자 포함되어있음

# for

with open('hi2.txt', 'r') as file:
    for line in file:
        print(line.strip('\n'))

# pickling (객체를 파일에 저장) , 'wb'  : write binary
# import pickle
#
# name = 'james'
# age = 17
# address = '서울시 서초구 반포동'
# scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
#
# with open('james.p', 'wb') as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#     pickle.dump(address, file)
#     pickle.dump(scores, file)
    
# unpickling(파일에서 객체 불러옴)
import pickle

with open('james.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)



# exercise

lines = [['anonymously\n'],
         ['compatibility\n'],
         ['dashboard\n'],
         ['experience\n'],
         ['photography\n'],
         ['spotlight\n'],
         ['warehouse\n']]

# for i in lines:
#     print(*i)


with open('word.txt', 'w') as file:
    for line in lines:
        file.writelines(*line)

with open('word.txt', 'r') as file:
    count = 0
    words = file.readlines()
    print(words)
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1

    print(count)

# TEST

with open('words.txt', 'r') as file:
    lines = file.read()
    words = lines.split(" ")
    word = list()

    for i in range(len(words)):
        word.append(words[i].strip(',. '))
        if 'c' in word[i]:
            print(word[i])
    # print(word)

    # print(word)
    # words = words.strip(",. ")
    # print(words)
