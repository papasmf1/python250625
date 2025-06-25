# web1.py 
#웹크롤링을 위한 선언 
from bs4 import BeautifulSoup

#문서를 로딩(메서드체인)
page = open("test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 스프객체
soup = BeautifulSoup(page, "html.parser")
#전체 보기 
#print(soup.prettify())
#<p>전체를 검색
#print(soup.find_all("p"))
#<p>첫번째 한개 
#print(soup.find("p"))
#조건: <p class="outer-text">
#print(soup.find_all("p", class_ = "outer-text"))
#조건검색: attrs속성 dict형식 
#print(soup.find_all("p", attrs = {"class": "outer-text"}))

#태그 내부의 문자열: .text속성 
for tag in soup.find_all("p"):
    title = tag.text.strip()
    title = title.replace("\n", "")
    print(title)


