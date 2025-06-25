import sqlite3
import random

class ElectronicsDB:
    def __init__(self, db_name="electronics.db"):
        self.conn = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS products (
                    product_id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    price INTEGER NOT NULL
                )
            """)

    def insert_product(self, product_id, name, price):
        with self.conn:
            self.conn.execute(
                "INSERT INTO products (product_id, name, price) VALUES (?, ?, ?)",
                (product_id, name, price)
            )

    def update_product(self, product_id, name=None, price=None):
        with self.conn:
            if name and price is not None:
                self.conn.execute(
                    "UPDATE products SET name=?, price=? WHERE product_id=?",
                    (name, price, product_id)
                )
            elif name:
                self.conn.execute(
                    "UPDATE products SET name=? WHERE product_id=?",
                    (name, product_id)
                )
            elif price is not None:
                self.conn.execute(
                    "UPDATE products SET price=? WHERE product_id=?",
                    (price, product_id)
                )

    def delete_product(self, product_id):
        with self.conn:
            self.conn.execute(
                "DELETE FROM products WHERE product_id=?",
                (product_id,)
            )

    def select_products(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM products")
        return cursor.fetchall()

    def close(self):
        self.conn.close()

# 샘플 데이터 100개 생성 및 삽입
def generate_sample_data(db):
    names = ["노트북", "스마트폰", "태블릿", "모니터", "키보드", "마우스", "프린터", "스피커", "헤드폰", "카메라"]
    for i in range(1, 101):
        name = f"{random.choice(names)}_{i}"
        price = random.randint(50, 1000)
        db.insert_product(i, name, price)

#만약에 모듈을 직접 실행한 경우면 
if __name__ == "__main__":
    db = ElectronicsDB()
    # 샘플 데이터가 없을 때만 생성
    if not db.select_products():
        generate_sample_data(db)
        print("샘플 데이터 100개가 삽입되었습니다.")
    else:
        print("이미 데이터가 존재합니다.")

    # 데이터 조회 예시
    for product in db.select_products()[:50]:
        print(product)

    db.close()