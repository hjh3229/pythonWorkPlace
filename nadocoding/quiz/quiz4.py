'''
규칙 1 : 20명의 참가자 중 1등 한 명 2등 3명을 랜덤으로 뽑되, 중복되지는 말 것.
규칙 2 : 20명의 아이디는 각 1~20으로 설정
규칠 3 : random 모듈의 shuffle 과 sample 사용

출력 예시)
 -- 당첨자 발표 --
치킨 당첨자 : 1
커피 당첨자 : [2, 3, 4]
 -- 축하합니다 --
'''

# 제출 답안
from random import *
first = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(first)
first.pop()
print(" -- 당첨자 발표 --\n치킨 당첨자 : "+str(first.pop())+"\n커피 당첨자 : "+str(sample(first, 3))+"\n -- 축하합니다 --")


# 모범 답안
from random import *
users = range(1, 21)
users = list(users)
shuffle(users)
winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" -- 축하합니다 -- ")