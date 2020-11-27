# -*- coding: utf-8 -*-

import os, sqlite3

#os.path.dirname(__file__)返回脚本的路径,再通过join在本py文件的文件夹下创建一个test
db_file = os.path.join(os.path.dirname(__file__), 'test.db')
#如果有db文件存在就删除已存在的db文件
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据: conn = sqlite3.connect('D:\\lolo\\python\\廖雪峰\\访问数据库\\test.db')
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Bart', 62)")
cursor.execute(r"insert into user values ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, high):
    ' 返回指定分数区间的名字，按分数从低到高排序 '
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name,score  from user ORDER BY score")
    nameList = []
    for i in cursor:
        if i[2]<low :
            pass
        elif i[2]>high:
            pass
        else:
            nameList.append(i[1])
    return nameList

# ssert的异常参数，其实就是在断言表达式后添加字符串信息，用来解释断言并更好的知道是哪里出了问题。
# 比如 ： assert len(lists) >=5,'列表元素个数小于5'

# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')