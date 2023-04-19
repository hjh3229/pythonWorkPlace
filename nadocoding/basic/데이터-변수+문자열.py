print("Python", "Java") # Python Java # , 사용시 자동으로 띄어쓰기
# sep = 문자 연결문구 지정
print("Python", "Java", sep = ",") # Python,Java
print("Python", "Java", "C++", sep = " vs ") # Python vs Java vs C++
# end = 문장의 끝부분 지정, 뒷문장 연결
print("Python", "Java", sep = ",", end = "! ")
print("무엇이 더 재밌을까요?") # Python,Java! 무엇이 더 재밌을까요?

import sys
print("Python", "Java", file=sys.stdout) # Python Java  # 표준출력
print("Python", "Java", file=sys.stderr) # Python Java  # 표준에러

# 정렬       # ljust = 칸 내에서 왼쪽정렬    # rjust = 칸 내에서 오른쪽정렬
scores = {"수학":50, "영어":0, "코딩":100}
for subject, score in scores.items():      # key value = subject, value name = score
    print(subject.ljust(8), str(score).rjust(4), sep=":") 
# 수학      :  50
# 영어      :   0
# 코딩      : 100

# zfill = 공백대신 0 채워서 정렬  (zero+fill)
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
# 대기번호 : 001
# 대기번호 : 002
# 대기번호 : 003
#      .
#      .
#      .
# 대기번호 : 020

# input = 프로그램 실행시 입력
'''입력값은 무조건 문자로 취급'''
answer = input("")
print(type(answer))
# 한지훈                  # 27
# <class 'str'>          # <class 'str'> 