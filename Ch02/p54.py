#이스케이프 문자 기능 차단 예
#\n 줄바꿈처리 \t 탭키 처리 \r 캐리지 리턴처리(다음줄 첫칸으로 이동)
#\f 폼 피드 처리 (한 페이지 넘김) \b 백스페이스 처리 \\ 문자 "\" 처리
#\' 문자 ' 처리 \" 문자 " 처리 \000 널 문자 처리

# (1) escape 문자 적용
print('escape 문자 차단')
print('\n출력 이스케이프 문자')

# (2) escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')

# (3) 경로 표현
print('path=','C:\Python\test')
print('path=','C:\\Python\\test')
print('path=',r'C:\\Python\\test')