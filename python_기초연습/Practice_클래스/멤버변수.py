class Unit:
    def __init__(self, name, hp, damage):
        self.name = name                 
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

writh1 = Unit("레이스", 80, 5)
print(f"유닛 이름 : {writh1.name}, 공격력 : {writh1.damage}") # 객체 뒤에 .과 멤버변수를 붙이면 외부에서 불러올 수 있음

writh2 = Unit("레이스", 80, 5)
writh2.clocking = True # 파이썬은 외부에서 객체에 변수를 만들어 추가할 수 있다.

if writh2.clocking == True:
    print(f"{writh2.name} 는 현재 클로킹 상태입니다.")