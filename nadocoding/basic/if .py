# if 
# if 조건 : 
#     실행 명령문
# elif 조건 :        <== 위 조건이 안 맞을때 다음 조건
#     실행 명령문
# else:
#     실행 명령문     <== 그 외에 조건일 경우
weather = "비"
if weather == "비" :
    print("우산을 챙기세요") # 우산을 챙기세요

weather = "맑음"
if weather == "비":
    print("우산을 챙기세요") # 출력 X

weather = "미세먼지"
if weather == "비" :
    print("우산을 챙기세요") # 출력 X
elif weather == "미세먼지" : 
    print("마스크를 챙기세요") # 마스크를 챙기세요

weather = "맑음"
if weather == "비" :
    print("우산을 챙기세요") # 출력 X
elif weather == "미세먼지" : 
    print("마스크를 챙기세요") # 출력 X
else :
    print("준비물이 필요 없어요") # 준비물이 필요 없어요

# 사용자가 직접입력 = input()       or, and 연산자를 통해 조건 추가 가능
weather = input("오늘 날씨 어때요? ")
if weather == "비" or weather == "눈":
    print("우산을 챙기세요") # 비 또는 눈 입력 => 우산을 챙기세요 | 아니면 출력 X
elif weather == "미세먼지" : 
    print("마스크를 챙기세요") # 미세먼지 입력 => 마스크를 챙기세요 | 아니면 출력 X
else :
    print("준비물이 필요 없어요") # 그 외 입력 => 준비물이 필요 없어요

temp = int(input("기온이 어때요? "))
if temp >= 30 :
    print("더워요")
elif temp >= 10 and temp < 30 :
    print("적당해요")
elif temp < 10 and temp >= 0 :
    print("추워요")
else:
    print("엄청 추워요")