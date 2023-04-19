# for, while 반복문에서 진행/정지 명령어

# 조건 만족시 무시하고 계속 진행 = continue
absent = [4,7]
for student in range(1,11):
    if student in absent:
        continue
    print("{0}번 출석".format(student))
# 1번 출석
# 2번 출석
# 3번 출석
# 5번 출석
# 6번 출석
# 8번 출석
# 9번 출석
# 10번 출석        <== 4번,7번은 조건을 만족하므로 부르지 않고 다음 진행,

for student in range(1,11):
    if student in absent:
        print("{0}번 결석".format(student))
        continue
    elif student in absent:                # = elif not student in absent
        continue
    print("{0}번 출석".format(student))      
# 1번 출석
# 2번 출석
# 3번 출석
# 4번 결석
# 5번 출석
# 6번 출석
# 7번 결석
# 8번 출석
# 9번 출석
# 10번 출석    
# if+continue+print=조건 만족시 무시 나머지 출력, if+print+continue=조건 만족시 출력 나머지 무시

# 조건 만족시 정지 = break
absent = [4,7]
no_homework = [6]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_homework:
        print("{0}번 숙제 안해왔어?".format(student))
        break
    print("{0}번 출석".format(student))
# 1번 출석
# 2번 출석
# 3번 출석
# 5번 출석
# 6번 숙제 안해왔어?       <== 4번은 continue로 무시하고 진행, 6번은 break로 정지

absent = [4,7]
no_homework = [6]
for student in range(1,11):
    if student in absent:
        continue
    elif student in no_homework:
        break
    print("{0}번 출석".format(student))
# 1번 출석
# 2번 출석
# 3번 출석
# 5번 출석               <== break 전 출력 문장이 없어 정지만 함
# if+break+print=조건 만족시 정지 O, 출력 X, if+print+break=조건 만족시 정지O, 출력O