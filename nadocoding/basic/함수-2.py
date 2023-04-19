# 함수 값 일일히 입력
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")  # 이름: 유재석    나이: 20        주 사용 언어: 파이썬
profile("김태호", 25, "자바")    # 이름: 김태호    나이: 25        주 사용 언어: 자바

# 기본값을 이용        기본값 입력한 변수는 입력필요 X
def profile(name, age=17, main_lang="파이썬"):         # '나이'와 '주 사용 언어'에 기본값 적용
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile("유재석") # 이름: 유재석    나이: 17        주 사용 언어: 파이썬
profile("김태호") # 이름: 김태호    나이: 17        주 사용 언어: 파이썬

# 키워드값을 이용       변수입력순서 상관 X
def profile(name, age, main_lang):
    print("이름: {0}\t나이: {1}\t주 사용 언어: {2}"\
        .format(name,age,main_lang))

profile(name="유재석", age=20, main_lang="파이썬") # 이름: 유재석    나이: 20        주 사용 언어: 파이썬
profile(main_lang="파이썬", name="유재석", age=20) # 이름: 유재석    나이: 20        주 사용 언어: 파이썬

'''
def profile(name,age,lang1,lang2,lang3,lang4,lang5):
    print("이름: {0}\t나이: {1}\t".format(name,age), end=" ")  # end=" " = 아래 출력문을 뒤에 이어서 입력
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#") 
# 이름: 유재석    나이: 20         Python Java C C++ C#
profile("김태호", 25, "Python", "Java", "","","") 
# 이름: 김태호    나이: 25         Python Java
필요한 만큼 변수를 일일히 써야하고, 후에 변수가 늘어날 땐 함수 자체를 수정해야 함
'''
# 가변인자 이용
def profile(name,age,*language): # 가변인자 = *~~~
    print("이름: {0}\t나이: {1}\t".format(name,age), end=" ")
    for lang in language:        # 변수를 입력하는 만큼 반복하기 위해 for 이용
        print(lang, end=" ")
    print()                      # 입력 없으면 공백으로 정지

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "Java Script") 
# 이름: 유재석    나이: 20         Python Java C C++ C# Java Script
profile("김태호", 25, "Python", "Java") 
# 이름: 김태호    나이: 25         Python Java

