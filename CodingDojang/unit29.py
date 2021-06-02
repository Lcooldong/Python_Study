# 함수
# 선입 후출 스택

def 함수이름(매개변수):
    """
    독스트링
    """

# 함수 설명
print(함수이름.__doc__)

# 함수 내용
help(함수이름)

# 반환값 2개

def add_sub(a, b):
    return a+b, a-b
x, y = add_sub(10, 20)
print(x, y)

# 한개만이면 튜플로 반환
z = add_sub(30, 15)
print(z)
print(*z)

# 튜플 리턴 1, 2
def one_two():
    return 1, 2
print(one_two())


# 리스트 리턴
def One_Two():
    return [1, 2]
print(One_Two())


# exercise

x = 10
y = 3

def get_quotient_remainder(a, b):
    return a//b , a % b

quotient, remainder = get_quotient_remainder(x, y)
print('몫:{0}, 나머지:{1}'.format(quotient, remainder))

# TEST

x, y = map(int, input().split())
def calc(a, b):
    return a+b, a-b, a*b, a/b

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))