#position 변수를 대상을 중복되지 않는 직위와 직위별 빈도수를 출력하시오

# <출력 결과 예시>
# 중복되지 않는 직위:['사장','과장','대리','부장']
# 각 직위별 빈도수:{'과장':2,'부장':1,'대리':2,'사장':1}

position = ['과장','부장','대리','사장','대리','과장']



# po1 = list(set(position))
# print("중복되지 않는 직위:",po1)
#
# a = position.count('과장')
# b = position.count('부장')
# c = position.count('대리')
# d = position.count('사장')
# dic = {'과장':+a,'부장':+b,'대리':+c,'사장':+d,}
#
# print("각 직위별 빈도수:",dic)

uni_position = list(set(position))
print('중복되지 않는 직위 :', uni_position)

position_cnt = {}
for p in position:
    position_cnt[p] = position_cnt.get(p,0) +1
    print(position_cnt[p]) # 키 값은 변경 불가 5번째 턴에서 키 값 찾아서 +1해줌

print('각 직위별 빈도수 : ', position_cnt)