#클래스 정의 기존 비슷한 기능 클래스를 상속받음(받으면 무조건 초기화 해줘야함)
from Ch06.sub1.Account import Account

class StockAccount(Account):

    def __init__(self, bank,id,name,money,stock,amount,price):
        # self.bank = bank
        # self.id = id
        # self.name = name
        # self.money = money
        super().__init__(bank,id,name,money)
        #초기화 명령(ctrl+__init__누르면 부모(super)한테감)
        self.stock = stock
        self.amount = amount
        self.price = price

    # def deposit(self,money):
    #     self.money += money
    # def withdraw(self,money):
    #     self.money -= money
    def sell(self,amount,price):
        print('{}을 {}개 {}가격에 판매함'.format(self.stock, amount, price))
    def buy(self,amount,price):
        print('{}을 {}개 {}가격에 구매함'.format(self.stock, amount, price))

    def show(self):
        super().show()
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)

