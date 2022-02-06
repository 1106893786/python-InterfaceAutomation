import data.data_config
from util.openration_json import OnpreaJson
from util.operation_excel import openrationExcel

class GetData:
    def __init__(self,fileName = None,sheed_id = None):
        if fileName!=None:
            self.opera_excel = openrationExcel(file_name=fileName,sheed_id=sheed_id)
        else:
            self.opera_excel = openrationExcel()
        self.opera_json = OnpreaJson()

    # 获取excel行数，就是我们的case数
    def get_case_lines(self):
        return  self.opera_excel.get_lines()

    # 获取是否执行
    def get_is_run(self,row):
        col = int(data.data_config.get_run())
        run_model = self.opera_excel.get_cell_value(row,col)
        flag = None
        if run_model == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否携带header
    def is_header(self,row):
        col = int(data.data_config.get_head())
        header = self.opera_excel.get_cell_value(row,col)
        if header == None: #这个地方正式判断时要判断是否为空，不为空时传excel文件的header值
            return header
        else:
            return None

    #是否进行数据库查询
    def is_mysql(self,row):
        col = int(data.data_config.get_is_mysql())
        is_mysql = self.opera_excel.get_cell_value(row,col)
        if is_mysql == 'yes':
            return is_mysql
        else:
            return None

    # 获取请求方式
    def get_request_method(self,row):
        col = int(data.data_config.get_run_way())
        request_method =self.opera_excel.get_cell_value(row,col)
        return request_method

    #获取请求的返回类型
    def get_return_type(self,row):
        col = int(data.data_config.get_return_type())
        return_type = self.opera_excel.get_cell_value(row,col)
        return return_type

    # 获取url
    def get_request_url(self,row):
        col = int(data.data_config.get_url())
        url = self.opera_excel.get_cell_value(row,col)
        return url

    # 获取请求数据
    def get_request_data(self,row):
        col =int(data.data_config.get_data())
        request_data = self.opera_excel.get_cell_value(row,col)
        if request_data == "":
            return None
        else:
            return request_data

    # 通过获取关键字拿到data数据
    def get_data_for_json(self,row):
        requst_json_data = self.opera_json.get_data(self.get_request_data(row))
        return requst_json_data

    # 获取预期结果
    def get_expecet_data(self,row):
        col = int(data.data_config.get_expect())
        expect = self.opera_excel.get_cell_value(row,col)
        if expect == "":
            return None
        else:
            return expect

    #写入实际结果
    def write_result(self,row,value):
        col = int(data.data_config.get_result())
        return self.opera_excel.write_values(row,col,value)

    #获取依赖数据的key
    def get_depend_key(self,row):
        col = int(data.data_config.get_data_depend())
        depend_key = self.opera_excel.get_cell_value(row,col)
        if depend_key == "":
            return None
        else:
            return depend_key

    #判断是否有case依赖
    def is_depend(self,row):
        col = int(data.data_config.get_case_depend())
        depend_case = self.opera_excel.get_cell_value(row,col)
        if depend_case =="":
            return None
        else:
            return depend_case

    #获取数据依赖字段
    def get_depend_file(self,row):
        col = int(data.data_config.get_file_depend())
        depend_file = self.opera_excel.get_cell_value(row,col)
        if depend_file == "":
            return None
        else:
            return depend_file

if __name__ == '__main__':
    get_data = GetData()
    # get_data.get_data_for_json(10)
#


