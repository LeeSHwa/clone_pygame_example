try:
    print("나누기 전용 게산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(float(nums[0] / nums[1]))

    print(f"{nums[0]} / {nums[1]} = {nums[2]}")
    
except Exception as arr:
    print(arr)
