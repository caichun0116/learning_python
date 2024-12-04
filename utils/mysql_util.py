import pymysql

from utils.log_utils import logger
from utils.read_data import TotalPath

# 从配置文件中读取MySQL数据库的配置信息
data = TotalPath.read_config_data()['mysql']
# 构建MySQL数据库连接配置字典
DB_CONF = {
    "host": data['MYSQL_HOST'],
    "port": int(data['MYSQL_PORT']),
    "user": data['MYSQL_USER'],
    "password": data['MYSQL_PASSWD'],
    "db": data['MYSQL_DB']
}


class MysqlDb:
    """
    MySQL数据库操作类
    """
    def __init__(self):
        # mysql连接
        self.conn = pymysql.connect(**DB_CONF, autocommit=True)
        self.cur = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    # 释放资源
    def __del__(self):
        self.cur.close()
        self.conn.close()

    # 查询一条
    def select_db_one(self, sql):
        """
        执行SQL查询语句，返回一条数据
        :param sql: SQL查询语句
        :return: 查询结果，一条数据
        """
        logger.info(f'执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchone()
        logger.info(f'sql执行结果：{result}')
        return result

    # 查询多条
    def select_db_all(self, sql):
        """
        执行SQL查询语句，返回多条数据
        :param sql: SQL查询语句
        :return: 查询结果，多条数据
        """
        logger.info(f'sql执行sql：{sql}')
        self.cur.execute(sql)
        # 获取数据
        result = self.cur.fetchall()
        logger.info(f'执行结果：{result}')
        return result

    def execute_db(self, sql):
        """
        执行SQL语句，用于增删改操作
        :param sql: SQL语句
        """
        try:
            logger.info(f'执行sql：{sql}')
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            logger.info("执行sql出错{}".format(e))


# 实例化数据库操作对象
db = MysqlDb()
if __name__ == '__main__':
    # 实例化数据库操作对象
    db = MysqlDb()
    # 执行SQL查询一条数据，并打印结果
    result = db.select_db_one(
        "select code from users_verifycode where mobile = '15000000000' order by id desc limit 1;")
    print(result['code'])
