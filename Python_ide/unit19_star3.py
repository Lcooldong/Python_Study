x=int(input())
for i in range(x):
    print(' '*(x-i-1), end='')  # x (높이)- i (세로,row) -1 만큼 빈칸
    for j in range(x):
        if i >= j :             #위 코드 빈칸 옆에  i,j 비교 만큼 별 그리기(왼쪽 산)
            print('@', end='')
    print('@'*i)              #end = ""때문에 오른쪽 옆으로 별x높이만큼 붙이고 다음줄
