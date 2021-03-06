# -- encoding: utf-8 --
# @time:    	2021/1/30 22:41
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		webpage
import win32gui
import win32con
# pip install pywin32
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from python_AppTest.py_appTest_framework2.common.basepage import BasePage
from selenium.webdriver.remote.webdriver import WebDriver
from python_AppTest.py_appTest_framework2.common.logginghandler import logger


class WebPage:
    def __init__(self, driver):
        self.driver = driver
        self.bp = BasePage(self.driver)

    # 窗口切换
    # iframe切换：下标、name属性、元组(find_element)
    def switch_to_iframe(self, loc, img_name, timeout=20, poll_fre=0.5):
        logger.info('{}切换到{}表单'.format(img_name, loc))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency=poll_fre).until(
                EC.frame_to_be_available_and_switch_to_it(loc))
        except:
            self.bp.save_page_shot(img_name)
            logger.exception('{}iframe切换失败'.format(loc))
            raise

    # alert切换
    def switch_to_alert(self, img_name, timeout=30, poll_frequency=0.5, action='accept'):
        logger.info('{0}_切换alert弹框'.format(img_name))
        try:
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            value = alert.text
            logger.info('{0}当前弹框内容为:{1}'.format(img_name, value))
            if action == 'accept':
                alert.accept()
            elif action == 'dismiss':
                alert.dismiss()
            return value
        except:
            logger.exception('{}弹框操作失败！'.format(img_name))
            self.bp.save_page_shot(img_name)
            raise

    # iframe切换
    def switch_to_frame(self, loc, img_name):
        ele = self.bp.find_element(loc, img_name)
        logger.info('{}表单切换'.format(img_name))
        try:
            self.driver.switch_to.frame(ele)
            logger.info('{}切换表单成功'.format(img_name))
        except:
            logger.exception('{}切换表单失败！'.format(img_name))
            self.bp.save_page_shot(img_name)
            raise

    # js执行
    def execute_script(self, js_str, img_name, element_info=None, ):
        logger.info('{}执行js'.format(img_name))
        try:
            if element_info:
                self.driver.execute_script(js_str)
            else:
                self.driver.execute_script(js_str, None)
            logger.info('{}执行js成功'.format(img_name))
        except:
            logger.exception('{}执行js操作失败'.format(img_name))
            BasePage(self.driver).save_page_shot(img_name)
            raise

    # 滚动条操作
    def scrollbal_handle(self,url,img_name,mode='foot'):
        global js
        logger.info('{}进行滚动条操作'.format(img_name))
        try:
            self.driver.get(url)
            if mode=='top':
                # 滚动到顶部
                js = "window.scrollTo(0,0)"
                self.driver.execute_script(js)
            else:
                # 滚动到底部
                js = "window.scrollTo(0,document.body.scrollHeight)"
                self.driver.execute_script(js)
            logger.info('{}滚动成功'.format(img_name))
        except:
            logger.exception('{}滚动操作失败'.format(img_name))
            self.bp.save_page_shot(img_name)
            raise
    # 切换窗口
    def switch_to_window(self, window_reference, img_name, timeout=30, poll_frequency=0.5, window_handles=None):
        logger.info("{0}_切换窗口".format(img_name))
        try:
            if window_reference == "new":
                if window_handles:
                    WebDriverWait(timeout, poll_frequency).until(EC.new_window_is_opened(window_handles))
                    current_window_handles = self.driver.window_handles
                    self.driver.switch_to.window(current_window_handles[-1])
                else:
                    logger.exception("打开新窗口时，请传入window_handles参数")
                    raise ("打开新窗口时，请传入window_handles参数")
            elif window_reference == "default":
                self.driver.switch_to.default_content()
            else:
                self.driver.switch_to.window(window_reference)
            logger.info("{0}_切换窗口成功".format(img_name))
        except:
            logger.exception("{0}_切换窗口失败".format(img_name))
            BasePage(self.driver).save_page_shot(img_name)
            raise

    # 获取当前url
    def get_current_url(self):
        pass

    # 上传
    def upload_file(self, UpfilePath, img_name):
        logger.info('{}进行文件上传'.format(img_name))
        try:
            dialog = win32gui.FindWindow('#32770', '打开')  # 一级
            # 二级窗口
            ComBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComBoxEx32', None)
            # 三级窗口
            ComboBox = win32gui.FindWindowEx(ComBoxEx32, 0, 'ComboBox', None)
            # 四级窗口
            edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
            button = win32gui.FindWindowEx(dialog, 0, 'Button', "打开(&0)")

            # 操作
            # 输入文件地址
            win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, UpfilePath)  # 发送文件路径
            # 打开文件按钮
            win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮
            logger.info('{}文件上传成功'.format(img_name))
        except:
            logger.exception('{}文件上传操作失败'.format(img_name))
            self.bp.save_page_shot(img_name)
            raise


if __name__ == '__main__':
    pass
