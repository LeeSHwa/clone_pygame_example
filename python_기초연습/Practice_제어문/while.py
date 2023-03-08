# customer = "토르"
# index = 1
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer,index))
#     index += 1
#     if index == 5:
#         print("커피는 폐기처분되었습니다.")

customer = "토르"
person = "Unknown"

while person != customer :
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")    
    if person == "토르":
        print("맛있게 드세요!")