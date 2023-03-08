# def profile(name, age, main_lang):
#     print(f"이름 : {name}, 나이 : {age}, 주 사용 언어 : {main_lang}") #만약 format를 사용하는데 줄을 넘어간다면 \를 사용 후 줄 넘김

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은 학교, 같은 학년, 같은 반, 같은 수업.

def profile(name, age = 17 , main_lang = "파이썬"):
    print(f"이름 : {name}, 나이 : {age}, 주 사용 언어 : {main_lang}") #만약 format를 사용하는데 줄을 넘어간다면 \를 사용 후 줄 넘김

profile("유재석")
profile("김태호", 25, "자바")
