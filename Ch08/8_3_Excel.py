"""
날짜:2021/05/03
이름:고현석
내용:파이썬 외부패키지 설치 교재 p239
pip install openpyxl 엑셀열기가능하게
"""

from openpyxl import Workbook

#엑셀파일 쓰기

workbook = Workbook()

# 활성화된 sheet 선택
sheet = workbook.active

# 데이터 입력
sheet['A1'] = '홍길동'
sheet.append([1,2,3])
sheet.append(['김유신','김춘추','장보고'])
sheet.cell(6,2,'사과') #6행 2열에 사과 단어 넣기

# 엑셀파일 저장/닫기
workbook.save('C:/Users/bigdata/Desktop/sample.xlsx')
workbook.close()

print('Excel 작업완료')