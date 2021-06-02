# 위치 인수(positional argument), 키워드 인수(keyword argument)

# 위치 인수, 언패킹
print(10, 20, 30)

x = [10, 20, 30]
print(*x)
print(*[10, 20, 30])

# 가변 인수 함수 만들기  args는 튜플
def print_numbers(*args):
    for arg in args:
        print(arg, end=" ")
    print()

print_numbers(10)
print_numbers(10, 20, 30)
print_numbers(*[10, 20, 30, 40])

# 고정 인수와 가변인수 함께 사용(항상 고정, 가변 순서)
def numbers(a, *args):
    print(a)
    print(args)

numbers(1, 5, 10)
numbers(1)
numbers(*[10, 20, 30])

# 키워드 인수
def personal_info1(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

# 키워드 인수 순서 상관 x
personal_info1(name='홍길동', age=28, address='서울시 용산구 이촌동')

# 키워드 인수  sep, end
print(10, 20, 30, sep=":", end="")
print('hi')


# 딕셔너리
x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
personal_info1(**x)

def personal_info2(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')

personal_info2(name='L')
personal_info2(name='L', age='22')

def personal_info3(**kwargs):
    if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
        print('이름 :', kwargs['name'])

    if 'age' in kwargs:
        print('나이 :', kwargs['age'])

    if 'address' in kwargs:
        print('주소 :', kwargs['address'])

personal_info3(**{'name':'jia', 'chara':'dark', 'address':'seoul'})

# 초기값  항상 뒤로 몰아주기
def personal_info4(name, age, address='비공개'):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

personal_info4('galaxy', 25)


# exercise

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수:', max_score)

max_score = get_max_score(english, science)
print('높은 점수:', max_score)


print("-----------------------")

# TEST

korean, english, mathematics, science = 76, 82, 89, 84

def get_min_max_score(*args):
    return min(args), max(args)

def get_average(**kwargs):

    # sum = 0
    # print(kwargs)
    # print(len(kwargs))
    # for arg in kwargs.values():
        # sum += arg

    getsum = sum(kwargs.values())
    return getsum/len(kwargs)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english,
                           mathematics=mathematics, science=science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'
      .format(min_score, max_score, average_score))

