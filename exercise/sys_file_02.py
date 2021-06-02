with open("test2.txt", "w", encoding="utf-8") as out_file2:   # close 없어도됨
    print("국어:100", file=out_file2)
    print("영어:90", file=out_file2)
    out_file2.write("과학:80\n")
    out_file2.close()

with open("../sample.txt", "w", encoding="utf-8") as out_file3:
    print("sample", end="", file=out_file3)
    out_file3.write("테스트연습\n")

with open("test.txt", "a", encoding="utf-8") as out_file4:   # 내용 추가
    out_file4.write("음악 : 80\n")
    out_file4.write("미술 : 70\n")