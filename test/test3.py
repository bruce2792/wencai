import wencai as wc
import datetime as dt
import os
import json

## 所有A股,A股，A股市值降序
# result = wc.search(query="A股市值降序", page=1, pageSize=5000)
# print(result)

# 1794.08 1794.02 1794.00 A股现价以及昨日收盘价 A股上市日期降序 A股上市日期降序
result = wc.search(query="A股换手率排名", page=1, pageSize=1)
print(result)

# result = wc.search(query="A股上市日期降序", page=1, pageSize=1000)
# print(result)