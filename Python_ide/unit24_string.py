a = "hi, hello".replace('hello', 'python')
print(a)

table = str.maketrans('aeiou', 'AE345')
b = 'apple'.translate(table)
print(b)
print(table) 
print(type(table))  # 딕셔너리

c = "apple pear grape pineapple orange".split()
print(c)

d = "apple, pear, grape, pineapple, orange".split(',')
print(c)


e ='-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
print(e)

f = 'dpi'.upper()
print(f)

print(f.lower())

g = '   -bamusun-    '
print(g.lstrip())
print(g.rstrip())
print(g.strip())

h = '!,.python.!#@'
print(h.lstrip('!@'))
print(h.rstrip('!@.')) # 오른쪽 가장 밖에 거 삭제
print(h.strip('!@.'))


import string
i =  ', python.....'.strip(string.punctuation)
print(i)    
print(string.punctuation)#양쪽 특수문자 전체 삭제

i =  ', python.'.strip(string.punctuation + ' ')
print(i)    # 빈칸도 제거

i = ', python.'.strip(string.punctuation).strip()
print(i) #메서드 체이닝(문자열에서 메서드 연속달기 가능)

j = 'abcde'.ljust(10)
print(j)
j = 'abcde'.rjust(10) #지정된 길이로 만들고 오른쪽 정렬
print(j)
j = 'abcde'.center(10)
print(j)
j = 'abcdef'.center(11) #왼쪽공백3오른쪽공백2
print(j)

k = '35'.zfill(4)
print(k)
k = '3.5'.zfill(6)
print(k)
k = 'hi'.zfill(10)
print(k)


l = 'apple pineapple'.find('e')
print(l) #위치 찾기

l = 'apple pineapple'.find('xy')
print(l)  # 없으면 -1

l = 'apple pineapple'.rfind('pl')
print(l)  

l = 'apple pineapple'.index('pl')
print(l) # 처음 찾은 위치

l = 'apple pineapple'.rindex('pl')
print(l) # 오른쪽에서 처음 찾은 위치

l = 'apple pineapple'.count('pl')
print(l) #갯수 


print('I am %s' %'james')
name = 'maria'
print('I am %s' %name)
print('I am %d' %20)

print('%10.3f' %2.6)
print('%-10s' %'python') #왼쪽정렬(길이10)

print('Today is %s %s' %("Fool\'s", 'day' ))

print('Hello, {0}'.format('world!'))

print('Hello, {0} {2} {1}'.format('Python', 'script', 3.7))

print('Hello, {language} {version}'.format(language = 'Python', version = '3.7'))

language = 'python'
version = 3.7
print(f'Hello, {language}{version}')

print('{{{0}}}' .format('hi'))

print('{0:<10}'.format('10length'))
print('{0:>10}'.format('10length'))
print('{:>10}'.format('hello'))

print('%03d' % 2)
print('{0:03d}'.format(27))

print('%06.3f' %3.7) #"." 도 자리수 차지함
print('{0:06.3f}'.format(3.7))

print('{0:0<10}'.format(15))
print('{0:0>10}'.format(15))
print('{0:0>10.2f}'.format(15))
print('{0:0<10.3f}'.format(15)) #왼쪽 정렬이라 .3 무시

print('{0:>10}'.format(15))
print('{0:<10}{1:<10}'.format(15, 20))

print('{0:$>10}'.format(15))

print(format(13000, ","))

print('%20s' %format(11551200, ','))
print('{0:20,}'.format(214214))
