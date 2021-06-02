from pprint import pprint
#col, row = map(int, input().split())




#matrix = []
#for i in range(row):
#    matrix.append(list(input()))

matrix = [['*', '.', '*'],
          ['.', '.', '.'],
          ['.', '*', '.']]

col = len(matrix[0]) #가로
row = len(matrix) #세로

print(col)
print(row)


#print(matrix[0][0])



# "." 을 0으로
for i in range(len(matrix)):
    for j in range(len(matrix)):
       if matrix[i][j] == ".":
           matrix[i][j] = 0

pprint(matrix, indent = 1, width = 20)


print("-------------------")              


for i in range(len(matrix)):                #i 세로
    for j in range(len(matrix[i])):         #j 가로
       if matrix[i][j] == "*" :   #최상단      and j+1 < len(matrix[i])
            print(i, j)
           
            if i == 0 and matrix[i][j+1] != "*":          #첫번째 줄
                matrix[i][j+1] += 1
                if j == 0 and matrix[i+1][j] != "*":      #첫번째 열
                    matrix[i+1][j] += 1
                    if matrix[i+1][j+1] != "*":
                        matrix[i+1][j+1] += 1

                if j == len(matrix[i])-1 and matrix[i][j-1] != "*":                 #우측
                    matrix[i][j-1] += 1
                    if matrix[i+1][j-1] != "*":
                        matrix[i+1][j-1] += 1





print("-------------------")
pprint(matrix, indent = 1, width = 20)




    
#좌측


#최하단



#중간


for row in matrix:
    for col in row:
        print()




#for i in range(row):
#    for j in range(col):
#        if matrix[i][j] == '*':
#            print(int(1), end = "")
#        else:
#            print(int(0), end = "")
#    print()

