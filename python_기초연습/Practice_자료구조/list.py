subway = [10,20,30]

subway = ["유재석", "조세호", "박명수"]
print(subway)  

print(subway.index("조세호"))

subway.append("하하")
print(subway)  

subway.insert(1, "정형돈") #삽일 될 인덱스가 먼저 와야함
print(subway)  

subway.pop()
print(subway)  

# subway.pop()
# print(subway)  

# subway.pop()
# print(subway)  

subway.append("유재석")
print(subway)  
print(subway.count("유재석")) # 해당 객체가 몇개 있는지

num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)  

num_list.clear()
print(num_list)

mix_list =  ["조세호", 20, True]
print(mix_list)

mix_list.extend(mix_list)
print(mix_list)