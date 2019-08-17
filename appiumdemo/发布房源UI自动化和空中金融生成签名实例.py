#!/usr/bin/env python
#_*_coding:utf-8_*_
import time
from appium import webdriver
'''
desired_caps = {						
	'platformName':'Android',						
	'platformVersion':'7.1.2',
	'deviceName':'85219011',
	'appPackage':'com.docrab.pro',						
	'appActivity':'com.docrab.pro.ui.page.SplashActivity',
    'noReset':'True',#每次运行不重新装包
	'unicodeKeyboard':'True', #使用unicodeKeyboard的编码方式来发送字符串
	'resetKeyboard':'True'#将键盘隐藏起来
	}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps) 
driver.implicitly_wait(20)
son = 'resourceId("com.docrab.pro:id/layout_phone").childSelector(resourceId("com.docrab.pro:id/ev_search_cell"))'			
driver.find_element_by_android_uiautomator(son).send_keys('18500000000')
driver.find_element_by_id('com.docrab.pro:id/tv_get_code').click()
son1 = 'resourceId("com.docrab.pro:id/layout_codes").childSelector(resourceId("com.docrab.pro:id/ev_search_cell"))'						
driver.find_element_by_android_uiautomator(son1).send_keys('1688')
driver.find_element_by_id('com.docrab.pro:id/btnLogin').click()
driver.find_element_by_id('layout_left').click()
time.sleep(3)
#driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.docrab.pro:id/tv_public")').click()
driver.tap([(840,98),(1032,163)],500)
#driver.find_element_by_id('tv_public').click()
driver.find_element_by_id('tv_cell_name').click()
driver.find_element_by_id('etSearch').send_keys(u'艾东小区')
time.sleep(3)
driver.tap([(500,250),(600,250)],500)
driver.find_element_by_id('tv_property').click()
time.sleep(3)
driver.swipe(540,1660,540,1500,500)
#driver.find_element_by_class_name('android.widget.TextView').click()
driver.find_element_by_id('tv_ok').click()
driver.find_element_by_id('tv_cottage_form').click()
driver.find_element_by_id('tv_ok').click()
driver.find_element_by_android_uiautomator('text("地下室层数").fromParent(text("请输入"))').send_keys('3')
driver.find_element_by_android_uiautomator('text("别墅地上层数").fromParent(text("请输入"))').send_keys('5')
driver.find_element_by_android_uiautomator('resourceId("com.docrab.pro:id/cottage_building_unit").fromParent(text("请输入"))').send_keys('2')
driver.find_element_by_id('checkbox_1').click()
driver.find_element_by_id('checkbox_2').click()
driver.find_element_by_id('checkbox_3').click()
driver.find_element_by_android_uiautomator('text("建筑面积").fromParent(text("请输入"))').send_keys('100')
driver.find_element_by_id('tv_years').click()
driver.find_element_by_id('tv_ok').click()
driver.find_element_by_id('iv_add_pic').click()
driver.tap([(362,240),(718,600)],500)
time.sleep(2)
driver.tap([(994,257),(1063,327)],500)
driver.find_element_by_id('commit').click()				
def swipeUp(driver,t=500,n=1):
	l = driver.get_window_size()   #获取手机屏幕尺寸				
	x1 = l['width'] * 0.5 # x坐标				
	y1 = l['height'] * 0.75 # 起始y坐标				
	y2 = l['height'] * 0.25 # 终点y坐标				
	for i in range(n):
		driver.swipe(x1,y1,x1,y2,t)
swipeUp(driver,t=500,n=1)
driver.find_element_by_android_uiautomator('text("房源自评").fromParent(className("android.widget.EditText"))').send_keys('你好啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈')
driver.find_element_by_android_uiautomator('text("我的售价").fromParent(text("请输入"))').send_keys('100')
driver.find_element_by_id('ll_confirm').click()




import hashlib
import hmac
import base64

#拼接data
data={"mobile":"13700000128","password":"e19d5cd5af0378da05f63f891c7467af","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":'hashing'}
c=''
for a,b in sorted(data.items()):
	if b!='' and a!='sign':
		c+="%s=%s"%(a,b)
		if sorted(data.items())[-1][0]!=a:	
			c+='&'
print(c[0:-1])
sk="kongzhongjr2018"
#生成签名
hashing =hmac.new(bytes(sk,encoding='utf-8'),bytes(c,encoding='utf-8'),hashlib.sha1).hexdigest()
print(hashing)
#请求接口
headers={"Content-Type":"application/json"}
data={"mobile":"13700000128","password":"e19d5cd5af0378da05f63f891c7467af","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":hashing}
r=requests.post(url="http://106.75.16.42:9300/login/passwordLogin",headers=headers,data=json.dumps(data))
print(r.json())

'''




import hashlib
import hmac
import base64,requests,json

#拼接data
#data={"mobile":"13700000128","password":"e19d5cd5af0378da05f63f891c7467af","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":"hashing"}
data={"mobile":"13700000128","password":"e19d5cd5af0378da05f63f891c7467af","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":'hashing'}
c=''
for a,b in sorted(data.items()):
	if b!='' and a!='sign':
		c+="%s=%s"%(a,b)
		if sorted(data.items())[-1][0]!=a:	
			c+='&'
print(c[0:-1])
sk="kongzhongjr2018"
#生成签名
hashing =hmac.new(bytes(sk,encoding='utf-8'),bytes(c,encoding='utf-8'),hashlib.sha1).hexdigest()
print(hashing)
#请求接口
headers={"Content-Type":"application/json"}
data={"mobile":"13700000128","password":"e19d5cd5af0378da05f63f891c7467af","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":hashing}
r=requests.post(url="http://106.75.16.42:9300/login/passwordLogin",headers=headers,data=json.dumps(data))
print(r.json())





data1={"mobile":"13700000128","password":"password","appPushId":"1517bfd3f791f921b71","client":"ios","code":"","timestamp":"1532404420","sign":"hashing"}


c=''
for a,b in sorted(data1.items()):
	if b!='' and a!='sign':
		c+="%s=%s"%(a,b)
		if sorted(data1.items())[-1][0]!=a:	
			c+='&'
sk="kongzhongjr2018"
#生成签名
hashing=hmac.new(bytes(sk,encoding='utf-8'),bytes(c,encoding='utf-8'),hashlib.sha1).hexdigest()

print(hashing)
