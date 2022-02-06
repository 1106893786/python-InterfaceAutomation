# coding:utf-8
import sys
sys.path.append(r"C:\untitled2")
from base.runMethod import RunMethod
from data.get_data import GetData
from util.common_util import CommonUtil
from data.dependent_data import DependentData
from util.send_email import SendEmail
from util.operation_header import *
from util.openration_json import OnpreaJson
from util.connect_db import OperationMysql
import unittest

class RunTest(unittest.TestCase):
	def __init__(self,fileName = None,sheed_id=None):
		self.run_method = RunMethod()
		self.com_util = CommonUtil()
		self.send_main = SendEmail()
		self.op_mysql = OperationMysql()
		if fileName !=None:
			self.data = GetData(fileName=fileName,sheed_id=sheed_id)
		else:
			self.data = GetData()

	#程序执行的
	def go_on_run(self):
		res = None
		pass_count = []
		fail_count = []
		row_count = self.data.get_case_lines()

		for i in range(1,row_count) :
			is_run = self.data.get_is_run(i)
			# print("is_run",is_run)
			if is_run ==True:
				method = self.data.get_request_method(i)
				url = self.data.get_request_url(i)
				print("接口地址：",url)
				header = self.data.is_header(i)
				# request_data = self.data.get_data_for_json(i)		#通过关键字从json文件获取请求数据
				request_data = self.data.get_request_data(i)		#直接获取请求数据
				return_type = self.data.get_return_type(i)
				expect = self.data.get_expecet_data(i)
				print('预期结果：',expect)
				# print('预期结果类型',type(expect))
				is_mysql = self.data.is_mysql(i)
				depend_case = self.data.is_depend(i)

				if depend_case != None:
					self.depend_data = DependentData(depend_case)
					depend_response_data = self.depend_data.get_data_for_key(i)
					depend_key = self.data.get_depend_file(i)
					request_data[depend_key] = depend_response_data

				res = self.run_method.run_main(method,return_type,url,request_data,header)
				print("接口返回结果：",res)
				print("接口返回结果类型：",type(res))
				# self.assertIn(expect,res,msg="不存在")
				if is_mysql == 'yes':
					expect = self.op_mysql.query(expect)
					print('数据库查询预期结果：',expect)
					if self.com_util.is_contain(str(expect), str(res)):
						self.data.write_result(i, "pass")
						pass_count.append(i)
					else:
						self.data.write_result(i, str(res))
						fail_count.append(i)

				if self.com_util.is_contain(str(expect),str(res)):
					self.data.write_result(i,"pass")
					pass_count.append(i)
				else:
					self.data.write_result(i,str(res))
					fail_count.append(i)

		# self.send_main.send_main(pass_count,fail_count)


if __name__ == '__main__':
	run = RunTest()
	run.go_on_run()

