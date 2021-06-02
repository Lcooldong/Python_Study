for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)


#3배수 5배수 15배수  or 숫자
#True or 숫자 = True, False or 숫자 = 숫자
 
a,b = map(int, input().split)

for i in range(a, b):
    if i % 5 == 0 and i % 7 == 0:
        print('FizzBuzz')    
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)
