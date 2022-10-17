# -- encoding: utf-8 --
# @time:    	2021/1/30 22:41
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		apppage
import time

from selenium.webdriver import ActionChains

from common.basepage import BasePage
from appium.webdriver import Remote
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.actions.mouse_button import MouseButton
from common.logginghandler import logger


class AppPage:
    def __init__(self, driver: Remote):
        self.driver = driver
        self.bp = BasePage(self.driver)

    def get_device_size(self):
        logger.info('获取设备大小')
        try:
            size = self.driver.get_window_size()
        except:
            logger.error('获取屏幕尺寸失败')
            BasePage(self.driver).save_page_shot(img_name='get_size_files')
            raise
        else:
            return size

    # 滑屏操作：上下左右
    def swipe_by_direction(self, direction, img, duration=200):
        size = self.get_device_size()
        logger.info('在{}的进行{}操作'.format(img, direction))
        try:
            if direction.lower() == 'up':
                self.driver.swipe(size['width'] * 0.5, size['height'] * 0.9, size['width'] * 0.5, size['height'] * 0.2,
                                  duration)
            elif direction.lower() == 'down':
                self.driver.swipe(size['width'] * 0.5, size['height'] * 0.2, size['width'] * 0.5, size['height'] * 0.9,
                                  duration)
            elif direction.lower() == 'left':
                self.driver.swipe(size['width'] * 0.9, size['height'] * 0.5, size['width'] * 0.2, size['height'] * 0.5,
                                  duration)
            elif direction.lower() == 'right':
                self.driver.swipe(size['width'] * 0.2, size['height'] * 0.5, size['width'] * 0.9, size['height'] * 0.5,
                                  duration)
        except:
            logger.error('{}滑屏操作失败'.format(img))
            BasePage(self.driver).save_page_shot(img)
            raise

    # 列表滑动 - 找文本/找元素/向上/向下
    def list_swipe(self, ele, direction, img, t=3):
        global new, old
        while (old != new):
            try:
                self.driver.find_element_by_android_uiautomator(ele)
            except:
                self.swipe_by_direction(direction, img)
                time.sleep(t)
                old = new
                new = self.driver.page_source
            else:
                logger.info('找到了{}'.format(ele))
                break

    # toast获取
    def get_toast(self, text, img_name, timeout=10, poll_fre=0.01):
        loc = (MobileBy.XPATH,'//android.widget.Toast') # 方式1
        # loc = (MobileBy.XPATH, '//*[contains(@text(),"{}")]'.format(text)) # 方式2
        logger.info('获取toast提示信息，toast元素为：{}'.format(loc))
        # 等待元素存在并获取文本内容
        self.bp.wait_element_exist(loc, img_name, timeout, poll_fre)
        ele = self.bp.find_element(loc, img_name)
        logger.info('在{}获取{}的toast'.format(img_name, text))
        try:
            text = ele.text
        except:
            self.bp.save_page_shot(img_name)
            logger.exception('获取{}的toast失败'.format(text))
            raise
        else:
            return text
    # 应用切换
    def switch_application(self,package_name,activity_name):
        logger.info('切换到{}应用'.format(package_name))
        self.driver.start_activity(package_name,activity_name)

    # 混合应用-获取所有的，然后切换，webview的名称
    def switch_multi_app(self,loc,img_name,t=2):
        """
        1)开启调试模式
        2）获取当前contexts
        3）切换到webview(即html)页面中去
        4)操作html页面(同web)
        """
        # loc采用UiSelector
        self.bp.click_element(loc,img_name)
        loc = (MobileBy.CLASS_NAME, 'android.webkit.WebView')
        time.sleep(t)
        cons = self.driver.contexts
        logger.info('所有上下文：{}'.format(cons))
        try:
            self.driver.switch_to.context(cons[-1])
        except:
            logger.exception('切换到{}失败'.format(loc))
            self.bp.save_page_shot(img_name)
            raise

    def zoom(self, step=0.5, duration=None):
        # 放大
        """
        :param step:
        :param duration: 停顿时间
        :return:
        """
        actions = ActionChains(self.driver)
        actions.w3c_actions.devices = []
        finger1 = actions.w3c_actions.add_pointer_input('touch', f'finger1')
        finger2 = actions.w3c_actions.add_pointer_input('touch', f'finger2')

        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        for finger in [finger1, finger2]:
            finger.create_pointer_move(x=width * 0.5, y=height * 0.5)
            finger.create_pointer_down(MouseButton.LEFT)
            if duration:
                finger.create_pause(duration / 1000)
            else:
                finger.create_pause(0.1)

        finger1.create_pointer_move(x=width * 0.5, y=height * (0.5 + step / 2))
        finger2.create_pointer_move(x=width * 0.5, y=height * (0.5 - step / 2))

        finger1.create_pointer_up(MouseButton.LEFT)
        finger2.create_pointer_up(MouseButton.LEFT)

        actions.perform()

    def pitch(self, step=0.5, duration=None):
        # 缩小
        """
        :param step:
        :param duration:
        :return:
        """
        actions = ActionChains(self.driver)
        actions.w3c_actions.devices = []
        # 1、使用add_point_input添加手指，放大需要用到两个手指。
        finger1 = actions.w3c_actions.add_pointer_input('touch', f'finger1')
        finger2 = actions.w3c_actions.add_pointer_input('touch', f'finger2')

        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        # 2、使用create_pointer_move移动到屏幕的正中间
        finger1.create_pointer_move(x=width * 0.5, y=height * (0.5 + step / 2))
        finger2.create_pointer_move(x=width * 0.5, y=height * (0.5 - step / 2))
        # 3、使用create_pointer_down按下手指
        for finger in [finger1, finger2]:
            finger.create_pointer_down(MouseButton.LEFT)
            if duration:
                finger.create_pause(duration / 1000)
            else:
                finger.create_pause(0.1)
            # 4、使用create_pointer_move往屏幕相反方向移动
            finger.create_pointer_move(x=width * 0.5, y=height * 0.5)
            # 5、使用create_pointer_up松开手指
            finger.create_pointer_up(MouseButton.LEFT)

        actions.perform()
        
    def press_enter(self):
        """回车"""
        self.driver.press_keycode(66)
    # 微信小程序/公众号

if __name__ == '__main__':
    pass
