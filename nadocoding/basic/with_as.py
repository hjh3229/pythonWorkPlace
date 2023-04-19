# with as = 파일을 연 후 자동으로 close를 실행해줌
'''if, for, while, def와 같이 구문 안에 있는 변수는 구문을 벗어나면 쓸 수 없음(지역변수)'''

import pickle

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))  # {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
# 자동으로 파일을 닫아주기에 profile_file.close() 필요 없음
'''
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
profile_file.close()
'''
# 위 명령어와 결과가 같음.

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")
# study.txt라는 파일을 만들고 파이썬을 열심히 공부하고 있어요가 입력됨.
'''
study_file = open("study.txt", "w", encoding="utf8")
study_file.write("파이썬을 열심히 공부하고 있어요")
study_file.close()
'''
# 위 명령어와 결과가 같음.

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read()) # 파이썬을 열심히 공부하고 있어요