import os,sys
sys.path.append(os.path.dirname(__file__))
# from config import setting
import unittest,time
# from HTMLTestRunner import HTMLTestRunner
# from lib.sendmail import send_mail
# from lib.newReport import new_report
# from db_fixture import test_data
from util.HTMLTestRunner import HTMLTestRunner

#用例路径
case_path = os.path.join(os.getcwd(),'case')

#报告存放路径
report_path = os.path.join(os.getcwd(),'report')


def add_case():
   # """加载所有的测试用例"""
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    return discover

def run_case(test_case):
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename =   r'C:\untitled2\report\ ' + now + '.html'
    fp = open(filename,'wb')
    runner = HTMLTestRunner( stream=fp,
        title=u"这是我的自动化测试报告",
        description=u"用例执行情况",
        verbosity=2
                            )
    runner.run(test_case)
    fp.close()


if __name__ == '__main__':
    cases = add_case()
    run_case(cases)