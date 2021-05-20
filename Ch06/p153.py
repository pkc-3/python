#클래스 구성요소 예
class Car:
    # (1) 멤버변수
    cc = 0 #엔진 cc
    door = 0 #문짝 개수
    carType = None #null
    
    # (2) 생성자
    def __init__(self,cc,door,carType):
        #멤버 변수 초기화
        self.cc = cc
        self.door = door
        self.carType = carType
        
    # (3) 메서드
    def display(self):
        print("자동차는 %d cc이고, 문짝은 %d개, 타입은 %s" %(self.cc, self.door,self.carType))

# (4) 객체 생성
car1 = Car(2000,4,"승용차")
car2 = Car(3000,5,"SUV")

# (5) 멤버 호출 : object.member()
car1.display() #car1 멤버 호출
car2.display() #car2 멤버 호출