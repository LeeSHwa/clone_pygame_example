# score_file = open("score.txt", "w", encoding = "utf8") #write
# print("수학 : 100",file = score_file)
# print("영어 : 80",file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding = "utf8") # append
# score_file.write("국어 : 50")
# score_file.write("\n코딩 : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# print(score_file.readline()) # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline())
# print(score_file.readline())
# print(score_file.readline())
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line)
# score_file.close()

score_file = open("score.txt", "r", encoding = "utf8")
lines = score_file.readlines()
for line in lines:
    print(line, end = "")
score_file.close()