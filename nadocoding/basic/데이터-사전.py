# 키 만들기 = {a:x, b:y, ...}   (a,b,... = key,  x,y,... = value)
# value 출력 = print(사전[key]) (값 없으면 오류)    
# value 확인 = print(사전.get(key)) (값 없으면 None 출력, 또는 원하는 메시지 출력 가능) 
cabinet = {3:"유재석", 100:"조세호"}
print(cabinet[3]) # 유재석
print(cabinet.get(100)) # 조세호
# print(cabinet(5)) # 오류
print(cabinet.get(5)) # None
print(cabinet.get(5, "사용 가능")) # 사용 가능

# 키에 대응하는 값 존재여부 확인 = print(key in 사전)
print(3 in cabinet) # True
print(5 in cabinet) # False

# 새로운 키&값 또는 키에 대응하는 값 업데이트 = 사전[key]=value    key 삭제 = del 사전[key]
print(cabinet) # {3: '유재석', 100: '조세호'}
cabinet["A-5"]="김종국"
cabinet[100]="지석진"
print(cabinet) # {3: '유재석', 100: '지석진', 'A-5': '김종국'}
del cabinet["A-5"]
print(cabinet) # {3: '유재석', 100: '지석진'}

# key 만 출력 = 사전.keys()     value 만 출력 = 사전.values()    key, value 쌍으로 출력 = 사전.items
print(cabinet.keys()) # dict_keys([3, 100])
print(cabinet.values()) # dict_values(['유재석', '지석진'])
print(cabinet.items()) # dict_items([(3, '유재석'), (100, '지석진')])

# 사전 초기화 = 사전.clear()
cabinet.clear()
print(cabinet) # {}