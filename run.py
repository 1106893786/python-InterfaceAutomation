import os,sys
sys.path.append(os.path.dirname(__file__))
import time
import unittest
from BeautifulReport import BeautifulReport
from util.HTMLTestRunner import HTMLTestRunner

#用例路径
case_path = os.path.join(os.getcwd(),'case')

#报告存放路径
report_path = os.path.join(os.getcwd(),'report')
print(report_path)

def add_case():
    discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py')
    print(discover)
    return discover


def run_case(test_case):
    # discover = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    # 获取当前时间
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    # print(now)
    # 保存生成报告的路径
    report_path = r'C:\untitled2\report\ ' + now + '.html'
    # report_path = r'C:\untitled2\report\ ' + now
    fp = open(report_path, 'wb')
    runner = HTMLTestRunner(
        stream=fp,
        title=u"这是我的自动化测试报告",
        description=u"用例执行情况",
        verbosity=2
    )
    runner.run(test_case)
    # runner = BeautifulReport(test_case)
    # runner.report(
    #     description = '描述信息',
    #     report_dir =report_path,
    #     filename = '自动化测试用例报告'
    # )
    fp.close()


if __name__ == '__main__':
    cases = add_case()
    run_case(cases)




