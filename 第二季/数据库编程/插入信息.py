# 导入sqllite3模块
import sqlite3

# 1.硬盘上创建连接
con = sqlite3.connect('first.db')
# 获取cursor对象
cur = con.cursor()
# 执行sql创建表
sql = 'insert into t_person(pname,age) values(?,?)'
try:
    cur.execute(sql, ('张三', 23))
    # 提交事务
    con.commit()
    print('插入成功')
except Exception as e:
    print(e)
    print('插入失败')
    con.rollback()
finally:
    # 关闭游标
    cur.close()
    # 关闭连接
    con.close()
