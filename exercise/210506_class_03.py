class Math:
#    def __init__(self):
#        pass

    @staticmethod   # 값 저장할 필요 없음
    def add(a,b):
        return a+b

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def bit_3(a):
        return (int(a*8))/8

a = Math()

print(a.add(10,20))
print(Math.bit_3(3.1512521))    # 소수점 3비트까지만 표현