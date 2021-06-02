def is_prime(num):
    cnt = 0
    if num == 1:
        return "1 입니다"
    else:
        for i in range(2, num):     # 1과 자기 자신으로만 나눠지니까
            if num % i == 0:        # 자신보다 작은 값(자신-1)으로 나눠지면
                return print(False)        # 소수아님
        return print(True)                 # 자신으로만 나눠져서 소수임


def count_prime(num):           # 9 이면  2,3,5,7 출력    4개
    cnt = 1    # 2는 기본
    for num_range in range(2, num+1):     # 2,3,4,5,6,7,8,9 넣은 수까지
#        print(f"num_range : {num_range}", end="") # 목록
        flag = 0
        for i in range(2, num_range):     # i: 3-> 2 / 4-> 2,3 / 5-> 2,3,4,/ 9-> 2,3,4,5,6,7,8
            if num_range % i == 0:        # 소수인지 아닌지 확인
#                print(" 나눠진적있음 ", end="")  # 확인용
                flag = 0
                break
            else:
                flag = 1

        if flag == 1:
            cnt += 1
#        print()
    return print(cnt)



number = 6
is_prime(number)
count_prime(number)


