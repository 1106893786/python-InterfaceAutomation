# import unittest,ddt
# from util.connect_db import  OperationMysql
#
# data_case = ({'name': 'qwl', 'age': '18'}, {'name': '吴彦祖', 'age': '38'})
#
# @ddt.ddt
# class Test02(unittest.TestCase):
#     opmysql = OperationMysql()
#
#     def setUp(self):
#         # self.opmysql.query(sql='select * from cname')
#         self.opmysql.update_add_delete(sql="insert into cname VALUE('007','物理',6) ")
#         print("开始")
#
#     def tearDown(self):
#         self.opmysql.update_add_delete(sql="delete from cname where id = '007'")
#         # self.opmysql.query(sql='select * from cname')
#         print("结束")
#
#     @ddt.data(*data_case)
#     # @ddt.unpack
#     def test_01(self,age):
#         print('执行第一条用例')
#
#
#
#
# if __name__ == '__main__':
#     unittest.main()
#     # Test02.test_01()