"""
날짜:2021/05/03
이름:고현석
내용:파이썬 예외처리 실습 교재 p212

"""

# n,m,k를 공백으로 구분하여 입력받기
n,m,k = map(int,input().split())

# n개의 숫자를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

# 내림차순 정렬
data.sort(reverse=True)

# 첫번째 숫자
first = data[0]

# 두번째 숫자
second = data[1]

# result = 0
# repeat = k # k값을 보존해야함
# for i in range(m):
#
#     if repeat > 0:
#         result += first
#         repeat -= 1
#     else:
#         result += second
#         repeat = k
#
# print(result)

