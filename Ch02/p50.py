#슬라이싱 예

# (1) 왼쪽기준
oneLine = "this is one line string"
print(oneLine)
print("문자열 길이 :", len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])
print(oneLine[::2])#2의 배수만 index

# (2) 오른쪽기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

# (3) 부분 문자열 생성
subString = oneLine[-11:]
print(subString)