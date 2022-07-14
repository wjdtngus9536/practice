def print_idx(word):
    for i in range(len(word)):
        if word[i]=='a':
            print(i)
            return
    print(-1)    

word = 'banana'
print_idx(word)