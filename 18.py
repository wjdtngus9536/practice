word = 'banana'
d = {}

for c in word:
    if d.get(c) == None:
        d[c] = 1
    else:
        d[c]+=1

for i in d:
    print(i, d[i])