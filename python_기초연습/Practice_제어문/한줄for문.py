# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] # i에다가 100을 더한 값을 넣을텐데, student라는 리스트에 있는 i를 불러오면서 거기다가 집어 넣어라
print(students)

# 학생 이름을 길이로 변환
students = ["Iron man", "Thor", "I am groot"]
students = [len(i) for i in students]

print(students)

students = ["small man", "yes man", "no man"]
students = [i.upper() for i in students]
print(students)
