# 문자열 처리 함수 예
# (1) 특정 글자 수 반환
oneLine = "this is one line string"
print('t 글자 수 :', oneLine.count('t'))
# (2) 접두어 문자 비교 판단
print(oneLine.startwith('this'))
print(oneLine.startwith('that'))
# (3) 문자열 교체
print(oneLine.replace('this','that'))
# (4) 문자열 분리(split) : 문단 -> 문장
# (5) 문자열 분리(split)2 : 문장 -> 단어
# (6) 문자열 결합(join) : 단어 -> 문장