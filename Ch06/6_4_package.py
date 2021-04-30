"""
날짜:2021/04/30
이름:고현석
내용:파이썬 패키지와 모듈 실습하기 교재 p175
"""
import Ch06.sub2.calc #r1처럼 사용해야함
import Ch06.sub2.calc as c  #as로 별칭 만들어줌 r2에 적용
from Ch06.sub2.calc import * #def 전부 들고옴 r3부터 적용

r1 = Ch06.sub2.calc.plus(1,2)
r2 = c.minus(1,2)
r3 = multi(3,4)
r4 = div(4,2)
print('r1:',r1)
print('r2:',r2)
print('r3:',r3)
print('r4:',r4)