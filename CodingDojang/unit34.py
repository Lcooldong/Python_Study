# 클래스

class Person:
    def greeting(self):
        print('hi')

# person->Person 의 인스턴스 생성
person = Person()
# 인스턴스 메서드 : 인스턴스를 통해 메서드 호출
person.greeting()


# 메서드 안에서 메서드 호출하기
class Person2:
    def greeting(self):
        print('hello')

    def hello(self):
        self.greeting()  # 클래스 안 메서드 호출 

person2 = Person2()
person2.hello()

# 인스턴스 확인
print(isinstance(person, Person))

# 객체의 자료형을 판단
def factorial(n):
    if not isinstance(n, int) or n < 0:  # n이 정수가 아니거나 음수이면 끝냄
        return None
    if n == 1:
        return 1
    return n * factorial(n-1)

# attribute (속성)
# __init__ 인스턴스 생성 때 호출되는 메서드
# self 클래스 주소

class Person3:
    def __init__(self):
        self.hello = '안녕하세요'

    def greeting(self):
        print(self.hello)

person3 = Person3()
person3.greeting()


# 인스턴스 생성시 attribute 값 받기

class Person4:
    def __init__(self, name, age, address):
        self.hello = '안녕하세여.'
        self.name = name
        self.age = age
        self.address = address

    def greeting(self):
        print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

maria = Person4('marie', 18, 'Australia')
maria.greeting()

print('이름:', maria.name)
print('나이:', maria.age)
print('주소:', maria.address)


# 클래스 위치 인수, 키워드 인수, 가변인수, 리스트 언패킹
class Person5:
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

person_list = ['메리', '25', '서울시']
merry = Person5(*person_list)
print(merry.name)
print(merry.age)
print(merry.address)

# 키워드 인수, 언패킹, 딕셔너리

class Person6:
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']
        
john = Person6(name='존', age=23, address='서울시 구로동')
Tom = Person6(**{'name': 'Tom', 'age': 23, 'address': '서울시 서초구'})

print(john.age + Tom.age)


# 인스턴스 생성 후 attribute 추가, 특정 attribute 만 허용
class Person7:
    pass

# 특정 인스턴스에만 있음
dolly = Person7()
dolly.name = '돌리'
print(dolly.name)

ally = Person7()
ally.name = '알리'
print(ally.name)


# 인스턴스 생성 후 속성 추가-> init 말고 다른 메서드에 속성 추가 가능

class Person8:
    def greeting(self):
        self.hello = 'hello'

kim = Person8()
# kim.hello 초기화(init) 속성에 없음 사용X
kim.greeting()  # 메서드 호출을 해야
print(kim.hello)  # hello 속성 생성됨


# __slots__ : 특정 속성만 허용
class Person9:
    __slots__ = ['name', 'age']
    
jenny = Person9()
jenny.name = '제니'
jenny.age = '19'
# jenny.address = '서울' 슬롯에 없어서 사용 X

print(jenny.name, jenny.age)


# private attribute  self.__attribute =
# 클래스 안 메서드만 접근 가능
class Person10:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

Andy = Person10('엔디', 26, '경북', 10000)  # 초기화에 넣을 수는 있음

# Andy.__wallet -= 5000  외부 접근 X

class Person11:
    def __init__(self, name, age, address, wallet):
        self.name = name
        self.age = age
        self.address = address
        self.__wallet = wallet

    def pay(self, amount):
        self.__wallet -= amount
        print('이제 {0}원 남았네요'.format(self.__wallet))

    def checkPay(self, amount):
        if amount > self.__wallet:
            print('돈이 부족합니다.')
            return
        self.__wallet -= amount


kari = Person11('카리', 15, '지리산', 10000)
kari.pay(600)
kari.checkPay(11000)
kari.checkPay(1200)  # 남은 돈 안뜨게 함수르 만듬

# 비공개 메서드

class Person12:
    def __greeting(self):
        print('hello')

    def hello(self):
        self.__greeting()

gian = Person12()
# gian.__greeting()  외부 접근 불가능
gian.hello()


# exercise
class knight:
    def __init__(self, health, mana, armor):
        self.health = health
        self.mana = mana
        self.armor = armor

    def slash(self):
        print('베기')

x = knight(health=542.4, mana=210.3, armor=38)
print(x.health, x.mana, x.armor)
x.slash()

# TEST

class Annie:
    def __init__(self, health, mana, ability_power):
        self.health = health
        self.mana = mana
        self.ability_power = ability_power

    def tibbers(self):
        print(f'티버: 피해량 {self.ability_power * 0.65 + 400}')
        print('티버: 피해량 {}'.format(self.ability_power * 0.65 + 400))

health, mana, ability_power = map(float, input().split())

x = Annie(health=health, mana=mana, ability_power=ability_power)
x.tibbers()
