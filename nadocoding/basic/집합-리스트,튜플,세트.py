# 리스트 = []
list1 = 10
list2 = 20
list3 = 30
list_ = [10, 20, 30]
print(list_) # [10, 20, 30]

# 리스트 내 위치 = .index()     리스트에 추가 = .append()    x 번째에 삽입 = .insert(x, "@")   
# 뒤에서부터 꺼내기 = .pop()    리스트 내 복수 값의 개수 = .count()
subway = ["유재석", "박명수", "정형돈"]
print(subway.index("박명수")) # 1
subway.append("하하")
print(subway) # ['유재석', '박명수', '정형돈', '하하']
subway.insert(2, "정준하")
print(subway) # ['유재석', '박명수', '정준하', '정형돈', '하하']
print(subway.pop()) # 하하 <== 꺼내진 대상
print(subway) # ['유재석', '박명수', '정준하', '정형돈']
subway.append("유재석") # ['유재석', '박명수', '정준하', '정형돈', '유재석']
print(subway.count("유재석")) # 2

# 리스트에서 숫자의 정렬 = .sort()    순서 뒤집기 = .reverse()     모두 지우기 = .clear()
num_list = [4,3,5,1,2]
num_list.sort()
print(num_list) # [1, 2, 3, 4, 5]
num_list.reverse()
print(num_list) # [5, 4, 3, 2, 1]
num_list.clear()
print(num_list) # []

# 리스트 확장 = .extend
num_list = [4,3,5,1,2]
mix_list = ["유재석", 3, True]
num_list.extend(mix_list)
print(num_list) # [4, 3, 5, 1, 2, '유재석', 3, True]



# 튜플 = ()
'''리스트와 달리 새로운 키나 변수를 추가하거나 수정할 순 없지만 출력이 빠름.'''

menu = ("돈까스", "우동")
print(menu) # ('돈까스', '우동')
print(menu[0]) # 돈까스
# menu.add("덮밥") # 오류

# 활용법
name = "한지훈"
age = 23
hobby = "퍼즐"
print(name, age, hobby) # 한지훈 23 퍼즐

(name, age, hobby) = ("한지훈", 23, "퍼즐") 
print(name, age, hobby) # 한지훈 23 퍼즐



# 집합 (set) = {} = set([])
'''중복 안됨, 순서 없음'''

my_set = {1,2,3,3,3}
print(my_set) # {1, 2, 3}

# 교집합 = & or .intersection()     합집합 = | or .union()     
# 차집합 = - or difference                                   ==> 원래순서와 상관없이 사전순으로 배열
mudo = {"유재석", "박명수", "하하"}
running = set(["유재석", "이광수", "하하"])
print(mudo & running) # {'유재석', '하하'}
print(mudo.intersection(running)) # {'유재석', '하하'}
print(mudo | running) # {'박명수', '유재석', '이광수', '하하'}
print(mudo.union(running)) # {'박명수', '유재석', '이광수', '하하'}
print(mudo - running) # {'박명수'}
print(running.difference(mudo)) # {'이광수'}

# 원소 추가 = .add()      원소 제거 = .remove()
mudo.add("조세호")
print(mudo) # {'유재석', '박명수', '조세호', '하하'}
running.remove("이광수")
print(running) # {'하하', '유재석'}


# 자료구조 변경
# 구조 확인 = @,type(@)     구조 변경 = @ = list or tuple or set(@)
print(subway,type(subway)) # ['유재석', '박명수', '정준하', '정형돈', '유재석'] <class 'list'>
print(menu,type(menu)) # ('돈까스', '우동') <class 'tuple'>
print(mudo,type(mudo)) # {'유재석', '하하', '조세호', '박명수'} <class 'set'>
subway = tuple(subway)
menu = set(menu)
mudo = list(mudo)
print(subway,type(subway)) # ('유재석', '박명수', '정준하', '정형돈', '유재석') <class 'tuple'>
print(menu,type(menu)) # {'우동', '돈까스'} <class 'set'>
print(mudo,type(mudo)) # ['박명수', '조세호', '유재석', '하하'] <class 'list'>