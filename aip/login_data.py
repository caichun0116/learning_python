# -*- coding: gbk -*-
from aip.query_code import query_code
from aip.login_Information import test_send_code
from data_assembly.data_url import get_url
from utils.log_utils import logger


def login_data():
    #发送验证码
    mobile=test_send_code()
    url = get_url.get_pytest_login1_url()
    parms = {
            "mobile":mobile,
            "code":query_code(mobile),
            "password": 123456,
            "username": mobile
    }
    logger.info(f"返回参数：{url,parms}" )
    return url,parms
#print(login_data())