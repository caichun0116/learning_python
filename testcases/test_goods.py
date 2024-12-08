import os

from data_assembly.data_request import get_request
from aip.login_api import login_api
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger
def test_get_login_data(login_api):
    url =get_url.get_pytest_goods_url()
    param=get_request.get_goods_data()
    token=login_api
    logger.info(f'token为：{token}')
    headers ={
        "Authorization": "JWT " + token['token']
    }
    print(logger.info(f'headers接口请求参数为：{headers}'))
    result=get_tmethod.Requestmethod_post(url,json=param,headers=headers)
    logger.info(f'商品列表接口返回结果为：{result}')





def test_get_login_data2(login_api):
    url = get_url.get_pytest_goods_url()
    param = get_request.get_goods_data()
    token = login_api
    logger.info(f'token为：{token}')
    headers = {
        "Authorization": "JWT " + token['token']
    }
    logger.info(f'headers接口请求参数为：{headers}')
    result = get_tmethod.Requestmethod_post(url, json=param, headers=headers)
    logger.info(f'商品列表接口返回结果为：{result}')

if __name__ == '__main__':
    test_get_login_data()
    test_get_login_data2()