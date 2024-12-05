import pytest
@pytest.mark.parametrize('key',['黄种','anqila'])
def test_parametrize_01(key):
    print(key)