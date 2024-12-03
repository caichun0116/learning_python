import os
import pytest
import requests

from utils.log_utils import LogUtils

logger = LogUtils().get_log()


def test_get_params():
    logger.info("开始测试get请求数据")
    url = "http://api.binstd.com/shouji/query"
    appkey = os.getenv("APPKEY", "0c818521d38759e1")  # 从环境变量中获取appkey
    params = {"shouji": "13399999999", "appkey": appkey}

    try:
        response = requests.get(url, params=params, timeout=10)  # 添加超时时间
        response.raise_for_status()  # 检查HTTP响应状态
    except requests.RequestException as e:
        logger.error(f"请求失败: {e}, URL: {url}, Params: {params}")
        pytest.fail("请求失败")
    else:
        logger.debug(f"响应数据: {response.json()}")
        logger.debug(f"状态码: {response.status_code}")
        result = response.json()
        assert response.status_code == 200  # 修改为正确的状态码
        logger.error(f"状态码不匹配: {response.status_code}, URL: {url}, Params: {params}")
        assert result["status"] == 0, "状态码不为0"
        assert result["msg"] == "ok", "消息不为'ok'"
        assert result["result"]["shouji"] == "13399999999", "手机号码不匹配"
        assert result["result"]["cardtype"] is None, "卡类型不为空"


if __name__ == '__main__':
    pytest.main()
