"""
날짜:2021/05/20
이름:고현석
내용:파이썬 데이터베이스 SQL 실습하기
"""
import pymysql

# 데이터베이스 접속
conn = pymysql.connect(host='192.168.10.114',user='pkc716054',password='1234',db='pkc716054',charset='utf8')

# SQL 실행 객체 생성
cur = conn.cursor()
# SQL 실행
sql = "INSERT INTO `USER1` VALUES('p102','김춘추','010-1234-1002',23);"
cur.execute(sql)
conn.commit()
# 데이터베이스 종료
conn.close()

print('Insert 완료')