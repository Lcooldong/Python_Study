import functools

def average(args):
    _sum = 0
    _sum = functools.reduce(lambda x, y: x+y, args)
    _average = _sum/len(args)
    return _average

a = [10, 20, 30, 40]

print(average(a))
