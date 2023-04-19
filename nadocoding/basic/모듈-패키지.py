import travel.thailand 
trip_to = travel.thailand.ThailandPackage()
trip_to.detail() # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# import 뒤에는 class나 함수를 직접 가져오진 못함
# 하지만 form ~~ import 구문에서는 가능
# import travel.thailand.ThailandPackage
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail() # ModuleNotFoundError
from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()  # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()  # [베트남 패키지 3박 5일] 다낭, 호도 여행 60만원


# 모듈 내에서 실행하는 것과 외부 파일에서 모듈의 함수를 불러와 실행하는 것은 구분됨.
from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()
# Thailand 외부에서 모듈 호출
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원

# travel/thailand.py에서 직접 실행하면 
# Thailand 모듈을 직접 실행
# 이 문장은 모듈을 직접 실행할 때만 실행돼요
# [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원
# 와 같이 출력됨.

# 모듈은 같은 경로 상에 있거나 py 라이브러리들이 모여있는 폴더에 있을 경우에만 불러올 수 있음.
# 이때 모듈, 패키지의 위치를 알 수 있는 함수가 있음.
import inspect
import random
print(inspect.getfile(random)) # C:\Python310\lib\random.py
print(inspect.getfile(thailand)) # c:\Users\한지훈\OneDrive\바탕 화면\pythonworkspace\개념\travel\thailand.py
# 파일 위치를 random 모듈이 있던 곳으로 옮긴 이후에도 잘 시행됨. 
# C:\Python310\lib\travel\thailand.py