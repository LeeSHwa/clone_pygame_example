# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))
menu.add("물")

menu = list(menu)
print(menu, type(menu))
menu.append("술")

menu = tuple(menu)
print(menu, type(menu))
