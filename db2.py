# db1.py 
import sqlite3
#연결객체를 생성
#물리적인 파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체를 생성
cur = con.cursor()
#테이블을 생성
cur.execute("create table if not exists person " + 
    "(id integer primary key autoincrement, name text, phoneNum text);")

#데이터 입력
cur.execute("insert into person (name, phoneNum) values (?, ?);", 
    ("홍길동", "010-1234-5678"))

#입력 파라메터 처리: GUI화면에서 별도 입력 
name = "전우치"
phoneNum = "010-9876-5432"
cur.execute("insert into person (name, phoneNum) values (?, ?);", (name, phoneNum))

#다중의 레코드를 입력
datalist = (("성춘향", "010-1111-2222"),("이몽룡", "010-3333-4444"))
cur.executemany("insert into person (name, phoneNum) values (?, ?);", datalist)
#완료하고 종료
con.commit()  #변경사항을 저장

#데이터 조회
# cur.execute("select * from person;")
# print("---fetchone()---")
# print(cur.fetchone()) 

# print("---fetchmany(2)---")
# print(cur.fetchmany(2)) 

print("---fetchall()---")
cur.execute("select * from person;")
print(cur.fetchall()) 
