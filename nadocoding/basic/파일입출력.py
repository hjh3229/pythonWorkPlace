score_file = open("score.txt","w",encoding="utf8") # "score.txt"=만들 파일명  "w"=덮어쓰기  "utf8"=한글
print("수학 : 0", file=score_file) # score_file에 수학점수 : 0 입력
print("영어 : 50", file=score_file) # score_file에 영어점수 : 50 입력
score_file.close()  # 파일닫기

score_file = open("score.txt","a",encoding="utf8") # "a"=이어쓰기
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") # .write로 작성시 줄바꾸기는 자동으로 되지 않음 = \n으로 줄바꾸기
score_file.close()

score_file = open("score.txt","r",encoding="utf8") # "r"=읽기
print(score_file.read()) # 한번에 읽기
score_file.close()
#수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline()) # readline=한 줄만 읽기+Enter
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
# 수학 : 0

# 영어 : 50

# 과학 : 80

# 코딩 : 100    # Enter 기능 때문에 한 칸씩 더 뜸

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline(), end="") 
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100   # end=""을 붙임으로서 엔터상태에서 연결하여 붙임

'''
위 방법은 4줄만 읽기 위한 방법이고, 몇 줄이든 전체를 읽기 위해선 아래 방법을 사용한다.
'''
score_file = open("score.txt","r",encoding="utf8")
while True:                        # 반복
    line = score_file.readline()   # line = score_file을 한 줄씩 읽기
    if not line:                   # line 진행 불가일 경우
        break                      # 정지
    print(line, end="")            # 반복할 명령
score_file.close()
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100

score_file = open("score.txt","r",encoding="utf8")
lines = score_file.readlines()  # 파일 내용들을 리스트 형태로 저장
for line in lines:
    print(line, end="")
# 수학 : 0
# 영어 : 50
# 과학 : 80
# 코딩 : 100