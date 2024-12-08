# -*- coding: gbk -*-
from utils.read_data import TotalPath


class AssemblyRequest:
    # 获取体首参数
    def get_ssport_home_request(self):
        return TotalPath.read_data()['sport_home_data']

    # 获取登录参数
    def get_login_request(self):
        return TotalPath.read_data()['login_data']

    # 获取直播参数
    def get_livetab_request(self):
        return TotalPath.read_data()['living_data']

    def get_login_request(self):
        return TotalPath.read_data()['log_pamas']
    def get_login_data(self):
        return TotalPath.read_data()['login_data']
    def get_goods_data(self):
        return TotalPath.read_data()['goods_data']


get_request = AssemblyRequest()
if __name__ == '__main__':
    print(get_request.get_login_data())