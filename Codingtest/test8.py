data = list(map(int, input().split()))

# if(data[0] != 1):
#     result = 1
#     for i in range(len(data)):
#         if (data[i] == 0):
#             continue
#         if (data[i] == 1):
#             result = (result) + data[i]
#         else:
#             result = (result) * data[i]
# else:
#     result = 0
#     for i in range(len(data)):
#         if (data[i] == 0):
#             continue
#         if (data[i] == 1):
#             result = (result) + data[i]
#         else:
#             result = (result) * data[i]
#
# print(result)
# ===============================================================================================
data = input()

result = int(data[0])  # 첫 번째 문자를 숫자로 변환해서 대입

for i in range(1, len(data)):

    num = int(data[i])

    # num 또는 result가 0 혹은 1인 경우, 곱셈 연산 대신 덧셈 연산을 수행
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)