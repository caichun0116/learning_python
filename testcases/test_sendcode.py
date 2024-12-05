# -*- coding: gbk -*-

from aip.query_code import query_code
from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod


class TestLogin:
    def test_login(self):
        #获取手机号
        url=get_url.get_pytest_login_url()
        json_data=get_request.get_login_request()
        #点击发送验证码
        result=get_tmethod.Requestmethod_post(url,json=json_data)
        print(f'发送验证码结果为:{result}')
        mobile=get_request.get_login_request()['mobile']
        code=query_code(mobile)
        print(code)
        #登录
        url=get_url.get_pytest_login1_url()
        parameters={
            "mobile":mobile,
            "code":code,
            "password": 123456,
            "username": mobile

        }
        result=get_tmethod.Requestmethod_post(url,json=parameters)
        print(f'登录返回结果为:{result}')
if __name__ == '__main__':
    test_login=TestLogin()
    test_login.test_login()
