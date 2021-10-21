# web1.py
from bs4 import BeautifulSoup

#웹페이지를 로딩
#메서드나 함수를 메서드체인(연속으로 호출)
page = open("c:\\work\\test01.html", encoding="utf-8").read()
# 검색이 용이한 객체
# soup = BeautifulSoup(page, "html.parser")
soup = BeautifulSoup(page, "html.parser")
#print( soup.prettify() )

#<p> 몽땅 검색
#print( soup.find_all("p"))
#<a> 태그 잡아와~~
#print( soup.find_all("a") )
#print( soup.find("p") )

# 검색 조검:<p class='out-text'>
# 파이썬의 키워드로 class가 제공 그래서 이름 충돌 class_
#print( soup.find_all("p", class_="outer-text") )

#태그 안쪽에 컨텐츠만 가져오기
for item in soup.find_all("p"):
    #태그를제거하고 컨테츠마 가져오기 .text
    data = item.text.strip()
    data = data.replace("\n","")
    data = data.replace("\t","")
    print(data)