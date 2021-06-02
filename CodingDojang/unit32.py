# 람다식
# 다른 함수의 인수부분에서 간단하게 함수를 만들기 위함

# 람다 표현식, 익명 함수

def plus_one(x):
    return x + 1
print(plus_one(2))

# 람다 표현식(익명함수)을 변수에 할당
plus_one = lambda x: x+1
print(plus_one(2))

# 람다 표현식 자체 호출
print((lambda x: x+1)(2))

# 람다 표현식에는 새로운 변수는 못 만듬
# 외부 변수는 사용가능
y = 1
print((lambda x: x+y)(2))

# 줄이기 3줄 - > 1줄
def plus_two(x):
    return x + 2
print(list(map(plus_two, [1, 2, 3])))

print(list(map(lambda x: x+2, [1, 2, 3])))

# 매개변수 없는 함수, 반환값 필수
print((lambda: 2)())

# 람다 표현식 조건부 표현식,   if 사용시 else 필수
# 3  배수를 문자열 , 나머지는 그대로
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(map(lambda x: str(x) if x % 3 == 0 else x, a))
print(b)

# 너무 길면 그냥 def 로 표현하기, 조건식은 여러개 쓸 수 있음
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))



# map(함수, 반복가능한 객체) 에 여러 객체 넣기
# map: input --(함수(1대1 대응)적용)--> output

a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]
print(list(map(lambda x, y: x*y, a, b)))



# filter(함수, 반복가능한 객체)
# 조건 만족하는 것만 가져오기

def f(x):
    return x > 5 and x < 10
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(f, a)))

a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print(list(filter(lambda x: x>5 and x<10, a)))

# reduce(함수, 반복가능한 객체)
# 먼저 것 2개씩 비교-> 1개로 줄이기(반환값은 함수적용값)
def f(x, y):
    return x + y
a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(f, a))


# 함수 줄이기
a = [1, 2, 3, 4, 5]
from functools import reduce
print(reduce(lambda x, y: x+y, a))


# reduce 복잡할 때는 for 문 사용
a = [1, 2, 3, 4, 5]
x = a[0]    # sum 초기화 과정과 같음, 첫번째 원소로 초기화
for i in range(len(a)-1):   # 초기화에 한개 들어갔으니 한개 빼주고
    x = x + a[i+1]  # x가 첫번째 원소니까, 그 다음부터 넣어주기 위해 i+1
print(x)



# 리스트 표현식
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
print([i for i in a if i > 5 and i<10])


print('------------------')

# quiz
# 끝자리 수가 7인 것만
a = [1, 2, 3, 4, 5, 6, 7, 8, 17]
b = list(filter(lambda x: x % 10 == 7, a))
print(b)

# exercise

files = ['font', '1.png', '10.jpg', '11.gif', '2.jpg', '3.png', 'table.xslx', 'spec.docx']
print(list(filter(lambda x: x.find('.jpg') != -1 or x.find('.png') != -1, files)))

print('--------------------------------')

# TEST
# files = input().split()
# files = ['1.jpg', '10.png', '11.png', '2.jpg', '3.png']
files = ['1.jpg', '97.xlsx', '100.xlsx', '101.docx']    # 101.docx -> 8칸  1.jpg -> 5칸
# print(list(map(lambda x: '{0:0>2s}{1:}'.format(x[0:2], x[2:]), files)))
# 길이로 하면 안되고 확장자를 제거해야함 .뒷부분 제거
a = files[0].split('.')
b = files[1].split('.')
c = files[2].split('.')
print(a)
print('{0:0>3}'.format(a[0]))
print('{0:0>3}'.format(b[0]))
print('{0:0>3}'.format(c[0]))
print(a[1])
print('{0:0>3}'.format(a[0]) + '.' + a[1])
print('{0:0>3}'.format(b[0]) + '.' + b[1])
print('{0:0>3}'.format(c[0]) + '.' + c[1])


print(list(map(lambda x: '{0:0>3s}'.format(x.split('.')[0]) + '.' + x.split('.')[1], files)))
print(list(map(lambda x: '{0:03d}.{1}'.format(int(x.split('.')[0]), x.split('.')[1]), files)))

