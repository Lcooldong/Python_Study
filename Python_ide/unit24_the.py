text = input()

words = text.split()
for i in range(len(words)):
    words[i] =words[i].strip(",.")

thefind = words.count('the')
print(thefind)
