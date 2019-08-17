import datetime
#_*_coding:utf-8_*_
import requests
# a = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

# 当前时间加30分钟
# a = (datetime.datetime.now()+datetime.timedelta(minutes=30)).strftime("%Y-%m-%d %H:%M:%S")
# print(a)
url4 = 'http://pre-onsite-api.shurenzhipin.com/1.0/admin/manager/login'
url = 'http://pre-onsite-api.shurenzhipin.com/1.0/bd/order/list?admin_list_status=waiting_confirm&page_size=10'
url1 = 'http://pre-onsite-api.shurenzhipin.com/1.0/bd/order/confirm'
url2 = 'http://pre-onsite-api.shurenzhipin.com/1.0/bd/order/depart'
url3 = 'http://pre-onsite-api.shurenzhipin.com/1.0/bd/order/arrive'
url5 = 'http://pre-onsite-api.shurenzhipin.com/1.0/bd/order/interviewed'

data4 = {
    "client_type": 2,
    "mobile": "14520000000",
    "password": "xia123"
}



# BD工具端登录接口
response = requests.request("post", url=url4, data=data4).json()
# print(response4)
b = response['data']['token']
print(b)
headers = {
    "Authorization": b
}

# response1 = requests.request("post", url=url, headers=headers).json()
# print(response1)
# c = response1['data']['list'][0]['order_sn']
#
# data = {
#     "order_sn": c
# }
# print(c)

# 订单确认
# response2 = requests.request("post", url=url1, data=data, headers=headers).json()
#
# print(response2)
data1 = {
    "order_sn": "I20190808267435116357",
    "admin_depart_address": "上海市",
    "admin_depart_longitude": "121.095932",
    "admin_depart_latitude": "30.900587"
}
# BD已出发
# response3 = requests.request("post", url=url2, data=data1, headers=headers).json()
# print(response3)

# BD已到达
# response4 = requests.request("post", url=url3, data=data1, headers=headers).json()
# print(response4)

# BD已面试
response5 = requests.request("post", url=url5, data=data1, headers=headers).json()
print(response5)


'''
面试通过 post /1.0/bd/order/interview/pass
传参：token、order_sn 、company_id 、job_id 、company_interview_time 、company_interview_address 
'''


'''
约复试 post， type =2  接口：/1.0/bd/order/recreate
传参：token、user_id 、job_id 、company_id 、company_interview_time 、company_interview_address 
'''


'''
面试不通过 /1.0/bd/order/interview/fail
传参：token、order_sn 、company_id 、job_id 、company_interview_time 、company_interview_address 、elimination_remark 
'''


'''
未到面 /1.0/bd/order/interview/bailed
传参：token 、order_sn 
'''


'''
已入职 /1.0/bd/order/employed
传参：token 、 order_sn 、job_id、company_id
'''


'''
未入职 /1.0/bd/order/unemployed
传参：token、order_sn 、elimination_remark 、job_id 、 company_id
'''


'''
已离职 /1.0/bd/order/leave
传参：token 、order_sn 、leaved_at 、elimination_remark
'''

