# web2.py 
#웹크롤링을 위한 선언
from bs4 import BeautifulSoup
#웹서버에 요청
import urllib.request

url = "https://www.clien.net/service/board/sold" 
data = urllib.request.urlopen(url).read()
soup = BeautifulSoup(data, "html.parser")
list = soup.find_all("span", attrs={"data-role": "list-title-text"})
for tag in list:
    title = tag.text.strip()
    print(title)


# <span class="subject_fixed" data-role="list-title-text" title="[예약중] 아이패드 미니 7 / 애플 케어 플러스 / 애플펜슬 프로">
# 			[예약중] 아이패드 미니 7 / 애플 케어 플러스 / 애플펜슬 프로
# </span>