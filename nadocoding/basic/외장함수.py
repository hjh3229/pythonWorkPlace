# 내장함수와 달리 직접 import 해서 사용해야 함.
# list of python modules 검색을 통해 외장함수 목록을 볼 수 있음. # ex) random, glob, ...

# glob : 경로 내의 폴더/ 파일 목록 조회 (= 윈도우 dir)
import glob
print(glob.glob("*.py")) # 확장자가 py인 모든 파일 조회
# ['helloworld.py', 'practice.py']

# os : 운연체제에서 제공하는 기본 기능
import os
print(os.getcwd()) # 현재 디렉토리
# C:\Users\한지훈\OneDrive\바탕 화면\pythonworkspace
folder = "sample_dir"
if os.path.exists(folder): # 경로 상에 폴더가 있을 시
    print("이미 존재하는 폴더입니다.")
    os.rmdir(folder)       # 폴더 삭제
    print(folder, "폴더를 삭제하였습니다.")
else:                      # 경로 상에 폴더가 없을 시
    os.makedirs(folder) # 폴더 생성
    print(folder, "폴더를 생성하였습니다.")
# sample_dir 폴더를 생성하였습니다. # 처음 실행 시
# 이미 존재하는 폴더입니다.
# sample_dir 폴더를 삭제하였습니다. # 다음 실행 시
print(os.listdir())  # glob과 달리 같은 경로의 파일, 폴더 전부 조회
# ['helloworld.py', 'practice.py', 'profile.pickle', 'quiz', 'score.txt', 'study.txt', '개념']

import time # 시간 관련 함수
print(time.localtime())
# time.struct_time(tm_year=2022, tm_mon=12, tm_mday=30, tm_hour=17, tm_min=26, 
# tm_sec=11, tm_wday=4, tm_yday=364, tm_isdst=0)
print(time.strftime("%Y-%m-%d %H:%M:%S")) # %Y 등을 이용해 정리해서 표시
# 2022-12-30 17:28:56

import datetime
print("오늘 날짜는 ", datetime.date.today())
# 오늘 날짜는  2022-12-30
date = datetime.date.today() # 오늘 날짜 지정
td = datetime.timedelta(days=100) # timedelta : 두 날짜 사이의 간격 # 100일 후 저장
print("우리가 만난지 100일은", date+td) # 오늘부터 100일 후
# 우리가 만난지 100일은 2023-04-09