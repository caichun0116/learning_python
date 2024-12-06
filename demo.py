以下是将上述代码按照功能封装到不同文件的示例结构，这样可以使代码的组织结构更加清晰，便于维护和扩展。
1. test_login.py（测试主文件）
这个文件主要用于定义测试类以及组织整个登录测试的流程，它会调用其他模块中封装好的功能函数来实现完整的测试逻辑。
python
复制
# -*- coding: gbk -*-
from utils.Request_method import get_tmethod
from data_assembly import data_url, data_request
from aip import query_code


class TestLogin:
    def __init__(self):
        """
        初始化测试类，可在这里进行一些通用的初始化操作（目前暂未添加额外初始化内容）
        """
        pass

    def test_login(self):
        """
        完整的登录测试流程
        """
        # 获取发送验证码的URL和请求数据
        send_code_url, send_code_json = data_url.get_send_verification_code_url()
        if send_code_url and send_code_json:
            # 发送验证码
            send_code_result = get_tmethod.Requestmethod_post(send_code_url, json=send_code_json)
            print(f'发送验证码结果为: {send_code_result}')

            if send_code_result:
                mobile = data_request.get_mobile_number()
                code = query_code.get_verification_code(mobile)
                if code:
                    # 获取登录的URL和请求数据
                    login_url, login_json = data_url.get_login_url(mobile, code)
                    if login_url and login_json:
                        # 执行登录操作
                        login_result = get_tmethod.Requestmethod_post(login_url, json=login_json)
                        print(f'登录返回结果为: {login_result}')


if __name__ == '__main__':
    test_login = TestLogin()
    test_login.test_login()
2. data_assembly/data_url.py（负责获取相关 URL 的模块）
这个模块主要封装了获取发送验证码以及登录操作相关 URL 的函数，将与 URL 获取相关的逻辑集中到这里。
python
复制
def get_send_verification_code_url():
    """
    获取发送验证码的URL
    :return: 发送验证码的URL
    """
    return get_pytest_login_url()

def get_login_url(mobile, code):
    """
    获取登录的URL，并根据手机号和验证码构建登录相关参数
    :param mobile: 手机号
    :param code: 验证码
    :return: tuple，包含登录的URL和对应的JSON请求数据
    """
    url = get_pytest_login1_url()
    parameters = {
        "mobile": mobile,
        "code": code,
        "password": 123456,
        "username": mobile
    }
    return url, parameters

# 以下两个函数假设是在原 data_url 模块中已定义好的，用于获取具体的URL，这里只是示意其调用关系
def get_pytest_login_url():
    # 实际实现获取发送验证码URL的逻辑，比如从配置文件读取或者硬编码等方式
    pass

def get_pytest_login1_url():
    # 实际实现获取登录URL的逻辑
    pass
3. data_assembly/data_request.py（负责获取请求相关数据的模块）
在这里封装了获取登录相关请求数据以及提取手机号等操作的函数，把和请求数据处理有关的逻辑放在这个模块里。
python
复制
def get_mobile_number():
    """
    获取手机号，从获取登录请求数据中提取手机号字段
    :return: 手机号
    """
    return get_login_request()['mobile']

def get_login_request():
    """
    获取登录请求数据，具体实现可根据实际情况，比如从配置文件构造、模拟生成等
    :return: 登录请求的JSON数据
    """
    # 实际实现获取登录请求数据的逻辑，例如构造符合要求的JSON格式数据
    pass
4. aip/query_code.py（负责查询验证码的模块）
这个模块主要用于实现根据手机号查询验证码的功能，集中处理与验证码查询相关的逻辑。
python
复制
def get_verification_code(mobile):
    """
    根据手机号获取验证码
    :param mobile: 手机号
    :return: 验证码
    """
    try:
        # 实际实现查询验证码的逻辑，可能涉及和相关服务交互等操作
        return query_code(mobile)
    except Exception as e:
        print(f"获取验证码出现异常: {e}")
        return None
5. utils/Request_method.py（负责请求方法封装的模块）
在这里封装了发送 POST 请求的函数，将和 HTTP 请求发送相关的逻辑独立出来，方便其他模块调用。
python
复制
import requests


def Requestmethod_post(url, json=None, param=None, data=None, **kwargs):
    """
    发送POST请求的封装函数
    :param url: 请求的目标URL
    :param json: 请求体中的JSON数据（可选）
    :param param: URL查询参数（可选）
    :param data: 其他形式的请求体数据（可选）
    :param kwargs: 其他额外的请求相关配置关键字参数（可选）
    :return: requests库返回的响应对象
    """
    try:
        req = requests.post(url,
                            json=json, params=param, data=data, **kwargs)
        result = req.json()
        return result
    except Exception as e:
        print(f"请求出现异常: {e}")
        return None
通过这样的文件结构划分，不同功能的代码被封装到各自对应的模块中，每个模块职责更加明确。例如，如果