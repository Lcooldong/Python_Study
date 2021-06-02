text = list(map(int,input().split(';')))
text_sort = reverse.sorted(text)

print(text_sort)

for i in range(len(text) ):
    print('{0:,}'.format(text[i]))
