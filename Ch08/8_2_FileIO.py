"""
날짜:2021/05/03
이름:고현석
내용:파이썬 파일 입출력 실습 교재 p217
"""

# 파일 읽기(Input)

file1 = open('C:/Users/bigdata/Desktop/sample.txt','r') # r 읽기모드
line = file1.readline()

print('line:',line)
file1.close() #열었으니까 꼭 닫아줘야함

# 여러줄 파일 읽기
file2 = open('C:/Users/bigdata/Desktop/sample.txt','r')

while True:
    line = file2.read() #read 반복

    if not line: #line에 내용이 없다면
        break
    print('line : \n'+str(line))

file2.close()

# 파일 쓰기(file output)
file3 = open('C:/Users/bigdata/Desktop/test.txt','w') # w 쓰기모드
file3.write('안녕하세요\n')
file3.write('반갑습니다\n')
file3.write('감사합니다\n')
file3.close()
# 예제 구구단 파일 만들기
file4 = open('C:/Users/bigdata/Desktop/gugudan.txt','w')

# for i in range(2,10):
#     file4.write('\n'+str(i)+'단입니다.\n')
#     for j in range(1,10):
#         file4.write(str(i)+' * '+str(j)+' = '+str(i*j)+'\n')

for x in range(2,10):
    file4.write('%d단\n' % x)
    for y in range(1,10):
        z= x*y
        file4.write('{} x {} = {}\n'.format(x,y,z)) #format이나 %d 활용하자!
file4.close()