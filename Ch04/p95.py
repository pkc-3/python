#튜플 관련 함수 예

# (1) 튜플 자료형 변환
lst = list(range(1,6))
t3 = tuple(lst)
print(t3)

# (2) 튜플 관련 함수
print(len(t3),type(t3))
print(t3.count(3)) #3이 몇개인지 나타냄
print(t3.index(4)) #4가 있는 위치 나타냄