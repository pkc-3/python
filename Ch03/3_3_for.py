"""
날짜:2021/04/28
이름:고현석
내용:파이썬 반복문 for 실습 교재 p78
"""

#for
for i in range(5):
    print('i :', i)

for j in range(10,20):

    print('j :', j)

for k in range(10,0,-1):
    print('k :', k)

#1부터 10까지 합
sum1 = 0
for k in range(11):
    sum1 += k

print('1부터 10까지 합:', sum1)

#1부터 10까지 짝수합
sum2 = 0

for k in range(11):
    if k % 2 == 0:
        sum2 += k

print('1부터 10까지 짝수합', sum2)

#중첩 for

for a in range(3):
    print('a:',a)
    for b in range(4):
        print('b:', b)

#구구단
for a in range(2,10):
    print(a,'단')
    for b in range(1,10):
        print(a,'x',b,':', a*b)

for x in range(2,10):
    print(x,'단')
    for y in range(1,10):
        z = x * y
        print('%d x %d = %d' % (x,y,z))
#별 삼각형
for a in range(10):

    for b in range(a):
        print('☆', end='')

    print()

for i in range(10):
    print('★'*i)
print()


for i in range(1,11):
    print("　"*(10-i)+"★"*(i*2-1))





#list를 이용한 for - 1
nums = [1,2,3,4,5]
for num in nums:
    print('num :', num)

for person in ['김유신','김춘추','장보고']:
    print('person :', person)
scores = [62,86,72,74,96]
total = 0
for score in scores:
    total += score
print('score의 총합:',total)
#list index, value 출력(enumerate 쓰면 인덱스값과 벨류값 나타냄)
for index, value in enumerate(scores):
    print('{}번 {}점'.format(index,value))




#list comprehension
list1 = [1,2,3,4,5]

list2 = [num * 2 for num in list1]
list3 = [num * 3 for num in list1 if num % 2 == 1] # 홀수만 * 3 해준다.
print('list2:',list2)
print('list3:',list3)