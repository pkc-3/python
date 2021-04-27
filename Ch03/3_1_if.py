"""
날짜:2021/04/27
이름:고현석
내용:파이썬 조건문 if 실습 교재 p68
"""

#if
num1, num2 = 1,2
if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
    print('num1은 num2보다 크다')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고 num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    print('num1은 0보다 크고 num2는 1보다 크다.')

#if else
num3,num4 = 3,4

if num3 > num4:
    #조건이 참일때
    print(num3, '이', num4, '보다 크다')
else:
    #조건이 거짓일때
    print(num3,'이',num4,'보다 작다')
    pass
#if - elif - else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

#삼항조건문

num = 3
result = num*2 if num >= 5 else num +2 #num이 5 이상일때는 x2 한다. 5이하라서 else로 감.
print('result:', result)

#연습문제
score = float(input('점수 입력: ')) #소수점 까지 입력하려면 float 정수만 넣으려면 int

print('점수 확인:',score)
if score>= 90 and score <= 100:
    print('A 입니다')
elif score>= 80 and score < 90:
    print('B 입니다')
elif 70 <= score < 80:
    print('C 입니다')
elif 60 <= score < 70:
    print('D 입니다')
elif score < 60:
    print('F 입니다')
else:
    print('잘못 입력하였습니다.')