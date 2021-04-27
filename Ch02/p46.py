# format과 양식문자 예

# %d 10진수 , %o 8진수 , %x 16진수, %f 실수(%f전체자리수.소수점 어디까지 표시 반올림) ,
# %s 문자열, %c 단일 문자열

#(4) format()함수 인수 : format(value,"format")
print("원주율=", format(3.14159, "8.3f"))
print("금액=", format(10000, "10d"))
print("금액=", format(125000, "3,d"))

#(5) 양식문자 인수 : print("%양식문자" % (값))
name = "홍길동"
age = 35
price = 125.451
print("이름:%s,나이:%d,data=%.2f" % (name,age,price))