#start, stop = map(int, input().split())
start = 21
stop = 33

i = start

while True:
    if not (1 <=start <= 200):
        break

    if not (1 <=stop <= 200):
        break
----------------    
    if i > stop:
        break
    

    if i % 10 == 3:
        i += 1
        continue
----------------        
    print(i, end = ' ')

    i += 1



