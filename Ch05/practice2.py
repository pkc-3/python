# 문제2
# 중첩함수를 적용하여 다음 <조건>에 맞게 은행계좌 함수의 빈 칸을 채우시오.
#
# <조건1> 외부 함수 : bank_account() : 잔액(balance) outer 변수
# <조건2> 내부 함수 : getBalance() : 잔액확인
#                   deposit(money) : 입금하기
#                   withdraw(money) : 출금하기
# <조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력
# <조건4> 기타 나머지는 출력 예시 참조
#
# <출력 결과 예시>
# 최초 계좌의 잔액을 입력하세요 : 1000
# 현재 계좌 잔액은 1000원 입니다.
# 입금액을 입력하세요 : 15000
# 15000원 입금후 잔액은 16000원 입니다.
# 출금액을 입력하세요 : 3000
# 3000원 출금후 잔액은 13000원 입니다.

# 함수 정의

def bank_account():
    balance = bal
    def getBalance():
        return balance

    def deposit(money):
        nonlocal balance
        balance += money

    def withdraw(money):
        nonlocal balance
        if balance < money:
            print('잔액이 부족합니다.')
        else:
            balance -= money

    return getBalance, deposit, withdraw

