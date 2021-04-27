#관계연산자 예
num1 = 100
num2 = 20
# (1) 동등비교
bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

#논리연산자 예


#두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)

#두 관계식 중 하나라도 같은지 판단
log_result = num1 >=50 or num2 <= 10
print(log_result)
log_result = num1 >=50
print(log_result)

#괄호 안의 관계식 판단 결과에 대한 부정
log_result = not(num1 >= 50)
print(log_result)