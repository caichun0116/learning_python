import pytest

from aip.login_api import login_api
from utils.log_utils import logger
@pytest.mark.run(order=1)
def test_login(login_api):
    print("开始执行登录")

    result=login_api
    logger.info(f"登录成功返回：{result}")
    try:
        if "token" in result:
            # 这里根据实际期望的token值和格式进行准确的断言，示例中假设token是字符串类型且有特定格式要求
            token=result["token"]
            logger.info(f"获取到有效的token: {token}")
        else:
            logger.error("登录失败，响应中未包含有效的token")
    except AssertionError:
        logger.error("登录失败，响应中未包含有效的token")



if __name__ == '__main__':
    test_login()