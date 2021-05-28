# 문제3
# 팩토리얼(Factorial)을 계산하는 재귀함수의 빈 칸을 채우시오.

# 재귀 함수 정의
def Factorial(n):
    if n == 1:
        return 1
    else:
        result_fact = n * Factorial(n-1)
        return result_fact

result_fact = Factorial(int(input('팩토리얼 계산할 숫자를 입력하세요 : ')))
print('팩토리얼 결과 : ', result_fact)