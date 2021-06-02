class Person:
    def __init__(self, na, ag): # 항상 첫번째 인자는 주소가 됨
        print(self, '생성')
        self.name = na
        self.age = ag

p1 = Person('John', 23)
p2 = Person('Justin', 28)

print(p2.name, p2.age)