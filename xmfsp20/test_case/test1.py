# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.select import Select
# import time
# driver = webdriver.Firefox()
# driver.get("https://www.baidu.com/")
# time.sleep(3)
# a = driver.find_element_by_xpath(".//*[@id='u1']/a[8]")
# ActionChains(driver).move_to_element(a).perform()
# time.sleep(0.5)
# driver.find_element_by_xpath(".//*[@id='wrapper']/div[6]/a[1]").click()
# time.sleep(0.5)
# b = driver.find_element_by_id("nr")
# Select(b).select_by_visible_text("每页显示50条")
# b.click()
# time.sleep(1)
# driver.find_element_by_class_name("prefpanelgo").click()
# time.sleep(0.5)
# c = driver.switch_to.alert
# print(c.text)  # 获取文本
# c.accept()  # 点确定
#
#
# a = [29,12,3,25]
# count = len(a)
# for i in range(0,count):
#     for j in range(i+1,count):
#         if a[i]>a[j]:
#             a[i],a[j]=a[j],a[i]
#         print(a)
# print(a)




# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']/option[3]").click()
# time.sleep(1)
# driver.find_element_by_xpath(".//*[@id='nr']").click()


import configparser
config = configparser.ConfigParser()
path  = "../config/config.ini"
config.read(path)
#修改参数的值
# config.set("EMAIL","sendpwd","1234")
# config.write(open(path, "r+"))
#读
# sender = config.get('EMAIL','sender')#读
# print(sender)
# print('\n')
#追加填写
config.add_section("School")
config.set("School","IP","192.168.1.120")
config.set("School","Mask","255.255.255.0")
config.set("School","Gateway","192.168.1.1")
config.set("School","DNS","211.82.96.1")
# config.write(open(path, "a"))
#覆盖填写
config.write(open(path, "w"))
