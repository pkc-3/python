#while 반복문 예

#(1) 카운터와 누적변수
cnt = tot = 0
while cnt <5:
    cnt += 1
    tot += cnt
    print(cnt,tot)


#1~100 사이 3의 배수 합과 원소 추출하기
cnt = tot = 0
dataset = []

while cnt<100:
    cnt+=1
    if cnt % 7 == 0:
        tot += cnt
        dataset.append(cnt)

print('1~100사이 7의 배수 합은 %d' % (tot))
print(dataset)