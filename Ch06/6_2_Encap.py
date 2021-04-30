"""
날짜:2021/04/30
이름:고현석
내용:파이썬 클래스 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

kb = Account('국민은행','101-21-1091','김유신',30000)
kb.deposit(10000)
kb.withdraw(5000)

# kb.__money -= 1
# 캡슐화(정보은닉)을 이용하여 취약코드 예방
kb.show()