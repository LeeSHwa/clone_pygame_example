class Unit:
    def __init__(self, name, hp, damage): # __init__은 Python에서 생성자 역할임
        self.name = name                  # 또한 self를 제외한 3개의 인자 중 하나라도 빠지면 오류가 남
        self.hp = hp
        self.damage = damage
        print(f"{name} 유닛이 생성 되었습니다.")
        print(f"체력 {hp}, 공격력 {damage}")

marine1 = Unit("마린", 35, 15) # Unit클래스의 인스턴스
marine2 = Unit("마린", 40, 15)

