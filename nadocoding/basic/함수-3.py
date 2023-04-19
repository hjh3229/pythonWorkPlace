# 지역변수 - 함수 내에서만 사용 가능
# 전역변수 - 프로그램 내에서 사용 가능

'''
gun = 10

def checkpoint(soldier):
    gun = gun-soldier
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2)
print("남은 총 : {0}".format(gun))

오류 - def 이후 gun이라는 변수는 정의가 안되어 있으므로 -> 함수 내 변수 대입
'''

gun = 10

def checkpoint(soldier):
    gun = 20     # 지역변수
    gun = gun-soldier
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 전체 총 : 10
checkpoint(2)                     # [함수 내] 남은 총 : 18   # 함수 내에서는 지역변수 우선
print("남은 총 : {0}".format(gun)) # 남은 총 : 10   # 함수 내에서 따로 계산되었으므로 함수 밖 변수는 그대로

gun = 10

def checkpoint(soldier):
    global gun   # 전역변수 # 프로그램에 있는 gun이라는 변수를 이 함수 내에서도 이용
    gun = gun-soldier
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun)) # 전체 총 : 10
checkpoint(2)                     # [함수 내] 남은 총 : 8
print("남은 총 : {0}".format(gun)) # 남은 총 : 8

'''
전역변수를 많이 쓰면 일반적으로 변수 이름을 관리해야하므로 코드가 복잡해져 추천하지 않음. 
따라서 함수의 전달값과 반환값 이용을 추천.
'''

gun = 10

def checkpoint_ret(gun, soldier):
    gun = gun-soldier
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # gun이라는 변수를 밖으로 전달 가능

print("전체 총 : {0}".format(gun)) # 전체 총 : 10
gun = checkpoint_ret(gun,2)       # [함수 내] 남은 총 : 8       # 반환되는 값을 전달받음 
print("남은 총 : {0}".format(gun)) # 남은 총 : 8