# 항공사에서는 짐을 부칠때, 10kg 이상이면 수수료 10,000원을 내
# 야한다 만약 10kg 미만이면 수수료는 없다. 사용자의 짐의 무게를
# 키보드로 입력 받아서 사용자가 지불하여아 하는 금액
# 을 계산하는 프로그램을 작성하시오.


x = (int(input('짐의 무게는 얼마입니까?')))
if x > 10:
    print('수수료는 10,000원 입니다.')
else:
    print('수수료는 없습니다.')

