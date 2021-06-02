# set

fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
print(fruits)

# 조합(순서에 상관 없음) -> 중복 불가
fruits = {'orange', 'orange', 'cherry'}
print(fruits)

# 특정 값 확인
print('orange' in fruits)
print('grape' in fruits)
print('grape' not in fruits)

# 세트 생성
a = set('people')
print(a)

b = set(range(5))
print(b)

c = set()
print(c)
print(type(c))
d = {}
print(type(d))

e = set('인사합시다.')
print(e)

# 세트안에 세트 못넣음

# frozenset 추가, 삭제 연산 불가능
a = frozenset(range(10))
print(a)

# 중첩 세트 만들 때 frozenset 사용
b = frozenset({frozenset({1, 2}), frozenset({3, 4})})
print(b)


# union 합집합
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(set.union(a, b))

# intersection 교집합
print(a & b)
print(set.intersection(a, b))

# difference 차집합
print(a - b)
print(set.difference(a, b))

# symmetric difference 대칭차집합  XOR
print(a ^ b)
print(set.symmetric_difference(a, b))
print(b ^ a)    # 대칭이라 같음
print(set.symmetric_difference(b, a))

# update, |=  추가
a = {1, 2, 3, 4}
a |= {5}
print(a)

a.update({6})
print(a)

# intersection_update, &=    교집합
a = {1, 2, 3, 4}
a &= {0, 1, 2, 3, 4, 5}
print(a)

a = {1, 2, 3, 4}
a.intersection_update({0, 1, 2, 3, 4, 6})
print(a)

# difference_update, -=   차집합
a = {1, 2, 3, 4}
a -= {4}
print(a)
a = {1, 2, 3, 4}
a.difference_update({2, 3})
print(a)

# symmetric_difference_update,  ^=  XOR
a = {1, 2, 3, 4}
a ^= {3, 4, 5, 6}
print(a)

a = {1, 2, 3, 4}
a.symmetric_difference_update({3, 4, 5, })
print(a)


# subset    부분집합 확인
a = {1, 2, 3, 4}
print(a <= {1, 2, 3, 4})
print(a <= {1, 2, 3, 4, 5})
print(a.issubset({1, 2, 3, 5}))

# proper subset  진부분집합(같지는 않은 부분집합)
a = {1, 2, 3, 4}
print(a < {1, 2, 3, 4, 5})  # 포함 되는가

# superset  상위집합
a = {1, 2, 3, 4}
print(a >= {1, 2, 3, 4})        # True
print(a >= {1, 2, 3, 4, 5})     # False
print(a.issuperset({1, 2, 3}))  # True


# proper superset 진상위집합
a = {1, 2, 3, 4}
print(a > {1, 2, 3, 4})   # False
print(a > {1, 2})         # True

# 일치 여부 확인
a = {1, 2, 3, 4}
print(a == {1, 2, 3, 4})
print(a == {1, 3, 4, 2})    # 순서 상관 없음
print(a != {2, 3})  # 다름 확인

# 겹침 확인
a = {1, 2, 3, 4}
print(a.isdisjoint({5, 6, 7, 8}))   # 안겹침  True
print(a.isdisjoint({5, 6, 1, 8}))   # 1 겹침 False

# add
a = {1, 2, 3, 4}
a.add(5)
print(a)

# remove    특정요소 삭제, 없으면 에러
a.remove(3)
print(a)

# discard   특정요소 삭제, 없으면 그냥 넘어감
a.discard(2)
a.discard(3)
print(a)

# pop   # 임의의 요소 삭제, 해당요소 반환, 요소 없으면 에러
a.pop()     # 1 제거
print(a.pop())  # 4
print(a)

# clear
a.clear()
print(a)

# len
a = {1, 2, 3, 4}
print(len(a))

# 그냥 복사 같음
a = {1, 2, 3}
b = a
print(a is b)   # True
print(a == b)
b.add(4)
print(a)
print(b)


# copy
a = {1, 2, 3}
b = a.copy()
print(a is b)   # False
print(a == b)

b.add(4)
print(a)
print(b)

# for   숫자는 차례대로, 문자는 그대로
for i in {1, 3, 5, 'b', 7, 'a', 2}:
    print(i)


# for, if 문
a = {i for i in 'bada'}
print(a)

a = {i for i in "pipineapple" if i not in 'ple'}
print(a)


# exercise
# 1~100, 3과 5의 공배수 세트

a = {i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0}
print(a)

# TEST

a, b = map(int, input().split())
a = {i for i in range(1, a+1) if a % i == 0}
b = {i for i in range(1, b+1) if b % i == 0}

divisor = a & b
print(divisor)

result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)

