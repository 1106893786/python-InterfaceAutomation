import xlrd
# import xlutils.copy
from xlutils.copy import copy

class openrationExcel:
    def __init__(self,file_name=None,sheed_id=None):
        if file_name:
             self.file_name = file_name
             self.sheed_id = sheed_id
        else:
            self.file_name = r'C:\untitled2\data_config\indec.xls'
            # self.file_name = r"C:\Users\Administrator\Desktop\indec.xls"
            self.sheed_id = 0
        # self.data = self.get_data()

    def get_data(self):
        # file_name = r'C:\Users\Administrator\Desktop\indec.xls'
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheed_id]
        # print(tables)
        return tables

    #获取单元格行数
    def get_lines(self):
        tables = self.get_data()
        # print(tables.nrows)
        return tables.nrows

    #获取单元格数据值
    def get_cell_value(self,row, col):
        return self.get_data().cell_value(row,col)

    #写入数据
    def write_values(self,row,col,values):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(self.sheed_id)
        sheet_data.write(row,col,values)
        write_data.save(self.file_name)

    #根据对应的caseID找到对应行的内容
    def get_rows_data(self,case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data

    #根据对应的caseID找到对应的行号
    def get_row_num(self,case_id):
        num = 0
        cols_data = self.get_cols_values()
        # print("cols_data",cols_data)
        # print("caseid", case_id)
        for col_data in cols_data:
            # print("col_data",col_data)
            # print("cols_data",type(cols_data))
            if case_id in col_data :
                # print("case_id",type(case_id))
                return num
            else:
                num = num + 1

    #根据行号找到该行的内容
    def get_row_values(self,row):
        tables = self.get_data()
        row_data = tables.row_values(row)
        return row_data

    #获取某一列的内容
    def get_cols_values(self,col_id=None):
        if col_id != None:
            cols = self.get_data().col_values(col_id)
        else:
            cols = self.get_data().col_values(0)
        return cols

    #获取excel的值转成字典类型（如{'ID': 'Imooc-1', '名称': '实战list', '接口地址': 'http://www.imooc.com/api3/getbanneradvertver2'）再放到列表中存储
    def read_data(self):
        if self.get_lines()>1:
            keys = self.get_data().row_values(0)
            listApidata = []
            for i in range(1,self.get_lines()):
                values =self.get_data().row_values(i)
                api_dict = dict(zip(keys,values))
                listApidata.append(api_dict)
            return listApidata
        else:
            print("表格数据为空")
            return None


if __name__ == '__main__':
    oper = openrationExcel(file_name = r'C:\untitled2\data_config\indec.xls',sheed_id=0)
    print(oper.get_row_values(5))
    print(oper.get_row_num('Imooc-1'))
    # print(oper.get_lines())
    # print(oper.read_data())

    # print("获取总行数",oper.get_lines())
    # print("根据行号找到该行的内容",oper.get_row_values(1))
    # print("获取某一列的内容",oper.get_cols_values(0))
    # print("根据对应的caseID找到对应的行号",oper.get_row_num('Imooc-4'))
    # print("根据对应的caseID找到对应行的内容",oper.get_rows_data('Imooc-4'))