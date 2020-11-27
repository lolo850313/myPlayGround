import sqlite3
conn = sqlite3.connect("test.db")
cur = conn.cursor()

print("start")

cur.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
conn.commit()
print("Total number of rows updated : ", conn.total_changes)

cur = conn.execute("SELECT id, name, address, salary from COMPANY ")
for row in cur:
    print("ID = ", row[0], "NAME = ", row[1], "ADDRESS = ", row[2], "SALARY = ", row[3])

print("end")