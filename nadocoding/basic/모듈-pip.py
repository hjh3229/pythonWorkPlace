# 이미 잘 만들어진 모듈이 많기 때문에 새로운 모듈이나 패키지를 만들기 보다는 찾아서 사용하는 편이 효율적이다.
'''https://pypi.org/''' #에서 검색가능, browse projects를 클릭해 정리된 기준을 통해 찾을 수도 있음.
# ex) beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
print(soup.prettify())
#   soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# <p>
#  Some
#  <b>
#   bad
#   <i>
#    HTML
#   </i>
#  </b>
# </p>

# terminal에서 pip list + Enter 현재 설치되어 있는 pip를 보여줌.

# 또한 pip show 정보를 보고자 하는 pip이름 + Enter 해당 pip의 간단한 정보를 보여줌.
# PS C:\Users\한지훈\OneDrive\바탕 화면\pythonworkspace> pip show  beautifulsoup4
# Name: beautifulsoup4
# Version: 4.11.1
# Summary: Screen-scraping library
# Home-page: https://www.crummy.com/software/BeautifulSoup/bs4/
# Author: Leonard Richardson
# Author-email: leonardr@segfault.org
# License: MIT
# Location: c:\python310\lib\site-packages
# Requires: soupsieve
# Required-by:

# pip install --upgrade 패키지명 + Enter 해당 패키지 최신버전 업그레이드

# pip uninstall 패키지명 + Enter + y 해당 패키지 삭제