class BigNumberError(Exception): # 사용자 설정 오류
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg



try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))

    if (num1 >= 10 or num2 >= 10):
        raise BigNumberError(f"입력값 : {num1} / {num2}")
    print(f"{num1} / {num2} = {num1 / num2}")

except ValueError:
    print("10 이하의 값을 입력하세요.")
except BigNumberError as arr:
    print("에러가 발생했습니다. 10 이하의 숫자만 적어주세요.")
    print(arr)
finally:
    print("계산기를 이용해주셔서 감사합니다.") # finally는 무슨 일이 일어나든 무조건 실행됨