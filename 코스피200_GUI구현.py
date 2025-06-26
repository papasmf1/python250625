import sys
import requests
from bs4 import BeautifulSoup
import re
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem,
    QLabel, QPushButton, QLineEdit
)
from PyQt5.QtCore import Qt

def clean_number(text):
    if isinstance(text, str):
        return re.sub(r'[^\d.-]', '', text)
    return text

def get_kospi200_top_stocks(max_pages=10):
    base_url = "https://finance.naver.com/sise/entryJongmok.naver"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }
    all_data = []
    for page in range(1, max_pages + 1):
        params = {"type": "KPI200", "page": page}
        response = requests.get(base_url, params=params, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        table = soup.find("table", class_="type_1")
        if not table:
            continue
        rows = table.find_all("tr")
        for row in rows:
            cols = row.find_all("td")
            if len(cols) == 7:
                stock_name = cols[0].get_text(strip=True)
                current_price = clean_number(cols[1].get_text(strip=True))
                change_elem = cols[2].find("span", class_="tah")
                change = clean_number(change_elem.get_text(strip=True)) if change_elem else "0"
                status = None
                if cols[2].find("em", class_="bu_pup"):
                    status = "상승"
                elif cols[2].find("em", class_="bu_pdn"):
                    status = "하락"
                elif cols[2].find("em", class_="bu_pn"):
                    status = "보합"
                change_rate = cols[3].get_text(strip=True)
                volume = clean_number(cols[4].get_text(strip=True))
                amount = clean_number(cols[5].get_text(strip=True))
                market_cap = clean_number(cols[6].get_text(strip=True))
                stock_link = cols[0].find("a")
                stock_code = None
                if stock_link and 'href' in stock_link.attrs:
                    code_match = re.search(r'code=(\d+)', stock_link['href'])
                    if code_match:
                        stock_code = code_match.group(1)
                all_data.append({
                    "종목코드": stock_code,
                    "종목명": stock_name,
                    "현재가": current_price,
                    "전일비": change,
                    "상태": status,
                    "등락률": change_rate,
                    "거래량": volume,
                    "거래대금(백만)": amount,
                    "시가총액(억)": market_cap
                })
    return all_data

class Kospi200App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("코스피200 편입종목 리스트")
        self.setGeometry(100, 100, 1200, 700)  # 창 크기 넓힘

        main_layout = QVBoxLayout()
        search_layout = QHBoxLayout()

        self.label = QLabel("코스피200 편입종목 상위 리스트")
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("종목명 또는 코드로 검색")
        self.search_btn = QPushButton("검색")
        self.search_btn.clicked.connect(self.search_stock)
        self.refresh_btn = QPushButton("새로고침")
        self.refresh_btn.clicked.connect(self.load_data)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)
        search_layout.addWidget(self.refresh_btn)

        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "종목명", "종목코드", "현재가", "전일비", "상태", "등락률", "거래량", "시가총액(억)"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)

        main_layout.addWidget(self.label)
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.table)
        self.setLayout(main_layout)

        self.all_stocks = []
        self.load_data()

    def load_data(self):
        self.all_stocks = get_kospi200_top_stocks(max_pages=10)
        self.display_stocks(self.all_stocks)

    def display_stocks(self, stocks):
        self.table.setRowCount(len(stocks))
        for row, stock in enumerate(stocks):
            self.table.setItem(row, 0, QTableWidgetItem(stock['종목명']))
            self.table.setItem(row, 1, QTableWidgetItem(stock['종목코드'] if stock['종목코드'] else ""))
            self.table.setItem(row, 2, QTableWidgetItem(stock['현재가']))
            self.table.setItem(row, 3, QTableWidgetItem(stock['전일비']))
            self.table.setItem(row, 4, QTableWidgetItem(stock['상태'] if stock['상태'] else ""))
            self.table.setItem(row, 5, QTableWidgetItem(stock['등락률']))
            self.table.setItem(row, 6, QTableWidgetItem(stock['거래량']))
            self.table.setItem(row, 7, QTableWidgetItem(stock['시가총액(억)']))

        # 각 컬럼의 폭을 넉넉하게 지정
        self.table.setColumnWidth(0, 180)  # 종목명
        self.table.setColumnWidth(1, 120)  # 종목코드
        self.table.setColumnWidth(2, 120)  # 현재가
        self.table.setColumnWidth(3, 120)  # 전일비
        self.table.setColumnWidth(4, 100)  # 상태
        self.table.setColumnWidth(5, 120)  # 등락률
        self.table.setColumnWidth(6, 180)  # 거래량
        self.table.setColumnWidth(7, 180)  # 시가총액(억)

    def search_stock(self):
        keyword = self.search_input.text().strip()
        if not keyword:
            self.display_stocks(self.all_stocks)
            return
        filtered = [
            stock for stock in self.all_stocks
            if keyword in stock['종목명'] or (stock['종목코드'] and keyword in stock['종목코드'])
        ]
        self.display_stocks(filtered)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Kospi200App()
    window.show()
    sys.exit(app.exec_())