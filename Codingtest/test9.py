# data = list(map(int, input()))
# cnt = 0
#
# for i in range(len(data)):
#
#     if i+1 == len(data):
#         break
#     if data[i] != data[i+1]:
#         cnt += 1
#
#
#
# print(int(cnt/2))
#
#===============================================
data = input()

count0 = 0  # 전부 0로 바꾸는 경우
count1 = 0  # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:

        if data[i + 1] == '1':
            # 다음 수에서 1로 바꾸는 경우
            count0 += 1
        else:
            # 다음 수에서 0로 바꾸는 경우
            count1 += 1

# 두 경우의 수 중 낮은 수 출력
print(min(count0, count1))
