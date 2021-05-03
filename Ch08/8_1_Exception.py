"""
날짜:2021/05/03
이름:고현석
내용:파이썬 예외처리 실습 교재 p212

"""

#try ~except
num1, num2 = 1, 0

r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = 0              #try 안에서만 선언되면 print에서 인식못함.
try:
    r4 = num1 / num2
except:
    print('예외발생...') #에러가 발생할때 프로그램이 멈추진 않음 (0일 경우) r4값 그대로 출력

print('r1 :',r1)
print('r2 :',r2)
print('r3 :',r3)
print('r4 :',r4)
print('=====================================================')
#try ~except
num1, num2 = 1, 0
r1= r2= r3= r4 = 0
try:
    r1 = num1 + num2
    r2 = num1 - num2
    r3 = num1 * num2
    r4 = num1 / num2
except:
    print('예외발생...')

print('r1 :',r1)
print('r2 :',r2)
print('r3 :',r3)
print('r4 :',r4)

#try ~ except ~ finally
people = ['김유신','김춘추','장보고']
try:
    # 예외(에러)가 발생할 가능성이 있는 코드영역
    for i in range(4): #범위 초과로 오류남
        print(people[i])
except IndexError:
    # 예외가 발생했을때 처리할 코드영역
    print('유효하지 않은 인덱스 참조')
finally:
    # 예외 발생여부 관계없이 마지막에 실행되는 코드영역
    print('예외처리 완료')
#try ~ except ~ else
animal = ['사자','코끼리','호랑이','기린']
result = None
while True:

    try:
        # 예외(에러)가 발생할 가능성이 있는 코드영역
        print('동물을 선택해보세요.')
        print('1:사자,2:코끼리,3:호랑이,4:기린,0:종료')

        answer = int(input('선택 : '))
        if answer == 0:
            break
        elif answer < 0:
            raise Exception('음수는 안됩니다.')#오류를 발생시킴(-값을 입력한 경우)

        result = animal[answer-1]

    except Exception as e:
        # 예외가 발생했을때 처리할 코드영역
        print('에러 내용 :',e)
        print('정확히 0~4 사이에 숫자를 입력하세요.')
    else:
        # 예외가 없을 경우 처리할 코드영역
        print('선택한 동물은 '+result+'입니다.')
print('프로그램 종료')