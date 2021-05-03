"""
날짜:2021/05/03
이름:고현석
내용:파이썬 정규 표현식 실습 교재 p192

정규표현식(RegularExpression)
 - 특정한 규칙을 갖는 문자열을 처리하기 위한 문법
 - 일반적으로 특정 문자 검색, 매치 여부를 확인할 때 정규표현식을 사용
"""

import re#(regular expression)
from re import findall,match

str1 = '1234 abc홍길동 ABC_555_6 부산광역시'

# 숫자 검색

print(findall('1234',str1))
print(findall('[0-9]',str1)) #str1에서 숫자만 들고왔음 0에서 9까지 숫자를 찾아라
print(findall('[0-9]{3}',str1))#3개씩 붙여져 있는거만 찾기{개수}
print(findall('[0-9]{3,}',str1))#3개이상 붙여져 있는거만 찾기

#문자열 검색
print(findall('[가-힇]{3,}',str1)) #한글만 3글자 이상 찾기
print(findall('[a-z|A-Z]{3,}',str1)) #영어 소문자만 3글자 이상 찾기 | 넣어서 대문자도 검색함

str2 = 'test1abcABC 123mbc 45test'
print(findall('^test',str2)) # ^ <시작을 의미한다.
print(findall('st$',str2)) # $ <끝을 의미한다.

# 단어 검색
str3 = 'test^홍길동 abc 대한*민국 123$tbc'
print(findall('\\w{3,}',str3)) # 3자 이상의 단어를 검색함

# 응용
jumin = '123456-1891234'
result = match('[0-9]{6}-[1-2][0-9]{6}',jumin) # - 앞에 : 6자리 맞으면 true판단
                                                [1-2] : 남녀 성별 확인
                                                [0-9] : 6자리 숫자

if result:
    print("주민번호가 맞습니다.")
else:
    print("주민번호가 아닙니다.")