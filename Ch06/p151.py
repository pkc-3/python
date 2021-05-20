#함수와 클래스 예

# (1) 함수 정의
def calc_func(a,b) : #외부함수
    # 변수 선언 : 자료 저장
    x = a # 10
    y = b # 20

    def plus(): #내부함수
        p = x + y
        return p
    def minus():
        m = x - y
        return m
    return plus,minus
# (2) 함수 호출
p,m = calc_func(10,20)
print('plus =', p())
print('minus=', m())

# (3) 클래스 정의
class calc_class:
    #클래스 변수 : 자료저장
    x = y = 0

    #생성자 : 객체 생성 + 멤버 변수 초기화
    def __init__(self,a,b):
        self.x = a #10
        self.y = b #20
    #클래스 함수
    def plus(self):
        p = self.x + self.y #변수 연산
        return p
    def minus(self):
        m = self.x - self.y
        return m
# (4) 객체 생성
obj = calc_class(10,20)

# (5) 멤버 호출
print('plus =',obj.plus())
print('minus =',obj.minus())