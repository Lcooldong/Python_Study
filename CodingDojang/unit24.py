# 문자열 리스트

# replace
print('hello, world'.replace('world', 'Python'))

# split
a = 'apple pear grape pineapple orange'.split()
print(a)

b = 'apple, pear, grape, pineapple, orange'.split(', ')  # 띄어쓰기도 중요
print(b)

# join
c = '+'.join(b)  # '+'
print(c)
c = ' '.join(b)  # 빈칸
print(c)

# upper, lower
print('python'.upper())
print('PYTHON'.lower())

print('==========================')

# strip
print('  a b c  '.lstrip())
print('  a b c  '.rstrip())
print('  a b c  '.strip())

print(',  a b c  .'.lstrip(',.'))
print(',  a b c  .'.rstrip(',.'))
print(',  a b c  .'.strip(',.'))
print(',  a b c  .'.strip(',. '))   # 빈칸도 포함

import string
print(', python.'.strip(string.punctuation))
print(', python.'.strip(string.punctuation + ' '))    # 빈칸 추가
print(', python.'.strip(string.punctuation).strip())  # strip default 는 빈칸
print(string.punctuation)


# just
print('a, b, c'.ljust(10), end=""), print("|")
print('a, b, c'.rjust(10), end=""), print("|")

# center
print('|', end="")
print('level'.center(11), end="")
print('|')


# zfill
print('123'.zfill(5))
print('123'.zfill(4))
print('12.35'.zfill(6))
print('hi'.zfill(5))


# find  위치  index 로 출력
print('don\'t worry'.find('\''))
print('don\'t worry'.find('t'))
print('don\'t worry'.find('o'))
print('don\'t worry'.rfind('o'))
print('don\'t worry'.rfind('k'))    # 없으면 -1 리턴

# index
print('be a hero'.index('e'))
print('be a hero'.rindex('e'))

# count
print('I want to be a god'.count('od'))

# format, 정렬
print('{0:<10}'.format('python'))
print('{0:>10}'.format('python'))

print('{0:04d}'.format(123))
print('{0:4d}'.format(123))
print('{0:.4f}'.format(12.3))
print('{0:07.2f}'.format(12.3))

print('{0:0<10.2f}'.format(321))
print('{0:0>10.2f}'.format(321))
print('{0:>10.2f}'.format(321))
print('{0:@>10.2f}'.format(321))

print('%s' % format(1324421, ','))
print('%10s' % format(1324421, ','))
print('{0:,}'.format(231214))
print('{0:>10,}'.format(231214))
print('{0:>10,}'.format(231214))
print('{0:0>10,}'.format(231214))

# filepath
path = 'C:\\Users\\dojang\\python.exe'
x = path.split('\\')
filename = x[-1]
print(filename)

# raw
print('1\n2\n3\n')
print(r'1\n2\n3\n')


# TEST
str = '51900;83000;158000;367500;250000;59200;128500;1304000'   # 8개
str1 = list(map(int, str.split(';')))
#str1 = list(map(int, input().split(';')))
str1.sort(reverse=True)

# for i in range(len(str1)-1):
#     if int(str1[i]) < int(str1[i+1]):
#         temp = str1[i+1]
#         str1[i+1] = str1[i]
#         str1[i] = temp

print(str1)
print(str1[0])
print(type(str1[0]))
for i in range(len(str1)):
    print('{0:>9,}'.format(str1[i]))

print('Answer')

# str = list(map(int, input().split(';')))
# str.sort(reverse=True)
# for i in range(len(str)):
#     print('{0:>9,}'.format(str[i]))