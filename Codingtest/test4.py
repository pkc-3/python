n = int(input())

x, y = 1,1
plans = input().split()

print(type(plans))
print(plans[0])

for i in plans:

    if (i == "L"):
        if y == 1:
            continue
        else:
            y -= 1

    if (i == "R"):
        if y == n:
            continue
        else:
            y += 1

    if (i == "U"):
        if x == 1:
            continue
        else:
            x -= 1

    if (i == "D"):
        if x == n:
            continue
        else:
            x += 1


print(x,y)