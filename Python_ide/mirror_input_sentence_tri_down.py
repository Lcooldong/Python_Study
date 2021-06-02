x = list('abcdef') #list(input())


#리스트의 범위를 생각할 것
#range(시작, 끝(자기 보다 하나큼), 증폭)
#abcdef 면 a만 살려야 하니까 len(x)-1
#리스트의 시작부분 "a"부분은 x[0] 즉, 0까지라서 그래서 끝 : -1(자신(제외)보다 하나 큰거)

for j in range(len(x)-1,-1, -1):    
    print(" "*j, end = '')
    for i in x[:len(x)-j]:
        print(i, end = '')
    for i in reversed(x[:-j-1]):
        print(i, end = '')
    print("")


