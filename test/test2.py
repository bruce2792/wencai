import wencai as wc
import datetime as dt
import os
import json

result = wc.search(query="所有A股", page=31)
print(result)

print(dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))

print(os.path.dirname(__file__) + '/cookies.json')
json_path = os.path.dirname(__file__) + '/cookies.json'
print(json_path)

cookies = dict()

cookies['expire_time'] = dt.datetime.today().strftime('%Y-%m-%d %H:%M:%S')


with open(json_path, 'w') as f:
    json.dump(cookies, f)
## return henxin_v


