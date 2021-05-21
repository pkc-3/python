# 3개의 단어를 키보드로 입력 받아서 각 단어의 첫글자를 추출하여 단어의 약자를 출력하시오.
#
# <처리 조건>
# <조건1> 각 단어 변수(word1, word2, word3) 저장
# <조건2> 입력과 출력 구분선: 문자열 연산
# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
#
# <출력 화면 예시>
# 첫번째 단어 : Korea
# 두번째 단어 : Baseball
# 세번째 단어 : Orag
# ====================
# 약자 : KBO
#

word1 = input("첫번째 단어 :")
word2 = input("두번째 단어 :")
word3 = input("세번째 단어 :")

re = word1[0] + word2[0] + word3[0]
re = re.upper() # 전부 대문자로 <=>lower
print("=================")
print("약자 :", re)