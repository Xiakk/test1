# a = ['qwe', 'chemistry', 1997, 2000]
# b = [1, 2, 3, 4, 5, 6, 7]
# c = a[0]
# print(c)
# d = b[1:5] #前闭后开
# print(d)
# a.append('12')
# print(a)
import json
dict = {'a': 1, 'b': 2, 'b': 3}
c = json.dumps(dict)
print(c)
a = dict.keys()
b = dict.values()
print(str(a))
print(b)
# print(dict['b'])
# print(dict)
# a = dict.setdefault('a', None)
# print(a)
for k, v in dict.items():
    print(k, v)

