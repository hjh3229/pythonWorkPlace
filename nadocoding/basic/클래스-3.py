class Unit:         
    def __init__(self, name, hp, speed):   
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("{0} : {1}의 방향으로 움직입니다. [속도 {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit):              
    def __init__(self, name, hp, speed, damage):   
        Unit.__init__(self, name, hp, speed)     
        self.damage = damage              
        
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 : {2}]"\
            .format(self.name, location, self.damage)) 
    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

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
        self.fly(self.name, location)   # '날아갑니다'를 출력해야하므로 fly함수 이용

vulture = AttackUnit("벌쳐", 80, 10, 20)
vulture.move("11시")       # 벌쳐 : 11시의 방향으로 움직입니다. [속도 10]
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
battlecruiser.move("9시")  # 배틀크루저 : 9시의 방향으로 날아갑니다. [속도 3]

# pass = 아무것도 하지 않고 넘김(입력은 기억함) , pass 전 명령은 시행됨.
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        pass

supply_depot = BuildingUnit("서플라이 디폿", 500, "7시") #

# super = 뒤에 ()가 필요한 대신 self는 넣지 않는다는 차이점이 있다.
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #Unit.__init__(self, name, hp, 0)  # Unit에는 속도가 있으나 건물에는 없으므로 0(없음)입력
        super().__init__(name, hp, 0)      # 결과는 위와 동일. 단, 다중 상속때 문제 발생
        self.location = location

'''super 다중상속 = 맨 처음에 상속받는 클래스에 대해서만 __init__ 함수가 호출됨.'''
class dessert:
    def __init__(self):
        print("간식")

class cookie:
    def __init__(self):
        print("쿠키")

class dessertcookie(dessert, cookie):
    def __init__(self):
        super().__init__()

chocochip = dessertcookie() # 간식

class dessertcookie(cookie, dessert):
    def __init__(self):
        super().__init__()

chocochip = dessertcookie() # 쿠키

class dessertcookie(cookie, dessert):
    def __init__(self):
        dessert.__init__(self)
        cookie.__init__(self)

chocochip = dessertcookie()
# 간식
# 쿠키