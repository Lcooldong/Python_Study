square = lambda x: x**3  # x의 3제곱수
print(square(5))

def square2(x):
    return x**3
print(square2(5))




def str_len(string):
    return len(string)

str_len('hello')

strings = ['abc', 'abcdefg','abcde', 'abcedf']
# strings.sort(key = str_len) # 함수를 정렬 키로 설정
strings.sort(key=lambda string: len(string)) # 변수: 구현
print(strings)


