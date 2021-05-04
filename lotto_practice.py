import random
# 연습 로또 번호
def Lotto(n):

    result = []
    numbers = []
    for i in range(n):
        r = random.sample(range(1,46),6)
        tot = sum(r)
        avg = int(tot/6)
        result.append(avg)
        for j in range(6):
            numbers.append(r[j])

    count1={}
    for i in result:
        try: count1[i] += 1
        except: count1[i]=1
    print('많이 나오는 평균값\n',sorted(count1.items()))

    count2 = {}
    for i in numbers:
        try:
            count2[i] += 1
        except:
            count2[i] = 1
    print('번호마다 나오는 개수\n',sorted(count2.items()))

    return result

Lotto(100)


