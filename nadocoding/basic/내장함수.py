# input : 사용자 입력을 받는 함수
language = input("지금 쓰는 프로그램 : ")
print("{0} 사용중".format(language))
# 지금 쓰는 프로그램 : 파이썬
# 파이썬 사용중

# dir : 어떤 객채를 넘겼을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'language']
import random # 외장함수
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'language', 'random']
import pickle
print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', 
# '__package__', '__spec__', 'language', 'pickle', 'random']
print(dir(random))
# ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', ... , 'weibullvariate']
name = "Jim"
print(dir(name))
# ['__add__', '__class__', '__contains__', '__delattr__', ... , 'title', 'translate', 'upper', 'zfill']

# list of python builtins 검색을 통해 python 내에서 사용가능한 내장함수들을 찾아볼 수 있다.