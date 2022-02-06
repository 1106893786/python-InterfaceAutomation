import unittest,requests,ddt,json
from util.operation_excel import openrationExcel
from main.run_main import RunTest
# from BeautifulReport import BeautifulReport
from util.connect_db import  OperationMysql

fileName = r'C:\untitled2\data_config\indec.xls'
sheed_id = 0
testData  = openrationExcel(file_name=fileName,sheed_id=sheed_id).read_data()
print("testData",testData)

@ddt.ddt
class Test01(unittest.TestCase):
    opmysql = OperationMysql()

    def setUp(self):
        self.s = requests.session()
        # self.opmysql.query('select * from cname')
        # self.opmysql.update_add_delete(sql="insert into cname VALUE('011','物理',6) ")
        # self.opmysql.update_add_delete(sql="update cname set Cname = '语文'where  id = '001' ")
        print("开始")

    def tearDown(self):
        # self.opmysql.update_add_delete(sql="delete from cname where id in ('007','008','009','010') ")
        print("结束")

    @ddt.data(*testData)
    def test_01(self,data):
        run_test = RunTest(fileName=fileName,sheed_id=sheed_id)
        run_test.go_on_run()
        print('执行第一条用例')



    # def test_02(self):
    #     self.run_test = RunTest(fileName= r'C:\untitled2\data_config\indec.xls')
    #     self.run_test.go_on_run()
    #     print("执行第二条用例")

if __name__ == '__main__':
    unittest.main()