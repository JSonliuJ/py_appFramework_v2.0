# -- encoding: utf-8 --
# @time:    	2021/1/31 12:37
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		conftest
"""
# npm -命令行安装appium -无界面-命令行参数
# desktop

#命令行启动desktop的appium
C: \Program Files \Appium\resources \app \node_ modules \app ium\build\lib>
node main.js            ---启动appium
node main.js --help    查看启动参数
# 1. appium server要是启动状态    用例结束之后，关闭服务。
# 2、检测一下是否有设备连接。如果没有呢，用例不执行。如果有呢，就获取版本号。
    adb devices -- 希望通过代码去执行adb devices命令。 从结果当中，来判断是否有设备连接。.
        用python去执行adb devices , 要获取命令执行后输出结果? --
    获取设备版本号：appium server日志，
# 3. 多设备并发
  - 多线程
  - pytest：pytest-xdist和pytest-parallel
  - grid
"""
import os

import pytest
import yaml
from appium import webdriver
from common.filehandler import FileHandler


@pytest.fixture()
def login_app(init):
    driver = init()


# 启动appium会话
def init(port=4723, **kwargs):
    with open(os.path.join(FileHandler.config_path,'config.yaml'), encoding='utf-8') as fs:
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
        # yaml.safe_load(fs)
    for key, value in kwargs.items():
        desired_caps[key] = value

    fs.close()
    print(desired_caps)
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(port), desired_caps)
    return driver


if __name__ == '__main__':
    init()
