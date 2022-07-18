'''
# 예제 05. [오류 해결] 숫자의 길이 구하기

# 문제

> 아래 코드는 숫자의 길이를 구하는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

### 오류 코드

number = 22020718
print(len(number))

### Output
8
'''

number = 22020718
num_len = 0
while number:
    number//=10
    num_len+=1
print(num_len)

# 원인 : TypeError: object of type 'int' has no len()
# ===> 자료형 에러, int형 객체는 len()이 없다.