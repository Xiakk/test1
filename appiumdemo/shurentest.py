import requests
import datetime

'''
获取当前时间+30分钟timedelta(minutes=30)
当前时间+1天  days=1
'''
localtime = (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")

url = 'http://onsite-api.st2.test.lanxinka.com/1.0/user/login'
url1 = 'http://onsite-api.st1.test.lanxinka.com/1.0/user/order/create'
url2 = 'http://onsite-api.st1.test.lanxinka.com/1.0/user/order/cancel'
url3 = 'http://onsite-api.st1.test.lanxinka.com/1.0/user/my_interviewer'
url4 = 'http://onsite-api.st1.test.lanxinka.com/1.0/admin/manager/login'

data1 = {
    "mobile": 14510000005,
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

# 登录接口
response = requests.request("post", url=url, data=data1).json()
a = response['data']['token']
print(a)
headers = {
    "Authorization": a
}

# 一键找工作接口
# response1 = requests.request("post", url=url1, data=data2, headers=headers).json()
# b = response1['data']['order_sn']
# print(b)
# print(response1)
#
#
# data3 = {
#     "cancel_note": "行程有变，暂时无法面试",
#     "order_sn": b
# }
# 取消订单接口
# response2 = requests.request("post", url=url2, data=data3, headers=headers).json()
# print(response2)

# 获取面试官信息接口
# response3 = requests.request("get", url=url3, headers=headers).json()
# c = response3['data']['admin_mobile']
# print(c)
#
# data4 = {
#     "client_type": 2,
#     "mobile": c,
#     "password": "xia123"
# }
#
# # BD工具端登录接口
# response4 = requests.request("post", url=url4, headers=headers, data=data4).json()
# print(response4)
data5 = {"bank_card_no": "6214832103707563"}

response4 = requests.request("post", url='http://onsite-api.st2.test.lanxinka.com/1.0/user/bank_card/bind', headers=headers, data=data5).json()
print(response4)
