# class inheritance
# parent class = super class
# child class = sub class

# is-a 관계
# 동등한 관계 (Student ia s Person)

class Person:
    def greeting(self):
        print('안녕하세요')

class Student(Person):
    def study(self):
        print('공부하기')

    @classmethod
    def admission(cls):
        fresh = cls()
        return fresh


Tom = Student.admission()
Tom.greeting()  # 상속받아서 가능
Tom.study()

# Student < Person 인가? 확인
print(issubclass(Student, Person))

# 포함 관계 : has-a 관계
# 상속 사용 X, 속성에 인스턴스를 넣어서 관리
# PersonList 가 Person1 포함 (PersonList has a Person1)
class Person1:
    def greeting(self):
        print('hi')

class PersonList:
    def __init__(self):
        self.person_list = []

    def append_person(self, person):    # has-a Person1 인스턴스
        self.person_list.append(person)