from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger


def test_send_code():
    '''
    发送验证码操作
    :return:
    '''
    # 1. 获取发送验证码的 URL
    url = get_url.get_pytest_login_url()
    # 3. 获取请求体
    json_data=get_request.get_login_request()
    # 4. 发送请求
    try:
        result = get_tmethod.Requestmethod_post(url, json=json_data)
        logger.info(f"请求结果: {result}")
        return get_request.get_login_request()['mobile']
    except Exception as e:
        logger.error(f"请求出现异常: {e}")



