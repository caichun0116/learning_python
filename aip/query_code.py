

from utils.mysql_util import MysqlDb


def query_code(mobile):
    sql= "select  * from users_verifycode where mobile='%s' order by id desc LIMIT 1" %mobile
    db = MysqlDb()
    result = db.select_db_one(sql)
    return result['code']
    #print(result)

if __name__ == '__main__':
    query_code(18000001111)
