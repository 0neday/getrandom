#coding=utf-8
#######################################################
#filename:xlsx.py
#function：生成N个(N>=65535)1000-9999999之间的不重复的随机数，并写入excel文件
#######################################################

import sys
import random
import openpyxl

n = sys.argv[1]
index = 1

randlist = random.sample(range(1000,9999999,1),int(n))  # 生成N个1000-9999999之间不重复的随机数，并保存在list类型的数据中


wb = openpyxl.Workbook() #创建excel文件
worksheet = wb.active
worksheet.title = 'user'
for x in randlist:
    worksheet.cell(column=1, row=index, value=x) # 循环取出list中的数据，写入到第一列中
    index = index + 1
wb.save('./random_user.xlsx')
print  'Finished!'
