python = "Python is Amazing"

print(python.lower())
print(python.upper())

print(python[0].isupper())

print(len(python))

print(python.replace("Python", "Java"))

index = python.index("n")
print(index)

index = python.index("n", index + 1) # index 
print(index)

print(python.find("Java")) # find 함수는 원하는 값을 찾지 못하여도 오류를 발생시키지 않고 -1값을 반환한다.
# print(python.index("Java")) # index 함수는 바로 오류발생시킴 ㅋㅋ
print("hi")

print(python.count("n")) # 총 몇번 등장하는지 