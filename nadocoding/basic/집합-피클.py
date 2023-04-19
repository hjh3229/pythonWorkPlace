# 데이터를 파일 형식으로 저장, 사용하는 것
# 따로 인코딩이 필요하지 않음.
import pickle   # pickle 쓰기 전 입력
'''
현재 파일명을 pickle로 두면 import가 모듈이 아닌 현재 파일을 먼저 인식하기에 파일명을 다르게 해줘야함.
현 파일 이름이 pickle.py일 때 다음과 같은 오류가 발생했음.
AttributeError: partially initialized module 'pickle' has no attribute 'dump' 
(most likely due to a circular import)
'''
profile_file = open("profile.pickle", "wb")  # wb=write binary=입력전용 바이너리 파일
profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)   # profile 내용 확인 
# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
pickle.dump(profile, profile_file) # dump = profile에 있는 정보를 profile_file에 저장
profile_file.close()   # 파일입출력과 마찬가지로 파일닫기

profile_file = open("profile.pickle", "rb")  # rb=읽기전용
profile = pickle.load(profile_file) # load = profile_file에 있는 정보를 profile에 불러오기
# {'이름': '박명수', '나이': 30, '취미': ['축구', '골프', '코딩']}
profile_file.close()