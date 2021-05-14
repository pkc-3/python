# 함수 스코프 예

# (1) 지역변수 예
x = 50
def local_func(x):
    x += 50 #지역변수
local_func(x)
print('x=',x)

# (2) 전역 변수 예
def global_func():
    global x #전역변수 x 사용
    x += 50 # x+50 = 100

global_func()
print('x=', x)