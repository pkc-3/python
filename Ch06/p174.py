# import 모듈 내장클래스 예

# (1) 모듈 내장 클래스 import
import datetime # 모듈 import
from datetime import date, time

# (2) date 클래스
help(date) #date 클래스 도움말

today = date(2019,10,23) #date 객체 생성
print(today) #date 객체 정보

# date 객체 멤버변수 호출
print(today,year) #2019
print(today.month) #10
print(today.day) #23

# date 객체 메서드 호출
w = today.weekday() # monday==0 ... sunday==6
print('요일 정보 : ', w) #요일 정보

# (3) time 클래스
help(time) # time 클래스 도움말

currTime = time(21,4,30) #time 객체 생성
print(currTime) #time 객체 정보

#time 객체 멤버변수 호출
print(currTime.hour) #21
print(currTime.minute) #4
print(currTime.second) #30

#time 객체 메서드 호출
isoTime = currTime.isoformat () #HH:MM:SS
print(isoTime)