from utils.log_utils import logger
from utils.mysql_util import MysqlDb, db


def query_code(mobile):
    sql= "select  * from users_verifycode where mobile='%s' order by id desc LIMIT 1" %mobile
    result = db.select_db_one(sql)
    return result['code']
    #print(result)
#删除用户
def delete_code(mobile):
    sql= "DELETE FROM users_userprofile where mobile='%s'" %mobile

    result=db.execute_db(sql)
    logger.info(f'sql 执行结果为：{result}')
if __name__ == '__main__':
    delete_code(18000000003)
