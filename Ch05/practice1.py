# 문제1
# 다음 height 변수에 별(star)의 층수를 입력하면 각 층 마다 별의 개수가 한 개씩 증가하여 출력되고, 마지막 줄에 별의 개수가 출력되도록 함수의 빈칸을 채우시오
# <출력 결과 예시>
# height : 3 <- 키보드 입력
# *
# **
# ***
#star개수 : 6

#함수 정의
height = int(input('height : '))

def StarCount(height):

    h_cnt = s_cnt = 0
    while h_cnt < height:
        h_cnt += 1
        print('*'*h_cnt)
        s_cnt += h_cnt
    return s_cnt

print('star 개수 : %d'%StarCount(height))