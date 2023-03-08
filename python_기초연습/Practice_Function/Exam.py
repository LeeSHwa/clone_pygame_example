# Quiz) 표준 체중을 구하는 프로그램을 작성하시오

# * 표준 체중 : 각 개인의 키에 적당한 체중

# (성별에 따른 공식)
#  남자 : 키(m) x 키(m) x 22
#  여자 : 키(m) x 키(m) x 21

# 조건 1 : 표준 체중은 별도의 함수 내에서 게산
#         * 함수명 : std_weight
#         * 전달값 : 키(height), 성별(gender)
# 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

def std_weight(height, gender):
    if gender == "남자":
        weight = height/100 * height/100 * 22
        return height, weight
    elif gender == "여자":
        weight = height/100 * height/100 * 21
        return height, weight
    else:
        print("오류오류")

gender = "여자"
height, weight = std_weight(197, gender)
temp = format(weight, ".2f")

print(f"키 {height}cm {gender}의 표준 체중은 {temp}kg 입니다.")

def std_weight_(height, gender):
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175
gender = "무생물"
weight = round(std_weight_(height / 100, gender), 2)
print(f"키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.")
