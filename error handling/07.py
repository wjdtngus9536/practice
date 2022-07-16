number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

# 원인 : count 들여쓰기 누락, print 몫 연산 아닌 나눗셈 연산으로 수정 필요