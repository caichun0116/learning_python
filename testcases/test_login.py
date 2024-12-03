# -*- coding: gbk -*-

from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger
from utils.read_data import TotalPath


# 组合URL以请求运动首页的热门游戏数据
# url = TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"


def test_api_login():

    url = get_url.get_login_url()
    # 读取爱奇艺首页数据的参数
    param = get_request.get_login_request()
    # 发送请求并接收响应结果
    logger.info(f"url地址为：{url}，param内容为：{param}")
    res = get_tmethod.Requestmethod_post(url, param)
    logger.info(f"报错内容：{res}")
    # 打印响应结果


# 当本模块作为主模块执行时，调用Sportshom函数
if __name__ == '__main__':
    test_api_login()