
a = int(input())
l = 0

if a == 0 :
    l = 1

while a:
    a //= 10
    l += 1
print(l)