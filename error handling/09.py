from pprint import pprint

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 원인 :  fruit_count = {fruit: 1} 이렇게 작성하게되면 가장 마지막에 읽은 {salal berry : 1}로 fruit_count 을 초기화 시키는걸로 끝나게 됨.