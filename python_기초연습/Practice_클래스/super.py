class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable): # 다중상속의 경우 super을 사용할 경우, 앞의 부모 클래스만 상속받은
    def __init__(self):
        super().__init__()

dropship = FlyableUnit()


class FlyableUnit1(Flyable, Unit): # 그렇기에 다중상속의 경우는 하나하나 풀어써주는게 좋음
    def __init__(self):
        Unit.__init__(self)
        Flyable.__init__(self)

dropship2 = FlyableUnit1()