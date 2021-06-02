# dict

# setdefault (추가)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.setdefault('e')
print(x)

y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y.setdefault('e', 50)
print(y)


# update (추가, 수정)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
x.update(a=90)
print(x)

y = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
y.update(e=50)
print(y)

z = {1: 'c', 2: 'b'}
z.update({1:'a', 3:300})
print(z)

z.update(zip([3, 4], ['THREE', 400]))
print(z)


# pop

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.pop('b'))
print(x)

print(x.pop('z', 0))    # 키 없을 때 지정한 숫자 반환

del x['a']
print(x)


# popitem (3.5 이하 랜덤  3.6 이상은 마지막 것)
x.popitem()
print(x)


# get
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.get('c'))

print(x.get('z', 5))  # 없을 때 지정한 숫자 반환


# items, key, value
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.items())
print(x.keys())
print(x.values())


# fromkeys (키리스트)

keys = ['a', 'b', 'c', 'd', 0]
x = dict.fromkeys(keys)     # 키로 딕셔너리 생성
print(x)
x = dict.fromkeys(keys, 10)
print(x)
print(x['a'])
print(x[0])

# defaultdict
from collections import defaultdict
x = defaultdict(int)    # 딕셔너리 생성, 키 없을 때 기본값 0 리턴
print(x['z'])

z = defaultdict(lambda: 'python')
print(z['a'])
print(z[0])

# for 키
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for i in x:
    print(i, end=" ")

print()

for key in x.keys():
    print(key, end=" ")

print()

# for 값

for value in x.values():
    print(value, end=" ")

print()


# for 키, 값
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
for key, value in x.items():
    print(key, value)

for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items():
    print(key, value)

# 키리스트 for -> 장점: 특정값 삭제할 수 있음
keys = ['a', 'b', 'c', 'd', 0]
x = {key: value for key, value in dict.fromkeys(keys, 5).items()}
print(x)

y = dict.fromkeys(keys, 5)  # 장점 : 간단히 표현 가능
print(y)

# 값을 키로 바꾸고,  값 0으로 초기화
z = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
z_value = {value: 0 for value in z.values()}
print(z_value)

# 값과 키 바꾸기
z = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
z_change = {value: key for key, value in z.items()}
print(z_change)


# 특정 값 제거할 때 for문, if문 사용
x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

# for key, value in x.items():    <- 문제 발생 크기 변화
#     if value == 20:
#         del x[key]

x = {key:value for key, value in x.items() if value != 20}     # if문 사용하여 제거
print(x)


# 중첩 딕셔너리   [키][키] 배열처럼 사용

terrestrial_plant = {
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period':87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641
    },
    'Mars': {
        'mean_radius': 3389.9,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600
    }
}

print(terrestrial_plant['Venus']['mean_radius'])


# 딕셔너리를 복사하려면 copy() 사용
x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
y = x
print(x is y)   # 같음
y['a'] = 100
print(x)
print(y)

x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
z = x.copy()
print(x is z)   # 다름
print(x == z)   # 값은 같음
z['a'] = 100
print(x)
print(z)

# 중첩 딕셔너리 할당, 복사
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = x.copy()
print(x)
print(y)

x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y['a']['python'] = '2.7.2'
print(x)    # 높은 버전은 딥카피됨
print(y)    # <- 낮은 버전에서는 둘이 같음

import copy
x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
y = copy.deepcopy(x)
y['a']['python'] = '2.7.15'
print(x)
print(y)

print(dict.clear(y))

# exercise

maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
average = sum(maria.values())/len(maria)
print(average)

# TEST

# keys = input().split()
# values = map(int, input().split())
#
# x = dict(zip(keys, values))
# del x['delta']
# x = {key: value for key, value in x.items() if value != 30}
# print(x)

# dictionary  합치기
# 1. update 
x = {'a': 1, 'b': 2}
y = {'c': 3, 'd': 4}
x.update(y)
print(x)

# 2. 언패킹
z = {**x, **y}
print(z)