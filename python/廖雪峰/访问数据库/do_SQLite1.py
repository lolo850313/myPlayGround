import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
cursor.execute("insert into user (id, name) values (\'1\', \'Mike\')")
cursor.rowcount
cursor.close()
conn.commit()

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
cursor.execute('select * from user where id=?', ('1',))
values = cursor.fetchall()
values
cursor.close()
conn.close()