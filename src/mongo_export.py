# coding:utf-8
"""
author:C-YC
target:导出mongodb数据库的演员链接
finish date:2018,07,13
"""
import sys
import os
import time
from pymongo import MongoClient
reload(sys)
sys.setdefaultencoding('utf-8')

# 连接数据库
conn = MongoClient('192.168.235.55', 27017)          # ip
db = conn['admin']                                   # 连接数据库
db.authenticate("admin", "123456")                   # 帐号密码认证
db = conn['team_behind_sc']                          # 所要导出数据的数据库
collection = db['Filmmaker_page']                    # 所要导出数据的数据表

all_url = set()                                      # 定义一个集合，用于数据去重
for item in collection.find():                       # 数据库的查询 .find()
    for key in item:
        if key == "演员":                             # 当键为 演员 时，拿下所有的值，即演员的所有url，顺便去重
            for url in item[key].values():
                all_url.add(url.replace(" ", "."))
print len(all_url)
with open("../data/export.txt", "a+")as f:
    for url in all_url:
        f.write(url+"\n")                            # 将拿到的所有url写入文档
