import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

query = "반도체"
url = f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# 기사 제목과 링크 수집
news_list = []
for idx, a in enumerate(soup.select('a.BHYkUbEQ2afEbTC7LXoA.tQzTN_dJmfJcpqVyJEAz'), 1):
    title = a.get_text(strip=True)
    link = a['href']
    news_list.append([idx, title, link])

# 엑셀 파일로 저장
wb = Workbook()
ws = wb.active
ws.title = "NaverNews"
ws.append(["번호", "제목", "링크"])

for news in news_list:
    ws.append(news)

wb.save("NaverNews.xlsx")
print("NaverNews.xlsx 파일로 저장 완료")