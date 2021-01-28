import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()
print("start")

cur.execute("DELETE from COMPANY where ID=2")
conn.commit()

print("Total number of rows deleted : ", conn.total_changes)

cur = conn.execute("SELECT id, name, address, salary  from COMPANY")
for row in cur:
    print("ID = ", row[0], "NAME = ", row[1], "ADDRESS = ", row[2], "SALARY = ", row[3])

print("end")
conn.close()