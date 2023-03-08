class Unit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit): # 클래스의 이름 뒤, 괄호 속에 부모 클래스를 넣어 상속해줌 
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) #Unit 클래스를 상속받은 후
        self.damage = damage
        
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 : {self.damage}") 

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.")
        self.hp -= damage
        if self.hp > 0: print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")
        else: print(f"{self.name} : 파괴되었습니다.")


firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

marin1 = AttackUnit("마린", 30, 9)
marin1.damaged(16)
marin1.damaged(16)

class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도{self.flying_speed}")

class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

dropship = FlyableAttackUnit("드랍쉽", 100, 0, 5)
dropship.fly(dropship.name, "5시")