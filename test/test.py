# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
# a = power(3,3)
#
# print(a)
#
# import time,calendar
# ticks = time.localtime()
#
# times = time.strftime("%Y-%m-%d %H:%M:%S", ticks)
#
# print(times)
#
# a = time.strftime("%a %b %d %H:%M:%S %Y", ticks)
#
# print(time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y")))
#
# cal = calendar.month(2019, 7)
# print("以下打印2019-07月的日历")
# print(cal)
#
# b = time.asctime(ticks)
# print(b)
#_*_coding:utf-8_*_
# # print(b)
# headers = {"Authorization": "bearereyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9vbnNpdGUtYXBpLnN0Mi50ZXN0LmxhbnhpbmthLmNvbVwvMS4wXC9hZG1pblwvbWFuYWdlclwvbG9naW4iLCJpYXQiOjE1NjM3NjAzNzEsImV4cCI6MTU2NjQzODc3MSwibmJmIjoxNTYzNzYwMzcxLCJqdGkiOiJRNHhvaVhENHFEeTJuellKIiwic3ViIjoyMzAsInBydiI6IjA1NzdiNDFmNTRlMDk1YTNkOGNhMjM3NDM2NTAxYjhiN2IxZmU0YTQifQ.rAHCL9FT_Z44Kz_Vr25ry23lfbuqBShvFej7eFM_7cs"}
# a.len()
# print(a[2].keys())
# url = 'http://onsite-bd-web.st2.test.lanxinka.com'+a[0]
# print(url)
# files = open("C:\\Users\\Administrator\Desktop\\", mode='w')
a = 1
while a < 7:
    if(a%2 == 0):
        print(a, "is even")
    else:
        print(a, "is old")
    a += 1

# age = int(input("猜年龄："))
# print("")
# ages = 28
# if age <= 0:
#     print("别皮")
#
# elif age == ages:
#     print("优秀啊")
# elif age < ages:
#     print("没这么小哦")
# elif age > ages:
#     print("没这么老")


sites = ["Baidu", "Google", "Runoob", "Taobao"]
for site in sites:
    if site == "Runoob":
        print("菜鸟教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")


for i in range(-1, 9, 3):
    print(i)


if None:
    print("Hello")


# 字段

dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8
dict['SChool'] = "菜鸟教程"


x = True
country_counter = {}

def addone(country):
    if country in country_counter:
        country_counter[country] += 1
    else:
        country_counter[country] = 1

addone('China')
addone('Japan')
addone('china')

print(len(country_counter))



confusion = {}
confusion[1] = 1
confusion['1'] = 2
confusion[1] += 1

sum = 0
for k in confusion:
    sum += confusion[k]
    print(k)

print(sum)