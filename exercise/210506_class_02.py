class Counter:
    def __init__(a,  start_num = 0):   # 생성자, a -> 주소
        a.num = start_num

    def increment(self):
        self.num += 1

    def reset(self):
        self.num = 0

    def print_current_value(self):
        print("Current_value :", self.num)

c1 = Counter(10)

c1.increment()

c1.print_current_value()