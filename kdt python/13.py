word = 'apple'
t=[]
for i in range(len(word)-1, -1, -1):
	t.append(word[i])
word = ''.join(t)

print(word)