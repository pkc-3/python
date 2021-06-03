
h=int(input("몇시까지 할건지 입력하세요 : "))

count = 0

for i in range(h+1):
    for j in range(60):
        for k in range(60):

            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)















#
# cnt=0;
#
# a = []
# b = []
# c = []
# for i in range(0,N+1):
#     a.append(i)
#
#     for j in range(0,60):
#         b.append(j)
#
#         for k in range(0,60):
#             c.append(k)
# print(len(a))
# print(len(b))
# print(len(c))
#
#
# list = a + b + c
# print(list)
# for x in list:
#     y = str(list[x])
#
#     if '3' in y:
#         cnt += 1
#     else:
#         continue
#
# print(cnt)



