import random
a = random.random()
print(a)

b = random.randint(1,6)
print(b)


dice = [1,2,3,4,5,6]
c = random.choice(dice)
print(c)

dice2 = (1, 2, 3, 4, 5 ,6)
d = random.choice(dice2)
print(d)

dice2 = range(1,7)
e = random.choice(dice2)
print(e)

dice3 = "abcde"
f = random.choice(dice3)
print(f)

