# 재귀호출
import sys


def hello(count):
    if count == 0:
        return

    print('hello', count)
    count -= 1
    hello(count)

hello(4)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(4))

def is_palindrome(word):
    if len(word) < 2:   # 가운데 하나만 남을 떄까지
        return True
    if word[0] != word[-1]: # 양끝(대칭) 다르면
        return False
    return is_palindrome(word[1:-1])    # -1 마지막, 포함 X

print(is_palindrome('hello'))
print(is_palindrome('level'))
print(is_palindrome('alevela'))

print('hia'[:-1])

#sys.setrecursionlimit(2000)  # 최대 재귀호출 횟수를 2000으로 늘림