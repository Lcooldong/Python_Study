class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def print_pt(self):
        print("({} {})".format(self.x, self.y))

    def add(self, pt):  #pt -> 다른 오브젝트 점
        new_x = self.x + pt.x
        new_y = self.y + pt.y
        return Point(new_x, new_y)
    
    def __add__(self, other):   # 더하기를 다른 걸로 오버라이드
        new_x = self.x + other.x    # 쓰면 안됨
        new_y = self.y + other.y
        return Point(new_x, new_y)

p1 = Point(3,4)
p2 = Point(5,6)

#p3 = p1+p2  <- 오버라이드 된 것

p3 = p1.add(p2)
p3.print_pt()