# -*- coding: gbk -*-
import requests
from six import get_function_code

from aip.query_code import query_code
from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger
from utils.read_data import TotalPath


# ���URL�������˶���ҳ��������Ϸ����
# url = TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"
def test_send_code():

    url = get_url.get_login_url()
    param = get_request.get_login_request()
    # �������󲢽�����Ӧ���
    #logger.info(f"url��ַΪ��{url}��param����Ϊ��{param}")
    res = get_tmethod.Requestmethod_post(url, json=param)
    #logger.info(f"��{res}")
    # ��ӡ��Ӧ���
    #assert res.success is True
    print(res['mobile'])
    #��ȡ�˺�
    mobile=res['mobile']
    return mobile


if __name__ == '__main__':
    test_send_code()