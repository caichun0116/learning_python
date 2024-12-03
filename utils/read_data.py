import configparser
import os

import yaml

data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "data", "data.yaml")
ini_path = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config", "settings.ini")


class file_path:
    def __init__(self):
        self.config_path = data_path
        self.ini_path = ini_path

    def read_data(self):
        f = open(self.config_path, encoding="utf-8")
        data = yaml.safe_load(f)
        return data

    def read_config_data(self):
        config = configparser.ConfigParser()
        config.read(self.ini_path, encoding='utf8')
        return config


TotalPath = file_path()

if __name__ == '__main__':
    print(TotalPath.read_data())