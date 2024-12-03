import requests

from data_assembly.data_url import get_url
from utils.read_data import TotalPath


# header={"Content-Type":"application/x-www-form-urlencoded","user-Agent":"iQiYiPhoneVideo/20241127103150 CFNetwork/1568.100.1.2.1 Darwin/24.0.0"}
class RequesTmethod:
    def Requestmethod_get(self, url, param, **kwargs):
        req = requests.get(url,
                           params=param, **kwargs)
        result = req.json()
        return result

    def Requestmethod_post(self, url, param=None, json=None,):
        req = requests.post(url,
                            params=param, json=json)
        result = req.json()
        return result


get_tmethod = RequesTmethod()
if __name__ == '__main__':
    param = TotalPath.read_data()['log_pamas']
    url=get_url.get_login_url()
    print(get_tmethod.Requestmethod_post(url, json=param))