'''
# 문제

> 두 수를 Input으로 받아 합을 구하는 코드이다.
코드에서 오류를 찾아 원인을 적고, 수정하세요.
> 

### 오류 코드

```python
numbers = input().split()
print(sum(numbers))
```

### Input

```
10 20
```

### Output

```
30
```
'''

# 원인
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sum 함수는 str 데이터 타입을 지원하지 않음.
numbers = map(int,input().split())
print(sum(numbers))