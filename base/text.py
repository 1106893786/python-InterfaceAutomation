# a = "username:123"
# b = {'username': '123', 'pwd': '111'}
# flag = None
# if a in b :
#     flag = True
# else:
#     flag = False
# print(flag)
import operator
# count = 0
# son = 0
# ops = {"+": operator.add, "-": operator.sub}
# for i in range(2,100,2):
#     count = count+1
#     if count % 2 ==0:
#         a = "+"
#     else:
#         a = "-"
#     # print(a)
#     son = ops[a](son,i)
# print(son)
import time
import unittest
# now =time.strftime("%Y-%m-%d %H_%M_%S")
# print(now)
# class demo(unittest.TestCase):
#
#     def aa(self):
#         self.assertIn(10,[1,2,3],msg="相等")
# def is_contain(str_one,str_two):
#     '''
#     :param str_one: 查找的字符串
#     :param str_two:被查找的字符串
#     :return:
#     '''
#     flag = None
#     # isinstance(str_one,unicode)
#     # if isinstance(str_one, unicode):
#     #     str_one = str_one.encode('unicode-escape').decode('string_escape')
#     # return cmp(str_one, str_two)
#     if (str_one in str_two):
#         flag = True
#     else:
#         flag = False
#     return flag

import configparser
import hashlib          #导入MD5加密包b
from util.common_util import CommonUtil
# config = configparser.ConfigParser()
# config.read(r'C:\untitled2\config\setting.ini',encoding='utf-8')
# user_name = config.get('send_email','user_name')
# sub_title = config.get('send_email','sub_title')
# print(user_name)
# print(sub_title)
# s = 'ewewsdas'
# ss = bytes(s,encoding='utf-8')  #将str类型转为bytes类型
# mpsw=hashlib.md5(ss)  #设置为MD5()需要bytes类型
# mpsw=mpsw.hexdigest() #设置为16进制
# print(mpsw)


# str_two = str({'status': 1, 'data': [], 'errorCode': 1006, 'errorDesc': 'token error', 'timestamp': 1643962441843})
# str_one = str({'status': 1123})
# print(type(str_two))
# print(type(str_one))
# a = str({'sta':123,'aaa':333})
# b = str({'sta':123})
# print(type(b))
# c = CommonUtil()
# print(c.is_contain(str_one,str_two))
# print(c.is_contain(a,b))



dict1=str({'name':'Lara','age':18})
one1= str({'name':'Lara','age':18})
# dict1={'name':'Lara','age':18}
# one1= 'name'
# one1= str({'name':'Lara'})
c = CommonUtil()
# print(c.is_equal_dict(one1,dict1))
print(c.is_contain(one1,dict1))

#判断键在不在字典中
# for one in dict1:
# if one1 in dict1:  #或dict1.keys()
#    print('key在字典中！')
#    # break






