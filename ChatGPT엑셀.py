from openpyxl import Workbook
import random

# 워크북과 시트 생성
wb = Workbook()
ws = wb.active
ws.title = "전자제품 목록"

# 헤더 추가
ws.append(["제품ID", "제품명", "가격", "수량"])

# 전자제품 이름 리스트
product_names = ["노트북", "스마트폰", "태블릿", "모니터", "키보드", 
                 "마우스", "프린터", "스피커", "웹캠", "게임기"]

# 데이터 100개 생성
for i in range(1, 101):
    #포맷스트링 문법 
    product_id = f"P{i:03d}"  # P001, P002, ...
    product_name = random.choice(product_names)
    price = random.randint(50, 2000)  # 가격: 5만 ~ 200만
    quantity = random.randint(1, 100)       # 수량: 1 ~ 100개
    ws.append([product_id, product_name, price, quantity])

# 엑셀 파일 저장
wb.save("ProductList.xlsx")
