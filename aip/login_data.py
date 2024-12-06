# -*- coding: gbk -*-

from aip.query_code import query_code
from data_assembly.data_request import get_request
from data_assembly.data_url import get_url


def login_data():
    mobile = mobile=get_request.get_login_request()['mobile']
    url = get_url.get_pytest_login1_url()
    parms = {
            "mobile":mobile,
            "code":query_code(mobile),
            "password": 123456,
            "username": mobile
    }
    return url,parms
#print(login_data())