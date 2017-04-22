#coding = utf-8
#######################################################
#filename: xls.py
#function：生成N个(N<65535)1000-9999999之间不重复的随机数，并写入excel文件
#######################################################

import sys
import random
import xlwt

n = sys.argv[1]
index = 0  # 变量初始化

randlist = random.sample(range(1000,9999999,1),int(n))  # 生成N个1000-9999999之间不重复的随机数，并保存在list类型的数据中


wb = xlwt.Workbook(encoding = 'ascii') #创建excel文件
worksheet = wb.add_sheet('user') # 创建名为user的excel表单
for x in randlist:
    worksheet.write(index, 0, x) # 循环取出list中的数据，写入到第一列中
    index = index + 1
wb.save('./random_user.xls')
print  'Finished!'
