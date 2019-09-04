# index = len(a)  # 获取需要写入数据的行数
# # print(index)
# workbook = xlwt.Workbook()  # 新建一个工作簿
# sheet = workbook.add_sheet('sheet1',cell_overwrite_ok=True)  # 在工作簿中新建一个表格
# for i in range(index):
#     for j in a[i]: # 像表格中写入数据（对应的行和列）
#         sheet.write(0,i,j)
# workbook.save('D:\\1.xls')  # 保存工作簿
# #     print("xls格式表格写入数据成功！")
a = ['/1.0/assets/tradingpwd/validate', 'post', {'login_account_id': {'name': 'login_account_id', 'in': 'query', 'description': '登录账号id', 'required': True, 'type': 'integer'}, 'trading_pwd': {'name': 'trading_pwd', 'in': 'query', 'description': '交易密码', 'required': True, 'type': 'string'}}]
for i in a:
    print(i)