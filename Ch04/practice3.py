#list 내포를 이용하여 문자열 처리하기

#A형============================================================================
#message 변수를 대상으로 'spam' 원소는 1 'ham' 원소는 0으로 dummy 변수를 생성하시오.
# message = ['spam','ham','spam','ham','spam']


# for i in range(0,5): #0~4
#     message[i] = 1
# message[1] = 0
# message[3] = 0
# print(message)


# for i in message:
#     if(i == "spam"):
#         a = message.index(i)
#         message[a] = 1
#
#     if (i == "ham"):
#         a = message.index(i)
#         message[a] = 0
#
# print(message)

#B형============================================================================
#message 변수를 대상으로 'spam' 원소만 추출하여 spam_list에 추가하시오
# message = ['spam','ham','spam','ham','spam']
# spam_list = []
# for i in message:
#     if(i == "spam"):
#         spam_list.append(i)
#
#     if (i == "ham"):
#         continue
#
# print(spam_list)