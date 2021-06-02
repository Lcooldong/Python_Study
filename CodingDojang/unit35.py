# 클래스 속성, 인스턴스 속성
# 클래스 속성 : 모든 인스턴스가 공유. 인스턴스 전체가 사용해야 하는 값을 저장할 때 사용
# 인스턴스 속성 : 인스턴스 별로 독립되어 있음. 각 인스턴스가 값을 저장해야 할 때 사용


# 클래스 속성은 클래스에 속해있으며 모든 인스턴스 공유
class Person:
    bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

one = Person()
one.put_bag('책')

two = Person()
two.put_bag('열쇠')

print(one.bag)  # ['책', '열쇠']
print(two.bag)  # ['책', '열쇠']

# one.bag -> 사실 Person.bag 클래스 속성
# 속성, 메서드 찾을 때 인스턴스, 클래스 순으로 찾음
# 그래서 bag 는 인스턴스 속성이 없으므로 클래스로 찾아짐
print(Person.__dict__)

# 인스턴스 속성 사용하기, 공유 X
class Person1:
    def __init__(self):
        self.bag = []

    def put_bag(self, stuff):
        self.bag.append(stuff)

one = Person1()
two = Person1()

one.put_bag('카메라')
two.put_bag('의자')

print(one.bag)
print(two.bag)


# 비공개 클래스 속성  __속성 = 값

class Knight:
    '''아이템 개수 제한'''
    __item_limit = 10

    def print_item_limit(self):
        '''아이템 개수 제한 출력 메서드'''
        print(Knight.__item_limit)

x = Knight()
x.print_item_limit()
# print(Knight.__item_limit)  클래스 외부에서 접근 할 수 없음
print(Knight.__doc__)   # 클래스.__doc__
print(Knight.print_item_limit.__doc__)  # 클래스.메서드.__doc__
print(x.print_item_limit.__doc__)   # 인스턴스.메서드.__doc__


# 정적 메서드
# 인스턴스를 통한 것이 아닌 클래스에서 바로 호출할 수 있음
# 정적 메서드는 인스턴스 속성(self필요), 인스턴스 메서드 필요 없을 때 사용
# self를 받지 않으면 인스터스 속성 접근 X, 순수함수(pure function) : 같은 입력->같은 출력


class Calc:
    @staticmethod
    def add(a, b):
        print(a + b)

    @staticmethod
    def mul(a, b):
        print(a * b)

Calc.add(10, 15)    # 수를 받아 그냥 출력
Calc.mul(3, 4)      # 인스턴스 속성 필요 없음

# 합집합 계산 시 정적 메서드 사용
a = {1, 2, 3, 4}
a.update({5})   # 인스턴스 메서드
print(a)

set.union({1, 2, 3, 4,}, {5})   # 정적(클래스) 메서드


# 클래스 메서드
class Person2:
    count = 0   # 클래스 속성

    def __init__(self):
        Person2.count += 1  # 인스턴스 생성시 +1


    @classmethod
    def print_count(cls):   # cls 클래스 속성 접근
        print('{0}명 생성되었습니다.'.format(cls.count))
    
    @classmethod    
    def create(cls):
        p = cls()   # 메서드 안에서 현재 클래스의 인스턴스 생성
        return p    # cls()와 Person2()은 같음
    
one = Person2()
two = Person2()
three = Person2()

Person2.print_count()   # 공통이라는 것을 표현하기 위해 클래스명
one.print_count()   # 클래스 메서드는 클래스 공통

four = Person2.create()  # four = Person2() 와 같음
four.print_count()

# exercise

class Date:
    @staticmethod
    def is_date_valid(date_string):
        year, month, day = map(int, date_string.split('-'))
        return month <= 12 and day <= 31

date_string = '2020-06-01'

if Date.is_date_valid(date_string):
    print('올바른 날짜 형식입니다.')
else:
    print('잘못된 날짜 형식입니다.')


# TEST

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second    # 클래스 속성

    @classmethod
    def from_string(cls, time_string):  # 인스턴스 만들기
        hour, minute, second = map(int, time_string.split(':'))
        instance = cls(hour, minute, second)
        return instance

    @staticmethod   # 내부에서 클래스 접근할 필요 없음
    def is_time_valid(time_string):     # 검사 메서드
        hour, minute, second = map(int, time_string.split(':'))
        return hour <= 24 and minute <= 60 and second <= 60  # True, False

# time_string = input()
time_string = '23:35:59'
# time_string = '12:62:43'

if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.second)
else:
    print('잘못된 시간 형식입니다.')



