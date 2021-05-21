# 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.
# <각 단계별 출력 결과 예시>
# 단계 1 : [10,1,5,2,10,1,5,2]
# 단계 2 : [10,1,5,2,10,10,1,5,2,20]
# 단계 3 : [1,2,1,2]


lst =[10,1,5,2]

result1 = lst*2
print("result1 : ",result1)
result3 = result1



a = lst[0]*2
result1.append(a)
result2 = result1
print("result2 : ",result2)

result3.remove(20)


d = int(len(result3)/2+1)

result4 =[]
for i in range(1,d):
    a = result3[2*i-1]
    result4.append(a)

print("result3 : ",result4)
