# import Practice_Package.Thailand
# trip_to = Practice_Package.Thailand.ThailandPackage()
# trip_to.detail()

# from Practice_Package.Thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from Random import * 처럼 모든 걸 불러오고 싶을 때
# 파일 내에 __init__에 가서 __all__ = [" "," "] 
# 위와 같은 방식으로 공개할 정보를 정할 수 있음

from Practice_Package import *
trip_to = Vietnam.VietnamPackage()
trip_to.detail()

# trip_to2 = Thailand.ThailandPackage()
# trip_to2.detail()


import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(Vietnam)) # 마찬가지로 __init__에서 베트남만 포함시켰기에, 태국은 안됨

