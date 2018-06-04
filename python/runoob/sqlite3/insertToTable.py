import sqlite3

conn = sqlite3.connect('test.db')
cur = conn.cursor()

print('open table')

cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES(1, 'Paul', 32, 'Califonia', 20000.00)")

cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY) \
            VALUES(2, 'Allen', 25, 'Texas', 15000.00)")

cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(3, 'Teddy', 24, 'Norway', 20000.00)")

cur.execute("INSERT INTO COMPANY(ID, NAME, AGE, ADDRESS, SALARY)\
            VALUES(4, 'Mark', 33, 'richmond', 65000.00)")

conn.commit()

print('record ok')

conn.close()