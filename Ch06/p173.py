# builtins 모듈 내장클래스 예

# (1) 리스트 열거형 객체 이용
lst = [1,3,5]
for i, c in enumerate(lst) : #enumerate 란 열거형 자료를 순회하여 색인과 값을 반환하는 객체 생성 역할
    print('색인 : ', i, end=', ')
    print('내용 : ',c)

# (2) 튜플 열거형 객체 이용
dit = {'name' : '홍길동','job' : '회사원','addr' : '서울시'}
for i, k in enumerate(dit):
    print('순서 : ', i, end=', ')
    print('키 : ', k, end=', ')
    print('값 : ', dit[k])