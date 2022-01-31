import sqlite3

con = sqlite3.connect("first.db")

cur = con.cursor()

sql = 'create table t_person(pno INTEGER PRIMARY KEY  AUTOINCREMENT ,pname varchar(30) NOT NULL ,age INTEGER)'

try:
    cur.execute(sql)
except Exception as e:
    print(e)
    print('创建表失败')
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()