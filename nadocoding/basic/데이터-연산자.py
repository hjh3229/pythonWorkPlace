# 곱하기 = *    나눗셈 = /    제곱 = **     나머지 = %      몫 = //       똑같다 = ==      같지않다 = !=
print(3**4) #81
print(25%6) #1
print(14//4) #3
print(3+4==7) #True
print(10-3!=5) #True

# 동시만족 = and, &    하나라도 만족 = or, |
print((3>0) and (7-2<9) & (8-3>2)) # True
print((5-3<=2) or (7+2>9) | (3**2<12)) # True

# 변수=변수+@   ==   변수+=@    (+외에 다른 연산기호 (*, /, //, ...)전부 가능)
number=12
print(number) # 12
number=number+2
print(number) # 14
number+=2
print(number) # 16
number*=2
print(number) # 32
number-=2
print(number) # 30
number/=2
print(number) # 15.0
number//=2
print(number) # 7.0 # 위 /의 영향으로 소수점 붙음
number%=3
print(number) # 1.0 # ''

# 절댓값 = abs()    @제곱 = pow(x, @)    최댓값 = max()     최솟값 = min()     반올림 = round() 
print(abs(-7.8)) # 7.8
print(pow(3, 4)) # 81
print(max(8, 2, 7, 15, 11)) # 15
print(min(8, 2, 7, 15, 11)) # 2
print(round(2.789)) # 3

# from math import * = 아래 수식 쓰기 전 불러오기
# 내림 = floor()    올림 = ceil()    제곱근 = sprt()    
# print(floor(2.789)) # 오류
from math import *
print(floor(2.789)) # 2
print(ceil(2.789)) # 3
print(sqrt(49)) # 7.0

# from random import * = 아래 랜덤함수 쓰기 전 불러오기
# random() = 0 이상 1 미만 '실수', randrange(x, y) = x 이상 y미만 '정수'
from random import *
print(random()) # 0 이상 1 미만 실수     ex) 0.8278695884663135
print(random()*10) # 0 이상 10 미만 실수     ex) 4.226269879100992
print(int(random()*10)) # 0 이상 10 미만 정수 ex) 8
print(int(random()*10)+1) # 1 이상 10 이하 정수    ex) 10
print(randrange(1, 47)) # 1 이상 46 이하 정수    ex) 22
