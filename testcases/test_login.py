# 导入登录所需的数据
import pytest

from aip.login_data import login_data
# 导入请求方法工具类
from utils.Request_method import get_tmethod
# 导入日志工具类
from utils.log_utils import logger

# 定义测试登录的类
class TestLogin:


    def test_login(self):
        # 获取登录的URL和数据
        url, data = login_data()
        try:
            # 发送POST请求并获取结果
            result = get_tmethod.Requestmethod_post(url=url, json=data)
            # 记录登录结果的日志
            logger.info(f"login_result:{result}")
        except Exception as e:
            # 记录登录错误的日志
            #
            logger.error(f"login_error:{e}")

# 创建TestLogin类的实例
login = TestLogin()
# 如果是主模块，执行登录测试
if __name__ == '__main__':
    login.test_login()
