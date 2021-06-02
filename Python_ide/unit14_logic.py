kor, eng, mat, sci = map(int, input().split())
list_subject = [kor, eng, mat, sci]
list_length = len(list_subject)
sum = kor + eng + mat + sci
avg = sum/list_length

if  0 <= kor <= 100 and 0 <= eng <= 100 and 0 <= mat <= 100 and 0 <= sci <= 100:
    if avg >=80:
        print('합격')
    else:
        print('불합격')
    
else:
    print('잘못된 점수')
