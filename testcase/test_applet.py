# -- encoding: utf-8 --
# @time:    	2022/10/18 16:53
# @Author: 		JsonLiu
# @Email:  		492224300@qq.com
from appium import webdriver
import time

desired_caps = {}
# 支持X5内核应用自动化配置
desired_caps["recreateChromeDriverSessions"] = True
# android 4.4以下的版本通过Selendroid来切换到webview
desired_caps["automationName"] = "UiAutomator2"
desired_caps["platformName"] = "Android"
desired_caps["deviceName"] = "Android Emulator"
desired_caps["appPackage"] = "com.tencent.mm"
desired_caps["appActivity"] = "com.tencent.mm.ui.LauncherUI"
desired_caps["chromedriverExecutableDir"] = r'D:\data\chromedriver'
desired_caps["noReset"] = True
desired_caps["chromeOptions"] = {"androidProcess": "com.tencent.mm:appbrand0"}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

# wait = WebDriverWait(driver, 30)

# 主页的元素
# loc = (MB.ID, 'com.tencent.mm:id/baj')
# wait.until(EC.visibility_of_element_located(loc))
el = driver.find_element('id', 'com.tencent.mm:id/baj')
size = driver.get_window_size()
el.click()

# 向下滑动
driver.swipe(size["width"] * 0.5, size["height"] * 0.1, size["width"] * 0.5, size["height"] * 0.9, 100)

el = driver.find_element('xpath', '//*[contains(@text, "平安金融")]')
# el = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(locator))
el.click()
time.sleep(3)

# 获取所有的上下文
cons = driver.contexts
print("当前所有的上下文为：", cons)

# 切换到小程序webview
driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')

time.sleep(3)
driver.quit()