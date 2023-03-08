absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range(1,11):
    if student in absent:
        print(f"{student}는 결석이란다")
        continue
    elif student in no_book:
        print(f"오늘 수업 여기까지. {student}는 교무실로 따라와")
        break
    print(f"{student}, 책을 읽어보렴")
    