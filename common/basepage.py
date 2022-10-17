# -- encoding: utf-8 --
# @time:    	2021/1/26 22:55
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		basepage
import datetime
import time
import os
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from common.filehandler import FileHandler
from common.logginghandler import logger


# 记录日志/失败截图+错误信息输出+抛出异常
class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待可见
    def wait_ele_visible(self, loc, img_name, timeout=20, poll_fre=0.5):
        global end
        logger.info('{}等待{}元素可见'.format(img_name, loc))
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            logger.info('等待元素可见开始时间：{}'.format(start))
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.visibility_of_element_located(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception('等待{}元素可见失败'.format(loc))
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logger.info('等待元素可见结束时间：{}'.format(end))
        wait_times = (end - start).seconds
        logger.info('总共等待时长:{}'.format(wait_times))

    def wait_element_exist(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 等待元素存在
        global end
        logger.info('{}等待{}元素存在'.format(img_name, loc))
        # 开始等待时间
        start = datetime.datetime.now()
        try:
            logger.info('等待元素存在开始时间：{}'.format(start))
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.presence_of_element_located(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception('等待{}元素存在失败'.format(loc))
            raise

        else:
            # 结束等待时间
            end = datetime.datetime.now()
            logger.info('等待元素存在结束时间：{}'.format(end))
        wait_times = (end - start).seconds
        logger.info('总共等待时长:{}'.format(wait_times))

    def wait_ele_clickable(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 等待元素可点击
        logger.info('{}等待{}元素可点击'.format(img_name, loc))
        # 开始等待时间
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(EC.element_to_be_clickable(loc))
        except:
            self.save_page_shot(img_name)
            logger.exception('等待{}元素可点击失败'.format(loc))
            raise

    def find_element(self, loc, img_name):
        # 查找元素
        self.wait_ele_visible(loc, img_name)
        logger.info('在{}查找{}元素'.format(img_name, loc))
        try:
            ele = self.driver.find_element(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception('查找{}失败'.format(loc))
            raise
        else:
            return ele

    def find_elements(self, loc, img_name):
        # 查找所有元素
        self.wait_ele_visible(loc, img_name)
        logger.info('{}查找{}所有元素'.format(img_name, loc))  # img_name 页面名称_模块名称
        try:
            ele = self.driver.find_elements(*loc)
        except:
            self.save_page_shot(img_name)
            logger.exception('查找{}所有元素失败'.format(loc))
            raise
        else:
            return ele

    def click_element(self, loc, img_name, timeout=20, poll_fre=0.5):
        # 点击元素
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)  # 必然前提1
        ele = self.find_element(loc, img_name)  # 必然前提2
        logger.info('在{}点击{}元素'.format(img_name, loc))
        try:
            ele.click()
        except:
            self.save_page_shot(img_name)
            logger.exception('点击元素失败')
            raise

    # 输入文本
    def input_text(self, value, loc, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.find_element(loc, img_name)
        logger.info('在{}往元素{}输入文本值：{}'.format(img_name, loc, value))
        try:
            ele.send_keys(value)
        except:
            self.save_page_shot(img_name)
            logger.exception('输入文本失败')
            raise

    # 获取元素属性
    def get_ele_attribute(self, loc, attribute_name, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.find_element(loc, img_name)
        logger.info('{}点击{}'.format(img_name, loc))
        try:
            attr = ele.get_attribute(attribute_name)
        except:
            self.save_page_shot(img_name)
            logger.exception('获取{}属性失败'.format(loc))
            raise
        else:
            return attr

    # 获取元素文本
    def get_ele_text(self, loc, img_name, timeout=20, poll_fre=0.5):
        self.wait_ele_visible(loc, img_name, timeout, poll_fre)
        ele = self.find_element(loc, img_name)
        logger.info('{}获取{}元素文本'.format(img_name, loc))
        try:
            text = ele.text
        except:
            self.save_page_shot(img_name)
            logger.exception('获取{}文本失败'.format(loc))
            raise
        else:
            return text

    # 保存截图
    def save_page_shot(self, img_name):
        # 命名规范：(页面名称_页面行为)_时间.png
        now_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        # time.strftime("%Y%m%d_%H%M%S", time.localtime())
        # time.strftime("%Y%m%d_%H%M%S", time.localtime(time.time()))
        file_name = '{}_{}.png'.format(img_name, now_time)
        # 保存位置：图片路径 + 文件名
        file = os.path.join(FileHandler.screenshot_path, file_name)
        self.driver.save_screenshot(file)
        logger.info('图片保存在：'.format(file))


if __name__ == '__main__':
    pass
