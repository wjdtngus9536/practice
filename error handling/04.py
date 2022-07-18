'''
# 문제

> 아래 코드는 문자열을 입력받아 단어별로 나누는 코드입니다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

### 오류 코드

```python
words = list(map(int, input().split()))
print(words)
```

### Input

```
I'm Tuotur 6
```

### Output

```
["I'm", 'Tutor', '6']
```
'''

words = input().split()
print(words)

# 원인

#  File "c:\Users\suhyeon\Desktop\practice\error handling\04.py", line 28, in <module>
#    words = list(map(int, input().split()))                 # 문자열을 정수로 변환하려 함
#ValueError: invalid literal for int() with base 10: "I'm"   # int()함수에 맞지 않은 어휘