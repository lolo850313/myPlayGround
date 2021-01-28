import sqlite3
conn = sqlite3.connect("test.db")

print("start")
cur = conn.execute("SELECT id, name, address, salary from COMPANY")

for row in cur:
    print("ID = ", row[0],"NAME = ", row[1],"ADDRESS = ", row[2],"SALARY = ", row[3])

print("End")
conn.close()
    


