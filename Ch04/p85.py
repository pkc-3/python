#단일 리스트 객체 예

#(1) 단일 list 예
lst = [1,2,3,4,5]
print(lst)
print(type(lst))

for i in lst:
    print(lst[:i])
print('=================')
#(2) 단일 리스트 색인 예
x = list(range(1,11))
print(x)
print(x[:5])
print(x[-5:])
print('index 2씩 증가')
print(x[::2])
print(x[1::2])