# from travel import *
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()  # NameError

'''
from random import *와 달리 위 명령어는 오류가 발생

__init__파일에서 공개할 범위를 지정하지 않았기 때문.

__init__파일에서 __all__=["vietnam", "thailand"]를 입력해 공개할 범위를 지정 후 위 명령어를 다시 시행하면
'''

from travel import *
trip_to = vietnam.VietnamPackage()
trip_to.detail()  # [베트남 패키지 3박 5일] 다낭, 호도 여행 60만원
trip_to = thailand.ThailandPackage()
trip_to.detail()  # [태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원