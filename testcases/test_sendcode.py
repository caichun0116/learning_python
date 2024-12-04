# -*- coding: gbk -*-


from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod


# 组合URL以请求运动首页的热门游戏数据
# url = TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"
def test_send_code():

    url = get_url.get_login_url()
    param = get_request.get_login_request()
    # 发送请求并接收响应结果
    #logger.info(f"url地址为：{url}，param内容为：{param}")
    res = get_tmethod.Requestmethod_post(url, json=param)
    #logger.info(f"：{res}")
    # 打印响应结果
    #assert res.success is True
    print(res['mobile'])
    #获取账号
    mobile=res['mobile']
    return mobile


if __name__ == '__main__':
    test_send_code()