import functools

def foo(args):
    sum = 0
    sum = functools.reduce(lambda x, y: x+y, args)
    print(sum)

def boo(args):  #  *args -> ([1,2,3,4],)
    sum = 0
    for i in args:
        sum += i

    print(sum)


a = [1, 2, 3, 4]

foo(a)
boo(a)
