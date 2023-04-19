# 모듈 = 코드의 파츠들을 교체하기 쉽게 분리해 놓는것
# 모듈은 같은 경로 상에 있거나 py 라이브러리들이 모여있는 폴더에 있을 경우에만 불러올 수 있음.

import theater_module   # 파일명만 적으면 되기 때문에 확장자 .py는 적을 필요 없음
theater_module.price(3) # 3명 가격은 30000원 입니다.
theater_module.price_morning(4) # 4명 조조 할인 가격은 24000원 입니다.
theater_module.price_soldier(5) # 5명 군인 할인 가격은 20000원 입니다.


import theater_module as mv  # theater.module을 줄여서 쓸 명령어 mv로 지정
mv.price(3)                  # 3명 가격은 30000원 입니다.
mv.price_morning(4)          # 4명 조조 할인 가격은 24000원 입니다.
mv.price_soldier(5)          # 5명 군인 할인 가격은 20000원 입니다.


# from random import *와 같이 앞에 붙이지 않고 함수만 가져오기도 가능
from theater_module import *
price(3)           # 3명 가격은 30000원 입니다.
price_morning(4)   # 4명 조조 할인 가격은 24000원 입니다.
price_soldier(5)   # 5명 군인 할인 가격은 20000원 입니다.


# 필요한 함수만 가져오기도 가능
from theater_module import price, price_morning
price(3)           # 3명 가격은 30000원 입니다.
price_morning(4)   # 4명 조조 할인 가격은 24000원 입니다.
price_soldier(5)   # NameError: name 'price_soldier' is not defined

# 가져온 함수의 이름 바꾸기 가능
from theater_module import price_soldier as price
price(3)           # 3명 군인 할인 가격은 12000원 입니다.