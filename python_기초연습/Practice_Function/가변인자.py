# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print(f"이름 : {name}\t나이 : {age}\t", end=" " ) # end를 정의해서 큰 따음표 띄어쓰기 큰따음표를 하면 줄바꿈 X
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language): # 인자변수 앞에 *를 붙인다면 가변인수가 됨!! 
    print(f"이름 : {name}\t나이 : {age}\t", end=" " )
    for lang in language:
        print(lang, end = " ") # print 문 뒤에 , 이후 end 를 " "로 정의해주면 출력문에서 줄바꿈이 없어짐
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Korlin", "Swift")
