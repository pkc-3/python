# 지방(fat),탄수화물(carbohydrate),단백질(protein) 칼로리의 합계를 프로그램을 작성하시오
#
# <처리조건>
# <조건1> 지방,탄수화물,단백질의 그램을 키보드로 입력 받는다.
# <조건2> 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4
#
# <출력 화면 예시>
#
# 지방의 그램을 입력하세요 : 25
# 탄수화물의 그램을 입력하세요 : 520
# 단백질의 그램을 입력하세요 : 45
# 총 칼로리:2,485 cal

# fa = (int(input("지방의 그램을 입력하세요 :")))
# ca = (int(input("탄수화물의 그램을 입력하세요 :")))
# pr = (int(input("단백질의 그램을 입력하세요 :")))
#
# result = fa * 9 + ca * 4 + pr * 4
#
# # print("총 칼로리 :", result,"cal")
#
print("총 칼로리 :", format(result,'3,d'),'cal')# 완벽답

# print("금액 =",format(100000000,"3,d")) # 3번째 자리 마다 , 찍음
# print("금액 =",format(1561.56512,".2f")) # 소수점 둘째짜리까지 표시 세번째 에서 반올림
# print("금액 =",format(156156512,"100d")) # 100자리까지 표시함(젤 오른쪽에 숫자있음)
