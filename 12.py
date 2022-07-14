word = 'aaassssss'
word = list(word)
i=0
while word[i:]:
    if word[i] == 'a':
        word.remove('a')
    else:
        i+=1
word = ''.join(word)
print(word)
