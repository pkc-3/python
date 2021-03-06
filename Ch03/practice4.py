# 중첩 반복문을 이용한 '단어 카운트(word count)'
#
# 다음과 같은 multiline의 문자열 객체를 이용하여 단어를 추출하고 단어의 개수를 출력하시오.
#
# multiline=""" 안녕하세요. 파이썬 세계로 오신걸
# 환영합니다.
# 파이썬은 비단뱀 처럼 매력적인 언어입니다."""

# <출력결과>
# 안녕하세요.
# 파이썬
# 세계로
# 오신걸
# 환영합니다.
# 파이썬은
# 비단뱀
# 처럼
# 매력적인
# 언어입니다.
# 단어 개수 : 10

multiline="""안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
cnt=0
doc =[]
word =[]
for i in multiline.split('\n'): # 줄 기준으로 3개가 되게 쪼갬
    for w in i.split(' '): # 공백 기준으로 단어별로 쪼갬.
        doc.append(w)
        print(w)
        cnt += 1 #쪼갤때마다 카운터 1씩 올림(단어 개수 몇개인지 알기 위해)

print("단어개수:",cnt)