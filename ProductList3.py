# MyProduct.ui(화면단) + ProductList3.py(로직단) 
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sqlite3
import os.path

# 데이터베이스 처리 클래스
class ProductDB:
    def __init__(self, db_path="ProductList.db"):
        self.db_path = db_path
        self.con = sqlite3.connect(self.db_path)
        self.cur = self.con.cursor()
        self._init_db()

    def _init_db(self):
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INTEGER);"
        )
        self.con.commit()

    def add_product(self, name, price):
        self.cur.execute("INSERT INTO Products (Name, Price) VALUES (?, ?);", (name, price))
        self.con.commit()

    def update_product(self, prod_id, name, price):
        self.cur.execute("UPDATE Products SET Name=?, Price=? WHERE id=?;", (name, price, prod_id))
        self.con.commit()

    def remove_product(self, prod_id):
        self.cur.execute("DELETE FROM Products WHERE id=?;", (prod_id,))
        self.con.commit()

    def get_products(self):
        self.cur.execute("SELECT * FROM Products;")
        return self.cur.fetchall()

# UI 처리 클래스
form_class = uic.loadUiType("MyProduct.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self, db):
        super().__init__()
        self.setupUi(self)
        self.db = db

        # QTableWidget 설정
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        self.tableWidget.setTabKeyNavigation(False)
        self.prodID.returnPressed.connect(lambda: self.focusNextChild())
        self.prodName.returnPressed.connect(lambda: self.focusNextChild())
        self.prodPrice.returnPressed.connect(lambda: self.focusNextChild())
        self.tableWidget.doubleClicked.connect(self.doubleClick)

        # 버튼 시그널 연결
        self.pushButton.clicked.connect(self.getProduct)
        self.pushButton_2.clicked.connect(self.addProduct)
        self.pushButton_3.clicked.connect(self.updateProduct)
        self.pushButton_4.clicked.connect(self.removeProduct)

        self.getProduct()  # 시작 시 데이터 표시

    def addProduct(self):
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        if not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "제품명과 가격(숫자)을 올바르게 입력하세요.")
            return
        self.db.add_product(name, int(price))
        self.getProduct()

    def updateProduct(self):
        prod_id = self.prodID.text().strip()
        name = self.prodName.text().strip()
        price = self.prodPrice.text().strip()
        if not prod_id.isdigit() or not name or not price.isdigit():
            QMessageBox.warning(self, "입력 오류", "ID, 제품명, 가격(숫자)을 올바르게 입력하세요.")
            return
        self.db.update_product(int(prod_id), name, int(price))
        self.getProduct()

    def removeProduct(self):
        prod_id = self.prodID.text().strip()
        if not prod_id.isdigit():
            QMessageBox.warning(self, "입력 오류", "ID를 올바르게 입력하세요.")
            return
        self.db.remove_product(int(prod_id))
        self.getProduct()

    def getProduct(self):
        self.tableWidget.clearContents()
        products = self.db.get_products()
        self.tableWidget.setRowCount(max(50, len(products)))
        for row, item in enumerate(products):
            itemID = QTableWidgetItem(str(item[0]))
            itemID.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 0, itemID)
            self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
            itemPrice = QTableWidgetItem(str(item[2]))
            itemPrice.setTextAlignment(Qt.AlignRight)
            self.tableWidget.setItem(row, 2, itemPrice)

    def doubleClick(self):
        row = self.tableWidget.currentRow()
        if self.tableWidget.item(row, 0):
            self.prodID.setText(self.tableWidget.item(row, 0).text().strip())
            self.prodName.setText(self.tableWidget.item(row, 1).text().strip())
            self.prodPrice.setText(self.tableWidget.item(row, 2).text().strip())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = ProductDB()
    myWindow = Window(db)
    myWindow.show()
    sys.exit(app.exec_())



