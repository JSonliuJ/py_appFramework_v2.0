# -- encoding: utf-8 --
# @time:    	2021/1/31 10:35
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		indexPage_locator
from  appium.webdriver.common.mobileby import MobileBy as MB
class IndexPageLocator:
    # 搜索按钮
    click_search_button = (MB.XPATH, '//*[contains(@resource-id,"searchWidget")]//*[@text="搜索"]' )
    # 搜索输入框
    search_stock_or_fund = (MB.XPATH, '//*[@text="搜索"]/../..//*[@resource-id="com.hundsun.winner.pazq:id/edit_search"]')