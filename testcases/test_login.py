# -*- coding: gbk -*-

from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger
from utils.read_data import TotalPath


# ���URL�������˶���ҳ��������Ϸ����
# url = TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"


def test_api_login():

    url = get_url.get_login_url()
    # ��ȡ��������ҳ���ݵĲ���
    param = get_request.get_login_request()
    # �������󲢽�����Ӧ���
    logger.info(f"url��ַΪ��{url}��param����Ϊ��{param}")
    res = get_tmethod.Requestmethod_post(url, param)
    logger.info(f"�������ݣ�{res}")
    # ��ӡ��Ӧ���


# ����ģ����Ϊ��ģ��ִ��ʱ������Sportshom����
if __name__ == '__main__':
    test_api_login()