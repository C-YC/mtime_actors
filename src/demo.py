# coding:utf-8
import sys
import csv
import pandas as pd
reload(sys)
sys.setdefaultencoding("utf-8")


actor_name = '汤姆·哈迪'
# content = pd.read_csv("../actor_works/"+actor_name+".csv", sep=',')
# a = content.fillna("", inplace=True)
# print a
with open("../actor_works/"+actor_name+".csv")as f:
    content = csv.reader(f)
    print list(content)