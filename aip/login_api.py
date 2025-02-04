# fixture 缓存：
# 1.pytest - cache实现缓存
# 2.cachetools库 缓存
import pytest
from data_assembly.data_request import get_request
from data_assembly.data_url import get_url
from utils.Request_method import get_tmethod
from utils.log_utils import logger
@pytest.fixture(scope='session')
def login_api():
    """
    登录接口
    :param url:
    :param params:
    :return:
    """
    url = get_url.get_xmlogin_url()
    params = get_request.get_login_data()
    logger.info(f'url参数为:{url}')
    logger.info(f'params参数为:{params}')
    result = get_tmethod.Requestmethod_post(url, json=params)
    logger.info(f'打印登录返回结果为:{result}')
    return result  # 明确返回登录请求的结果


# cachetools库 缓存
# from cachetools import cached, TTLCache
# from data_assembly.data_request import get_request
# from data_assembly.data_url import get_url
# from utils.Request_method import get_tmethod
# from utils.log_utils import logger
# import pytest
#
# # 创建一个基于时间的缓存，设置缓存有效期（这里设为3600秒，可根据实际调整）
# cache = TTLCache(maxsize=1, ttl=3600)
#
#
# @pytest.fixture(scope='session')
# @cached(cache)
# def login_api():
#         """
#         登录接口
#         :param url:
#         :param params:
#         :return:
#         """
#         url = get_url.get_xmlogin_url()
#         params = get_request.get_login_data()
#         logger.info(f'url参数为:{url}')
#         logger.info(f'params参数为:{params}')
#         result = get_tmethod.Requestmethod_post(url, json=params)
#         logger.info(f'打印登录返回结果为:{result}')
#         return result

# 使用pytest - cache实现缓存
# import pytest
#
# from data_assembly.data_request import get_request
# from data_assembly.data_url import get_url
# from utils.Request_method import get_tmethod
# from utils.log_utils import logger
#
#
# @pytest.fixture(scope='session')
# def login_api(request: pytest.FixtureRequest):
#         cache = request.config.cache
#         cached_result = cache.get('login_api_result', None)
#         if cached_result is not None:
#                 logger.info("这里是使用缓存的登录结果")
#                 return cached_result
#         else:
#                 url = get_url.get_xmlogin_url()
#                 params = get_request.get_login_data()
#                 logger.info(f'url参数为:{url}')
#                 logger.info(f'params参数为:{params}')
#                 result = get_tmethod.Requestmethod_post(url, json=params)
#                 logger.info(f'打印登录返回结果为:{result}')
#                 cache.set('login_api_result', result)
#                 return result


if __name__ == '__main__':
    login_api()
