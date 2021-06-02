# 클로저
# 변수의 사용 범위와 함수를 클로저 형태로 만드는 법
# 내부함수 -> 루푸나 코드 중복을 피하기 위해, 복잡한 작업을 한번 이상 할 때

# 전역 변수 없을 때
# 함수 내에서 전역변수 수정하고 싶을 때
def foo():
    global x
    x = 20
    print(x)  # 20

foo()
print(x)  # 20


# 변수는 namespace 에 저장
def goo():
    y = 10
    print(locals()) # 지역 네임스페이스 출력

goo()

# 이중 함수
def print_text():
    greeting = 'Thanks, alot!'
    def print_message():  # 함수 정의
        print(greeting) 
    print_message()       # 함수 호출 -> print 문장출력
print_text()

# 지역변수 범위

def A ():
    x = 10
    def B():
        x = 20  # 한단계 더 들어감 함수 밖으로 나오면 안씀

    B()
    print(x)

A()

# 전역변수
x = 1
def A():
    x = 10  # 지역 def A 내에서만, def B는 다른 범위
    def B():
        x = 20  # 지역  def B 내에서만
        def C():
            global x   # 전역
            x = x + 30
            print(x)   # 출력 C-> b -> a 로 이어짐
        C()
    B()
A()

# closure
# 함수를 둘러싼 환경(지역 변수, 코드) 계속 유지하다가
# 함수를 호출할 때 다시 꺼내서 사용하는 함수를 클로저(closure)라고 함
# c 에 저장했다가 c(1) 식으로 꺼내서 사용
# 지역 변수를 바깥에서 접근 못하게 하기 위해
# 매개변수(tag)로 넣으면 기능을 나눠서 사용가능
def calc():
    #---------------------
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b
    #----------------------
    return mul_add  # 함수 자체 반환

c = calc()  # 함수 호출 후 c에 반환값 저장 -> 함수 자체
print(c(1), c(2), c(3), c(4), c(5))
# print(calc(1))    매개 변수가 없어서 사용X
print(calc()(1))  # 리턴 함수에 매개변수 입력 하지만 사용에 번거로움
print('-------------')
# 내부 지역 변수 추적
print(c.__closure__[0].cell_contents)
print(c.__closure__[1].cell_contents)
print('-------------')

# 기능을 살짝 변경하여 사용가능
def outer_func(tag):  #1
    text = 'Some text'  #5
    tag = tag  #6

    def inner_func():  #7
        print('<{0}>{1}<{0}>'.format(tag, text))  #9

    return inner_func  #8

h1_func = outer_func('h1')  #2
p_func = outer_func('p')  #3

h1_func()  #4
p_func()  #10



#  뭔 차이지? 2칸 아래
def calc(x):
    a = 3
    b = 5
    return a * x + b

print(calc(1))



# lambda closure
def calc():
    a = 3
    b = 5
    return lambda x: a*x + b    # 람다 표현식 반환

c = calc()
print(c(1), c(2), c(3), c(4), c(5))

# 클로저의 지역 변수 변경하기
# total 수정하고싶음
def calc():
    a = 3
    b = 5
    total = 0
    def mul_add(x):
        nonlocal total
        total = total + a*x + b
        print(total)
    return mul_add

c = calc()
c(1)    # 8
c(2)    # 19 = 8 + 11
c(3)    # 33 = 19 + 14

print(c.__closure__[0].cell_contents)
print(c.__closure__[1].cell_contents)
print(c.__closure__[2].cell_contents)  # c()작업 후 마지막 total 값

# exercise

def counter():
    i = 0
    def count():
        nonlocal i
        i += 1
        return i
    return count

c = counter()
for i in range(10):
    print(c(), end=' ')

print()
print('-----------Test------------')
# TEST

def countdown(n):
    i = n + 1
    def count():
        nonlocal i
        i -= 1
        return i

    return count

# n = int(input())
n = 10
c = countdown(n)
for i in range(n):
    print(c(), end=' ')
print()
print('-----------Test2------------')

def countdown(n):
    i = n   # i 초기값
    def count():
        nonlocal i  # 전체 함수 내 사용가능
        r = i   # 한번 작동할 때 r 값에 저장해두고
        i -= 1  # 다음 r 을 위해
        return r
    return count    # 카운트 한번 할 때마다 -1씩 감소됨 그값을 r에 저장

# n = int(input())
n = 20
c = countdown(n)
for i in range(n):
    print(c(), end=' ')

print()
print('----------------------')

# 참고 dictionary lambda 로 switch 문 가능
switch = {
    '+': lambda x, y: x + y,  # 람다 표현식으로 실행할 코드를 작성
    '*': lambda x, y: x * y
}

x = '+'
try:
    print(switch[x](10, 20))  # 딕셔너리에 키를 지정하는 방식
except KeyError:
    print('default')  # 딕셔너리에 키가 없을 때는 기본값