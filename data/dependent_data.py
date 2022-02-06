from util.operation_excel import openrationExcel
from base.runMethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse
import json

class DependentData:

    def __init__(self,case_id):
        self.case_id = case_id
        self.opera_excel = openrationExcel()
        self.run_method = RunMethod()
        self.get_data = GetData()

    #通过caseId去获取caseId的整行数据
    def get_case_line_data(self):
        rows_data = self.opera_excel.get_rows_data(self.case_id)
        return rows_data

    #执行依赖测试获取结果
    def run_dependent(self):
        row_num = self.opera_excel.get_row_num(self.case_id)
        request_data = self.get_data.get_request_data(row_num)
        header = self.get_data.is_header(row_num)
        return_type = self.get_data.get_return_type(row_num)
        method = self.get_data.get_request_method(row_num)
        url = self.get_data.get_request_url(row_num)
        res = self.run_method.run_main(method, return_type, url, request_data, header)
        return res

    #根据依赖的key去获取执行依赖测试case的响应数据,然后进行返回
    def get_data_for_key(self,row):
        depend_data  = self.get_data.get_depend_key(row)
        response_data = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(response_data) #在response_data中查询depend_data的值
        return [math.value for math in madle][0]

if __name__ == '__main__':
    d = DependentData('Imooc-1')
    print(d.get_case_line_data())
    print(d.run_dependent())
    print(d.get_data_for_key(5))
