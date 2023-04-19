# # 마린
# name = "마린"  # 이름
# hp = 40        # 체력 
# damage = 5     # 공격력

# print("{} 유닛이 생성되었습니다.".format(name))    # 마린 유닛이 생성되었습니다.
# print("체력 {0}, 공격력 {1}\n".format(hp,damage)) # 체력 40, 공격력 5

# # 탱크
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))          # 탱크 유닛이 생성되었습니다.
# print("체력 {0}, 공격력 {1}\n".format(tank_hp,tank_damage))  # 체력 150, 공격력 35

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))
    

# attack(name, "1시", damage)             # 마린 : 1시 방향으로 적군을 공격합니다. [공격력 5]
# attack(tank_name, "1시", tank_damage)   # 탱크 : 1시 방향으로 적군을 공격합니다. [공격력 35]

'''
위와 같은 방법을 사용할 시 새로운 마린이나 탱크, 아예 다른 이름의 유닛을 만들 때마다 
다른 이름, 체력등을 만들어줘야 함. 이는 너무 번거롭고, 비효율적이므로 아래와 같은 방법(클래스)을 사용함.
'''

# class = 틀
class Unit:         # Unit이라는 클래스를 만듦
    def __init__(self, name, hp, damage):   # self, name, hp, damage 입력
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린", 40, 5) # 마린 유닛이 생성 되었습니다.
                              # 체력 40, 공격력 5
marine2 = Unit("마린", 40, 5) # 마린 유닛이 생성 되었습니다.
                              # 체력 40, 공격력 5
tank = Unit("탱크", 150, 35)  # 탱크 유닛이 생성 되었습니다.
                              # 체력 150, 공격력 35

# __init__ = 생성자   marine, tank = 객체 = class로 부터 만들어짐 = class의 'instance'라 불림.
# 객체가 생성될 때 기본적으로 __init__함수에 정의된 개수와 동일하게 값을 지정해줘야 함.(self 제외) 
# .name, .hp, .damage = 멤버 변수 = 클래스 내에서 정의된 변수
wraith1 = Unit("레이스", 80, 5) # 레이스 유닛이 생성 되었습니다. ~~~
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage)) # 유닛 이름 : 레이스, 공격력 : 5
# . 을 통해 함수 내 멤버 변수에 접근 가능

wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True  # .clocking 이라는 새로운 변수를 외부에서 만듦.

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name)) # 빼앗은 레이스는 현재 클로킹 상태입니다.

if wraith1.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))
# Traceback (most recent call last):
#   File "c:\Users\한지훈\OneDrive\바탕 화면\pythonworkspace\개념\클래스.py", line 57, in <module>
#     if wraith1.clocking == True:
# AttributeError: 'Unit' object has no attribute 'clocking'
'''클래스 외부에서 원하는 변수를 확장 가능하나 이는 확장을 객체에서만 적용되고 다른 객체에서는 오류 발생'''