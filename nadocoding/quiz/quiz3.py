'''
비밀번호 만들기 규칙
규칙 1 : url에서 http:// 부분 삭제
규칙 2 : .부터 뒷부분 삭제
규칙 3 : 앞에서부터 3글자 + 글자수 + "e"의 개수 + !
'''


url = "http://naver.com"
my_str=url.replace("http://", "")
my_str=my_str[:my_str.index(".")]
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))

url = "http://google.com"
my_str=url.replace("http://", "")
my_str=my_str[:my_str.index(".")]
password=my_str[:3]+str(len(my_str))+str(my_str.count("e"))+"!"
print("{0}의 비밀번호는 {1}입니다.".format(url, password))