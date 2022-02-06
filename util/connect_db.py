import pymysql.cursors
import json
import configparser

# conn = pymysql.connect(
#     host = 'localhost',
#     port =3306,
#     user = 'root',
#     passwd = 'root',
#     db ='test',
#     charset = 'utf8'
# )
# cur = conn.cursor()
# cur.execute("select * from students ")
# s = cur.fetchall()
# print(s)

class OperationMysql():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(r'C:\untitled2\config\setting.ini',encoding='utf-8')
        self.conn = pymysql.connect(
            host = config.get('mysql', 'host'),
            port = config.getint('mysql', 'port'),
            user = config.get('mysql', 'user'),
            passwd = config.get('mysql', 'passwd'),
            db = config.get('mysql', 'db'),
            charset = config.get('mysql', 'charset'),
            cursorclass = pymysql.cursors.DictCursor
            #     host = 'localhost',
            #     port =3306,
            #     user = 'root',
            #     passwd = 'root',
            #     db ='test',
            #     charset = 'utf8'
            )
        self.curr = self.conn.cursor()


    #单条查询、多条查询
    def query(self,sql):
        s = self.curr.execute(sql)
        # print(s)
        for i in range(0,s):
            # print(self.cur.fetchone())
            # print(type(self.cur.fetchone()))
            result = self.curr.fetchone()
            result = json.dumps(result,ensure_ascii=False)
            print(result)
        # print('result',type(result))
        return result


    #修改、新增、删除
    def update_add_delete(self,sql):
        # 执行sql语句
        self.curr.execute(sql)
        self.curr.fetchone()
        # 提交
        self.conn.commit()
        # 关闭游标
        # self.curr.close()
        # 关闭连接
        # self.conn.close()

if __name__ == '__main__':
    op_mysql = OperationMysql()
    op_mysql.query("select * from cname ")
    # op_mysql.update_add_delete("update cname set Cname = '123' where id= 001 ")





















