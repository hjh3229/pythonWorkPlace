class Unit:         
    def __init__(self, name, hp, speed):   
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("{0} : {1}의 방향으로 움직입니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):                    # 부모클래스(Unit)에 이미 있는 내용을 자식클래스(Attack)에 상속
    def __init__(self, name, hp, speed, damage):   
        Unit.__init__(self, name, hp, speed)      # Unit.__init__를 통해 상속받을 값을 지정해줌.
        self.damage = damage               # damage는 Unit에 없으므로 추가
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) 
# name, damage는 self를 붙임으로서 class에서 받은 변수를 입력하는거고 lacation은 전달받은 값을 그대로 씀
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

firebat1 = AttackUnit("파이어뱃", 50, 16, 2)
firebat1.attack("5시")
firebat1.damaged(25)
firebat1.damaged(25)
# 파이어뱃 : 5시 방향으로 적군을 공격합니다. [공격력 : 16]
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 25입니다.
# 파이어뱃 : 25 데미지를 입었습니다.
# 파이어뱃 : 현재 체력은 0입니다.
# 파이어뱃 : 파괴되었습니다.

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1}의 방향으로 날아갑니다. [속도 {2}]"\
            .format(name, location, self.flying_speed))

class FlyableAttackUnit(AttackUnit, Flyable):   # 공격유닛과 공중유닛의 내용을 상속받음
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # AttackUnit에서 이름, 체력, 공격력 상속 (속도는 상속 X)
        Flyable.__init__(self, flying_speed)           # Flyable에서 비행속도 상속

valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
valkyrie.fly(valkyrie.name, "3시") # 발키리 : 3시의 방향으로 날아갑니다. [속도 5]

vulture = AttackUnit("벌쳐", 80, 10, 20)

battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시") # 벌쳐 : 11시의 방향으로 움직입니다. [속도 10]
battlecruiser.fly(battlecruiser.name, "9시") # 배틀크루저 : 9시의 방향으로 날아갑니다. [속도 3]

'''
이와 같이 지상유닛은 이동시 move, 공중유닛은 fly를 구분해서 사용해야 하는 번거로움이 있다. 
따라서 사용자가 유닛의 종류와 상관없이 move만 사용해도 출력이 구분되도록 해주는 
메소드 오버라이딩을 사용할 것이다.
'''
