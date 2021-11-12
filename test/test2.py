import wencai as wc
import datetime as dt
import os
import json

## 所有A股,A股，A股市值降序
# result = wc.search(query="A股市值降序", page=1, pageSize=10)
# print(result)

# 1794.08 1794.02 1794.00
# result = wc.search(query="A股现价以及昨日收盘价", page=1, pageSize=10)
# print(result)

# result = wc.search(query="A股现价", page=1, pageSize=10)
# print(result)

result = wc.search(query="A股现价以及昨日收盘价", page=3, pageSize=1000)
print(result)



# print(dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
#
# print(os.path.dirname(__file__) + '/cookies.json')
# json_path = os.path.dirname(__file__) + '/cookies.json'
# print(json_path)
#
# cookies = dict()
#
# cookies['expire_time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
#
#
# with open(json_path, 'w') as f:
#     json.dump(cookies, f)
# ## return henxin_v
#
#
