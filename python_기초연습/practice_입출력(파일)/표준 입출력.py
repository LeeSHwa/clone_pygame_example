# import sys

# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)


# print("Python", "Java", sep = " vs ", end="?") 
# print("무엇이 더 재밌을까요?")

# # 시험 성적
# scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
# for subject, score in scores.items(): 
#     print(subject.ljust(8), str(score).rjust(4), sep = ":") # ljust : 왼쪽으로 정렬을 하는데 int의 공간만큼 확보하고 정렬

# # 은행 대기순번표
# for num in range(1, 21):
#     print( "대기번호 : " +str(num).zfill(3) ) # int 크기만큼의 공간을 확보하고, 값이 없는 공간은 zero fill

answer = input("아무 값이나 입력하세요 : ") # 사용자 입력은 무조건 문자열로 인식함
print("입력하신 값은 " + answer + "입니다.")