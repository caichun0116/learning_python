# -*- coding: gbk -*-
from utils.read_data import TotalPath


class AssemblyURL:

    # ��ȡ����ҳurl
    def get_ssport_home_url(self):
        return TotalPath.read_config_data()['host']['cooperation'] + "/gameHot/top/homepage"

    # ��ȡ��¼url
    def get_login_url(self):
        return TotalPath.read_config_data()['host']['api_sit_url'] + "/apis/reglogin/mobile_login.action"

    # ��ȡ ֱ����url
    def get_livetab_url(self):
        return TotalPath.read_config_data()['host']['living_sit_url'] + "/match/global/livingMatchList"

    def get_pytest_login_url(self):
        return TotalPath.read_config_data()['host']['login_sit_url'] + '/code/'

    def get_pytest_login1_url(self):
        return TotalPath.read_config_data()['host']['login_sit_url'] + '/users/'

    def get_xmlogin_url(self):
        return TotalPath.read_config_data()['host']['login_sit_url'] + '/login/'

    def get_pytest_goods_url(self):
        return TotalPath.read_config_data()['host']['login_sit_url'] + '/shopcarts/'


get_url = AssemblyURL()
if __name__ == '__main__':
    print(get_url.get_pytest_login1_url())
