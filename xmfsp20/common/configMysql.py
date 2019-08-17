import pymysql
import configparser
'''
@author:xiakongkong
'''

class MSSQL:
    def __init__(self):  # 类的构造函数，读配置文件中的配置信息，初始化数据库连接ip或者域名，以及用户名，密码，要连接的数据库名称，
        config = configparser.ConfigParser()
        config.read('../config/config.ini')
        self.host = config.get("DATABASE","host")
        self.user = config.get("DATABASE","user")
        self.port = int(config.get("DATABASE","port"))
        self.pwd = config.get("DATABASE","passwd")
        self.db = config.get("DATABASE","database")

    # 得到数据库连接信息函数， 返回: conn.cursor()
    def GetConnect(self):

        self.conn = pymysql.connect(host=self.host,port=self.port ,user=self.user, password=self.pwd, database=self.db, charset='utf8')
        # 将数据库连接信息，赋值给cur。
        cur = self.conn.cursor()
        if not cur:
            raise (NameError, "连接数据库失败")
        else:
            print("连接数据库成功")
            return cur

    # 执行查询语句,返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    def ExecQuery(self,sql):  # 执行Sql语句函数，返回结果
        cur = self.GetConnect()  # 获得数据库连接信息
        cur.execute(sql)  # 执行Sql语句
        resList = cur.fetchall()  # 获得所有的查询结果
        # 查询完毕后必须关闭连接
        self.conn.close()  # 返回查询结果
        return resList

    def ExecNonQuery(self, sql):
        cur = self.GetConnect()
        cur.execute(sql)
        self.conn.commit()
        self.conn.close()
if __name__ == '__main__':
    a = MSSQL()
    sql = "select * from dsbs_apply_info_temp where dsbs_apply_no = '20180327015829972687996596224' ;"
    b=a.ExecQuery(sql)
    print(b)