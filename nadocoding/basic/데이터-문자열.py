# 2줄 이상 출력 = """   """
sentence1 = """제 이름은 한지훈이고
나이는 23살이에요."""
print(sentence1) # 제 이름은 한지훈이고
                 # 나이는 23살이에요.

# @번째 문자 = [@]    x부터 y 직전까지 = [x:y]    
# 처음부터 y 직전까지 = [:y]     x부터 끝까지 = [x:]     뒤에서 x부터 끝까지 = [-x:]
jumin = "000417-3933810"
print(jumin[4]) # 1
print(jumin[4:6]) # 17
print(jumin[:6]) # 000417
print(jumin[7:]) # 3933810
print(jumin[-7:]) # 3933810
print(jumin[-14:-8]) # 000417

# 문장 소문자 변환 = ~~.lower()     문장 대문자 변환 = ~~.upper()
# @번째 문자 대문자 여부 확인 = ~~[@].isupper()
# 문장 길이 = len()    단어교체 = ~~.replace("x", "y") (대소문자 구분)     특정 단어의 개수 = ~~.count("@")
python = "Python is Amazing"
print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True
print(len(python)) # 17
print(python.replace("Python", "Java")) # Java is Amazing
print(python.replace(" is Amazing", "")) # Python
print(python.count("n")) # 2

# 특정 문자의 처음 위치 = ~~.index("@")     특정 문자의 다음 위치 = ~~.index("@", index+1)
print(python.index("n")) # 5
print(python.index("n", 5+1)) # 15
index = python.index("n")
print(index) # 5
index = python.index("n", index+1)
print(index) # 15

# index와 유사한 함수 find      
'''차이점: find 함수는 찾는 결과가 없으면 -1이 출력되지만 index는 오류가 뜸'''
# print(python.index("Java")) # 오류
print(python.find("Java")) # -1