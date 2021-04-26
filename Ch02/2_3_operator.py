"""
날짜:2021/04/26
이름:고현석
내용:파이썬 연산자 실습하기 교체 p38
"""

#대입연산자
a = 1
b = c = d = 0
e, f, g = 7, True, 'apple'

print('a:', a)
print('b:', b)
print('f:', f)
print('g:', g)

#산술연산자
num1 = 1
num2 = 2
num3, num4 = 3, 4

r1= num1 + num2
r2= num1 - num2
r3= num2 * num3
r4= num4 / num3 #소수점 밑에 부분도 표시
r5= num4 // num3 #정수부분만 표시
r6= num4 % num3 #나머지
r7= num4 ** num2 #거듭제곱

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)
print('r4 :', r4)
print('r5 :', r5)
print('r6 :', r6)
print('r7 :', r7)

#복합대입연산자
num5,num6,num7,num8 = 5, 6, 7, 8

num5 += 1 # 5 + 1
num6 -= 2 # 6 - 2
num7 *= 3 # 7 * 3
num8 /= 4 # 8 / 4

print('num5:', num5)
print('num6:', num6)
print('num7:', num7)
print('num8:', num8)

#비교연산자
var1 = 1
var2 = 2

rs1 = var1 > var2 # var1이 var2보다 크다
rs2 = var1 < var2 # var1이 var2보다 작다
rs3 = var1 >= var2 # var1이 var2보다 크거나 같다
rs4 = var1 <= var2 # var1이 var2보다 작거나 같다
rs5 = var1 == var2 # var1이 var2보다 서로 같다
rs6 = var1 != var2 # var1이 var2보다 서로 다르다

print('rs1:',rs1)
print('rs2:',rs2)
print('rs3:',rs3)
print('rs4:',rs4)
print('rs5:',rs5)
print('rs6:',rs6)
#논리연산자
var3 = 3
var4 = 4

res1=(var3 > 2) and (var4 > 3) #True 둘다 True여야 True(and)
res2=(var3 > 2) and (var4 > 4) #False
res3=(var3 > 2) or (var4 > 4) #True 하나만 True면 True(or)
res4=not (var3 > var4) #True 괄호 안에꺼가 False 인데 not 으로 True 바꿈

print('res1:',res1)
print('res2:',res2)
print('res3:',res3)
print('res4:',res4)