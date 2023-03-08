# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙 3 : 남은 글자 중  처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 구성
                    # (nav)           (5)             (1)         (!)
# ex) 생선된 비밀번호 : nav51!

# site = "http://naver.com"

# ini = site[7:10]

# ran = len(site[7:12])

# num = site.count('e')

# password = str(ini) + str(ran) + str(num) + '!'

# print(password)

URL = "http://naver.com"

my_str = URL.replace("http://", "") # 규칙 1
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(f"생성된 비밀번호 : {password}")

print("{0} 의 비밀번호는 {1}입니다.".format(URL, password))