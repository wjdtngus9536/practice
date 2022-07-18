number_list = [1, 23, 9, 6, 91, 59, 29]
Max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)                                                # TypeError: 'int' object is not callable

if Max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif Max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")  

# 원인 : 변수명으로 예약어를 사용하였기 때문에 line 5 에서는 max라는 객체를 함수처럼 호출하려는 형태가 돼었다.
# 예약어는 모두 소문자로 이루어져있기 때문에 max를 대문자로 변경해주자