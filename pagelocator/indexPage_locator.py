# -- encoding: utf-8 --
# @time:    	2021/1/31 10:35
# @Author: 		jsonLiu
# @Email:  		810030709@qq.com
# @file: 		indexPage_locator
from  appium.webdriver.common.mobileby import MobileBy as MB
class IndexPageLocator:
    # 导航栏
    #主页
    home_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_home" )
    # 题库
    tiku_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_tiku")
    #我的柠檬
    my_nav_loc = (MB.ID, "com.lemon.lemonban:id/navigation_my")