n,m = map(int,input().split())


nums = []
for i in range(n):
    data = list(map(int,input().split()))

    #data에서 가장 작은 수 구함
    data.sort()
    num = data[0]
    nums.append(num)

result = max(nums) #내가 한 거

# nums.sort()
# result = nums[-1] 쌤이 하신거

print(result)