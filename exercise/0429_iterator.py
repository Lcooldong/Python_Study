a = [2, 3, 4]
a_iter = iter(a)
print(type(a))
print(type(a_iter))

print(dir(a))  # 어떤 변수와 메소드를 가지고 있는지

print(next(a_iter))
print(next(a_iter))
print(next(a_iter))
