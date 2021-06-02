import sys

#print("hello", file=sys.stdout)    # 표준 출력
#print("error", file=sys.stderr)    # 표준 에러

out_file = open("test.txt", "w", encoding="utf-8")
print("국어:100", file=out_file)
print("영어:90", file=out_file)
out_file.write("과학:80\n")
out_file.close()
