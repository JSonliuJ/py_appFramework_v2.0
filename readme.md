## 01app框架
1. basepage 扩展
 - 获取设备大小
 - 滑屏操作 - 上下左右
 - 列表滑动 - 找文本/找元素/向上/向下
 - toast获取
 - 混合应用-获取所有的，然后切换，webview的名称
 - 微信小程序/公众号
2. pageObject
3. pageLoctor
4. testCases
5. outputs
 - screenshots
 - reports
   - html_report
   - allure_report 
 - logs
6. run.py
7. 启动会话
 - web：driver = webdriver.Chrome()
 - app:
```
automationName = UiAutomator2 .
platformName = 
platformVersion = 
deviceName =  
appPackage=
appActivity = 
noReset = True
chromdriverExecutable = 
unicodeKeyboard = 
ChromeOption
```
8. 配置功能：py、yaml、ini
## 02 docker+jenkins搭建自动化用例
**1.** 安装jenkins：
```
docker run -dit --name=mmmm_jenkins  \ 
-p 8000:8080  \ 
-u=root -v /var/run/docker.sock:/var/run/docker.sock  \ 
-v /usr/bin/docker:/usr/bin/docker 
jenkins/jenkins
```
**2.** 创建Dockerfile文件
```
FROM python:3.8
COPY . .
RUN pip3 install -r requirements.txt
CMD [ "python3", "run.py"]
```

**3.** jenkins构建任务,shell执行脚本
```
docker build --tag 容器名 .
docker run 容器名
docker rmi 容器名
```
## 03小程序/公众号 测试
- 连接真机：开启usb调式模式，
- 打开x5内核调试模式：http://debugmm.qq.com/?forcex5=true
- mumu模拟器显示真机屏幕

