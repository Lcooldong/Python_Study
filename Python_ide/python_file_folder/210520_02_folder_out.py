with open("../../test_folder/t1.txt", "w", encoding="utf-8-sig") as out_file:
    out_file.write("hi1")

with open("./test_folder2/t2.txt", "w", encoding="utf-8-sig") as out_file:
    out_file.write("hi2")

with open("t3.txt", "w", encoding="utf-8-sig") as out_file:
    out_file.write("hi3")

with open("test_folder2/t4.txt", "w", encoding="utf-8-sig") as out_file:
    out_file.write("hi4")

# filePath = 'C:/Users/'
# out_file = open(filePath, 'w')
# out_file.close()


