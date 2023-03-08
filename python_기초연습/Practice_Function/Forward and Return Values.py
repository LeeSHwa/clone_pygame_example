def deposit(balance, money):
    print(f"입금이 완료되었습니다. 잔액은 {balance + money} 원 입니다.")
    return balance + money

balance = 0
balance = deposit(balance, 1000)
print(balance)

def withdraw(balance, money):
    if balance >= money:
        print(f"출금이 완료되었습니다. 잔액은 {balance - money} 원 입니다.")
        return balance - money
    else: 
        print("잔액이 부족합니다.")
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 900)
print(balance)
    
def withdraw_night(balance, money): #저녁에는 수수료 
    commission = 100 # 수수료 금액
    return commission, balance - money - commission # 튜플 형식으로 리턴


balance = 0
balance = deposit(balance, 1000)

commission, balance = withdraw_night(balance, 500) # 튜플 형식으로 값을 반환받음
print(f"수수료 {commission} 원이며, 잔액은 {balance} 원입니다.")