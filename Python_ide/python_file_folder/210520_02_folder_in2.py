with open('test_folder2/abc.txt','w', encoding='utf-8') as out_file:
    out_file.write('hi\n')
    print('good',file=out_file)
    out_file.write('hello\n')
    out_file.write('bonjour\n')

print('--------------------------------')

with open('test_folder2/abc.txt', 'r', encoding='utf-8') as in_file:
    lines = in_file.read()
    print(lines)


print('--------------------------------')



with open('test_folder2/abc.txt', 'r', encoding='utf-8') as in_file:
    print(in_file.readline(), end="")   #readline으로 읽은 문자열에 이미\n 포함 + print()
    print(in_file.readline().strip())
    print(in_file.readline())
    print(in_file.readline())

print('--------------------------------')

with open('test_folder2/abc.txt', 'r', encoding='utf-8') as in_file:
    while True:
        line = in_file.readline()
        if not line:
            break
        print(line, end="")

print('--------------------------------')

with open('test_folder2/abc.txt', 'r', encoding='utf-8') as in_file:
    lines = in_file.readlines()     # 리스트로 읽음
    print(lines)

print('--------------------------------')

with open('test_folder2/abc.txt', encoding='utf-8') as in_file:
    for line in in_file:
        line = line.rstrip()        # \n
        word_list = line.split()    # 스페이스
        for word in word_list:
            print(word)
        
    #print(in_file.read())  전체 
    #print(in_file.readline().rstrip())  <-  스페이스, 탭(\t), 줄바꿈 (\r,\n) 제거
