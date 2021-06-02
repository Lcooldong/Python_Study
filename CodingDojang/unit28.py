# 회문 판별, N-gram

# word = input('단어를 입력하세요')
word = 'abcdcba'
is_palindrome = True
print(len(word)//2) # 소수점 버림 나눗셈
for i in range(len(word)//2):
    if word[i] != word[-1-i]:
        is_palindrome = False
        break

print(is_palindrome)


# [::-1] 문자열을 반대로 뒤집음
print(word == word[::-1])

# 리스트 reversed
print(list(word) == list(reversed(word)))

# join, reversed
print(word == ''.join(reversed(word)))
print('+'.join(word))   # join 은 리스트 구분자(,) 사이에 '+'을 넣음


# for N-gram
text = 'Hello'
for i in range(len(text) - 1):
    print(text[i], text[i+1], sep='')   # sep 구분자 사이에 틈 x

# list zip
print(list(zip(text, text[1:])))    # 1~끝이라서 하나 적음

# 참고용
t = 'project'
a = list(t)
print(a)
print(list(zip(a)))

# 3-gram
text = 'this is python script !!'
words = text.split()
print(words)
print(list(zip(words, words[1:], words[2:])))

# 자동 추가 N-gram
text = 'hello'
gram = [text[i:] for i in range(3)]  # gram 순서를 나눈것
print(gram)
gram = list(zip(*gram))  # zip 내부는 'a', 'b'로 한문자씩 구분되어야함
print(gram)


# exercise

# n = int(input())
n = 7
text = 'Python is a programming language that lets you work quickly'
words = text.split()
if len(words) < n:
    print('Wrong')
else:
    # n_gram = [words[i:] for i in range(n)]
    # gram = list(zip(*n_gram))
    # print(*gram)

    n_gram = zip(*[words[i:] for i in range(n)])
    print(n_gram)   # zip 주소
    for i in n_gram:
        print(i)

# TEST

# 쓰기
lines = [['apache'],
         ['decal'],
         ['did'],
         ['neep'],
         ['noon'],
         ['refer'],
         ['river']]

# print(len(lines))
# print(*lines[1])
# print(*lines[2])
# print(str(*lines[1]) + 't')

new_lines = list()
for i in range(len(lines)):
    temp = [str(*lines[i]) + '\n']
    new_lines.append(temp)

# print(new_lines)
with open('words2.txt', 'w') as file:
    for i in new_lines:
        file.write(*i)

# 읽기        text 파일이 words2 로 되어있음
with open('words2.txt', 'r') as file:
    for line in file:
        line = line.strip('\n')
        if line == line[::-1]:
            print(line)


