# db1.py
import sqlite3

#연결객체를 리턴받기
con = sqlite3.connect(":memory:")
#커서객체를 리턴받기
cur = con.cursor()
#테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum test);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")
#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#여러건을 입력
datalist = (("tom","010-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values(?,?);", datalist)
#검색
cur.execute("select * from PhoneBook;")

# for row in cur:
#     print(row[0] + " , " + row[1])

#검색메서드 사용
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())