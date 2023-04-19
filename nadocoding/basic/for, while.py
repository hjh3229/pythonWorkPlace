for waiting_no in [1,2,3,4,5]:        # = for waiting_no in range(1, 6)
    print("대기번호 : {0}".format(waiting_no))
# 대기번호 : 1
# 대기번호 : 2
# 대기번호 : 3
# 대기번호 : 4
# 대기번호 : 5     ==> 정해진 범위 내에서 반복 = for

avengers = ["아이언 맨", "토르", "헐크", "캡틴 아메리카"]
for hero in avengers:
    print("아이 앰 {0}".format(hero))
# 아이 앰 아이언 맨
# 아이 앰 토르
# 아이 앰 헐크
# 아이 앰 캡틴 아메리카


index = 5
while index >= 1:
    print("숙제 {0} 번만 더 안해오면 죽는다.".format(index))
    index -= 1
    if index == 0:
        print("넌 뒤졌다.")
# 숙제 5 번만 더 안해오면 죽는다.
# 숙제 4 번만 더 안해오면 죽는다.
# 숙제 3 번만 더 안해오면 죽는다.
# 숙제 2 번만 더 안해오면 죽는다.
# 숙제 1 번만 더 안해오면 죽는다.
# 넌 뒤졌다.                      ==> 탈출조건이 나올 때까지 반복 = while

# index = 1
# while True:
#     print("양 {0}마리".format(index))
#     index += 1
# 양 1마리 부터 무한반복   <== 무한로그   <== 멈추려면 터미널에서 ctrl+c

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비 되었습니다.".format(customer))
    person = input("성함이 어떻게 되세요? ")
# 토르님, 커피가 준비 되었습니다.
# 성함이 어떻게 되세요? 아이언맨
# 토르님, 커피가 준비 되었습니다.
# 성함이 어떻게 되세요? 아이 앰 그루트
# 토르님, 커피가 준비 되었습니다.
# 성함이 어떻게 되세요? 토르


# 한 줄 for := 조건문
students = ["Iron man", "Thor", "I am groot"]
students = [i.upper() for i in students]
print(students) # ['IRON MAN', 'THOR', 'I AM GROOT']

students = [len(i) for i in students]
print(students) # [8, 4, 10]