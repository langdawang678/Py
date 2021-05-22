import pymysql

DATA_CONFIG = dict(
    host="localhost",
    user="root",
    password="mysql",
    database="test",
    port="3306",
    charset="utf8"
)
print(DATA_CONFIG)


class DB(object):
    # 数据库操作的上下文管理器
    def __init__(self, data_config):
        self.con = pymysql.connect(**data_config)
        self.cursor = self.con.cursor()

    def __enter__(self):
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.con.close()


with DB(DATA_CONFIG) as cur:
    cur.execute("SELECT * FROM students")
    print(cur.fetchone())
