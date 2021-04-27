#외부상수 출력 예


name = "홍길동"
age = 35
price = 125.451
#(6) 외부 상수 인수
print("이름:{},나이:[],data={}".format(name,age,price))
print("이름:{1},나이:[0],data={2}".format(name,age,price))

#(7) format 축약형(SQL문 작성)
uid = input("id input:")
query = f"select * from member where uid={uid}"
print(query)