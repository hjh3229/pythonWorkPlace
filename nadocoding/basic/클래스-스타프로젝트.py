from random import *

class Unit:         
    def __init__(self, name, hp, speed):   
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))
    
    def move(self, location):
        print("{0} : {1}의 방향으로 움직입니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit):              
    def __init__(self, name, hp, speed, damage):   
        Unit.__init__(self, name, hp, speed)     
        self.damage = damage              
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) 

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 1, 5)

    def stimpack(self):
        if self.hp >10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (hp 10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

class Tank(AttackUnit):
    seize_developed = False  # 시즈모드 개발 여부

    def __init__(self):
        AttackUnit.__init__(self, "탱크", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False: 
            return                          # 시즈모드가 개발되지 않았으면 시행X

        if self.seize_mode == False:
            print("{0} : 시즈모드로 전환합니다.".format(self.name))
            self.damage *= 2
            self.seize_mode = True          # 시즈모드가 아닐시 시즈모드로 전환하고 공격력 두배

        else:
            print("{0} : 시즈모드를 해제합니다.".format(self.name))
            self.damage /= 2
            self.seize_mode = False         # 시즈모드일 시 시즈모드 해제하고 공격력 원상복구 

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}의 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable): 
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) 
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):           # 공중유닛도 move 함수를 통해 이동되도록 메소드 오버라이딩 사용
        self.fly(self.name, location)

class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
            self.clocked = False

        else:
            print("{0} : 클로킹 모드로 전환합니다.".format(self.name))
            self.clocked = True

def game_start():
    print("새로운 게임을 시작합니다")

def game_over():
    print("Player : gg")
    print("[Player] 님이 게임에서 퇴장하였습니다.")

# 게임 진행 시뮬

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("1시")

Tank.seize_developed = True
print("[알림] 탱크 시즈모드가 개발되었습니다.")

for unit in attack_units:
    if isinstance(unit, Marine):   # 개별 유닛의 종류를 확인하고 명령수행
        unit.stimpack()
    
    if isinstance(unit, Tank):
        unit.set_seize_mode()

    if isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")

for unit in attack_units:
    unit.damaged(randint(5,21)) # 5~20 랜덤한 데미지를 입음

game_over()

'''
새로운 게임을 시작합니다
마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
마린 유닛이 생성되었습니다.
탱크 유닛이 생성되었습니다.
탱크 유닛이 생성되었습니다.
레이스 유닛이 생성되었습니다.
마린 : 1시의 방향으로 움직입니다. [속도 1]
마린 : 1시의 방향으로 움직입니다. [속도 1]
마린 : 1시의 방향으로 움직입니다. [속도 1]
탱크 : 1시의 방향으로 움직입니다. [속도 1]
탱크 : 1시의 방향으로 움직입니다. [속도 1]
레이스 : 1시의 방향으로 날아갑니다. [속도 5]
[알림] 탱크 시즈모드가 개발되었습니다.
마린 : 스팀팩을 사용합니다. (hp 10 감소)
마린 : 스팀팩을 사용합니다. (hp 10 감소)
마린 : 스팀팩을 사용합니다. (hp 10 감소)
탱크 : 시즈모드로 전환합니다.
탱크 : 시즈모드로 전환합니다.
레이스 : 클로킹 모드로 전환합니다.
마린 : 1시 방향으로 적군을 공격합니다. [공격력 : 5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력 : 5]
마린 : 1시 방향으로 적군을 공격합니다. [공격력 : 5]
탱크 : 1시 방향으로 적군을 공격합니다. [공격력 : 70]
탱크 : 1시 방향으로 적군을 공격합니다. [공격력 : 70]
레이스 : 1시 방향으로 적군을 공격합니다. [공격력 : 20]
마린 : 11 데미지를 입었습니다.
마린 : 현재 체력은 19입니다.
마린 : 17 데미지를 입었습니다.
마린 : 현재 체력은 13입니다.
마린 : 11 데미지를 입었습니다.
마린 : 현재 체력은 19입니다.
탱크 : 10 데미지를 입었습니다.
탱크 : 현재 체력은 140입니다.
탱크 : 14 데미지를 입었습니다.
탱크 : 현재 체력은 136입니다.
레이스 : 13 데미지를 입었습니다.
레이스 : 현재 체력은 67입니다.
Player : gg
[Player] 님이 게임에서 퇴장하였습니다.
'''