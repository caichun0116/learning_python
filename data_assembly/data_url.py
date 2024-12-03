# -*- coding: gbk -*-
from utils.read_data import TotalPath


class AssemblyURL:

    # 获取体首页url
    def get_ssport_home_url(self, **kwargs):
        return TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"

    # 获取登录url
    def get_login_url(self, **kwargs):
        return TotalPath.read_config_data()['host']['api_sit_url'] + "/apis/reglogin/mobile_login.action"

    # 获取 直播中url
    def get_livetab_url(self, **kwargs):
        return TotalPath.read_config_data()['host']['living_sit_url'] + "/match/global/livingMatchList"

    def get_login_url(self, **kwargs):
        return TotalPath.read_config_data()['host']['login_sit_url'] + '/code/'

get_url = AssemblyURL()
if __name__ == '__main__':
    print(get_url.get_login_url())