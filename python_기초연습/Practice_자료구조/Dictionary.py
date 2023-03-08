# cabinet = {3:"유재석", 100:"김태호"} # 키와 값으로 이루어져있는 Dictionary
# print(cabinet[3]) # 키는 대괄호 안에

# print(cabinet[100])

# print(cabinet.get(3))

# # print(cabinet[5]) 직접 가져오면 오류출력 후 종료

# print(cabinet.get(5,"사용 가능"))

# print(cabinet.get(5)) # get을 통해 가져오면 None 을 출력

# print(cabinet)

# print("hi")


cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

print(cabinet)
cabinet["A-3"] = "김종국" # 키에다가 값을 대입 가능
cabinet["C-20"] = "조세호" # 새로운 키에 새로운 값을 추가 가능
print(cabinet)

del cabinet["A-3"]
print(cabinet)

print(cabinet.keys())

print(cabinet.values())

#key, valude 쌍으로 출력
print(cabinet.items())

cabinet.clear()
print(cabinet)

