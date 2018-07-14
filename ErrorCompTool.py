# -*- coding:utf-8 -*-

import re
import json
import xlrd
from pyExcelerator import *

configFilePath = 'D:\python\config'
with open(configFilePath, 'r') as f:
    configFileStr = f.read()

# 考虑找不到路径的场景
codeJavaPath = re.findall("error_code_java_file_path.*=.*\"(.+)\"", configFileStr)[0]
errorMsgJSONPath = re.findall("error_msg_json_file_path.*=.*\"(.+)\"", configFileStr)[0]

with open(codeJavaPath, 'r') as codeFile:
    codeFileStr = codeFile.read()

with open(errorMsgJSONPath, 'r') as msgFile:
    msgJson = json.load(msgFile)

# 考虑对错误码做去重校验
codeArr = re.findall("String.+\"(.+)\"", codeFileStr)
u
print '==================='
need2TranslateCodeArr = []
for code in codeArr:
    if not code in msgJson:
        need2TranslateCodeArr.append(code)

print need2TranslateCodeArr

# fname = "D:/python/test.xlsx"
# bk = xlrd.open_workbook(fname)
# try:
#   sh = bk.sheet_by_name("Sheet1")
# except:
#   print "no sheet in %s named Sheet1" % fname
# #获取行数
# nrows = sh.nrows
# #获取列数
# ncols = sh.ncols
# print "nrows %d, ncols %d" % (nrows,ncols)
# #获取第一行第一列数据
# cell_value = sh.cell_value(1,1)
# print cell_value
