gun = 10

def checkpoint(soliders):
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soliders
    print(f"[함수 내] 남은 총 : {gun}") # 권장되지 않는 방법

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print(f"[함수 내] 남은 총 : {gun}")
    return gun

print(f"전체 총 : {gun}")

gun = checkpoint_ret(gun, 2)
print(f"남은 총 : {gun}")