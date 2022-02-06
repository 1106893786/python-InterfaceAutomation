class global_var:
    id = '0'
    request_name = '1'
    url = '2'
    run = '3'
    request_way = '4'
    return_type = '5'
    header = '6'
    case_depend = '7'
    data_depend = '8'
    filed_depend = '9'
    data = '10'
    is_mysql = '11'
    expect = '12'
    result = '13'

#h获取case_id
def get_id():
    return global_var.id

#获取url
def get_url():
    return global_var.url

def get_run():
    return global_var.run

def get_run_way():
    return global_var.request_way

def get_return_type():
    return global_var.return_type

def get_head():
    return global_var.header

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_file_depend():
    return global_var.filed_depend

def get_data():
    return global_var.data

def get_is_mysql():
    return global_var.is_mysql

def get_expect():
    return global_var.expect

def get_result():
    return global_var.result
