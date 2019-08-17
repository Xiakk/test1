# from appium import webdriver
#
# desired_caps = {
#     'platformName': 'Android',
#     'deviceName': 'E3PBB18406201037',
#     'platformVersion': '8.0',
#     'appPackage': 'com.xinrenlei.koubeigongzuo',
#     'appActivity': 'com.xinrenlei.koubeigongzuo.ui.setup.SplashActivity'
#
# }
#
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
from appium import webdriver
desired_caps = {
   'platformName': 'Android',#移动设备系统IOS或Android
   'platformVersion': '7', #Android手机系统版本号
   'deviceName': 'M960SDTGNRCAB',#手机唯一设备号
   'app': 'C:\\Users\\Administrator\\Desktop\\kbgz-v5.8.0-release.apk',#APP文件路径
   'appPackage': 'com.xinrenlei.koubeigongzuo',#APP包名
   'appActivity': 'com.xinrenlei.koubeigongzuo.ui.setup.SplashActivity',#设置启动的Activity
    'noReset': 'True',#每次运行不重新安装APP
   'unicodeKeyboard': 'True', #是否使用unicode键盘输入，在输入中文字符和unicode字符时设置为true
   'resetKeyboard': 'True'#隐藏键盘
   }
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps) #与appium-server的通信协议
driver.find_element_by_id("com.xinrenlei.koubeigongzuo:id/inputPhone").click()

driver.quit()

'''
import requests
import datetime

'''
获取当前时间
'''
localtime = (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")

# response通过json获取指定的返回值
url = 'http://onsite-api.st1.test.lanxinka.com/1.0/user/login'
url1 = 'http://onsite-api.st1.test.lanxinka.com/1.0/user/order/create'
url2 = 'http://ck-api.st2.test.lanxinka.com/1.0/admin/staff/disable'
url3 = 'http://ck-api.st1.test.lanxinka.com/1.0/admin/user/login'

data1 = {
    "mobile": 14580000001,
    "captcha": 1234,
    "client_type": 2,
    "tn": 1,
    "login_type": 1
}

data2 = {
    "district_name": "金山区",
    "interview_address": "金山北站",
    "interview_address_lat": "30.900587",
    "interview_address_long": "121.095932",
    "interview_time": localtime,
    "job_id": "",
    "orderType": 2,
    "user_address": "南泉北路1021号",
    "user_address_lat": "31.231952",
    "user_address_long": "121.524275"


}


response = requests.request("post", url=url, data=data2).json()
b = response['data']['token']
# print(response)
headers = {
    "Authorization": b
}


response1 = requests.request()

#
# response = requests.request("post", url=url3, data=data1).json()
# b = response['data']['token']
# print(b)

# response = requests.request("get", url=url1, headers=headers).json()
# print(response)
#
# # a = response['data']['0']['id']
# a = response['data']['data'][0]['user_id']
# print(a)
#
# data = {
# "user_id":a
# }
#
# a = requests.request("post", url2, data=data, headers=headers)
# c = a.json()
# print(c)