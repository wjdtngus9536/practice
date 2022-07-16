word = "HappyHacking"

count = 0

for char in word:
    if char in "aeiou":
        count += 1

print(count)

# 원인 or "e" 방식으로 span 하게 되면 e의 상수값인 102는 True로 나오게 되고 if 문은 항상 참인 경우로 동작하게 된다.