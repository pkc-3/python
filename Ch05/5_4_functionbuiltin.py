"""
날짜:2021/04/29
이름:고현석
내용:파이썬 내장함수(자주 쓰는 함수기능이 파이썬에 있음) 교재 p118
"""

import math
import random
import time

r1 = abs(-5) #절대값 함수
print('r1:',r1)

r2 = math.ceil(1.2)#올림함수
r3 = math.ceil(1.8)

print('r2:',r2)
print('r3:',r3)

r4 = math.floor(1.2)#내림함수
r5 = math.floor(1.8)
print('r4:',r4)
print('r5:',r5)

r6 = round(1.2)#반올림
r7 = round(1.8)
print('r6:',r6)
print('r7:',r7)

r8 = math.sqrt(4)#제곱근
r9 = math.sqrt(9)
print('r8:',r9)
print('r9:',r9)

#random
num1 = random.random()
print('num1:',num1) #0~1사이 임의의 실수

num2 = num1 * 10
print('num2:',num2) #0~10사이 실수

num3 = math.ceil(num2)
print('num3:',num3) #1~10사이 정수

num4 = math.ceil(random.random()*10)
print('num4:',num4) #1~10사이 정수

#날짜 시간
t1 = time.time()#유닉스타임으로 표시됨
print('t1:',t1)
t2 = time.ctime()
print('t2:',t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)
print('%s년 %s월 %s일' % (year,month,date))
print('%s시 %s분 %s초' % (hour,min,sec))