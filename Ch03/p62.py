# 중첩 조건문 예

score = int(input('점수입력:'))
grade = ''
if score >= 85 and score <= 100:
    grade = '우수'
elif score >=70:
    grade = '보통'
else:
    grade = '저조'

print('당신의 점수는 %d 점이고, 등급은 %s 입니다.' % (score,grade))