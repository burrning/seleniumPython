import unittest
#from case_t import FirstCase
import time
import HTMLTestReportCN
import os
from my_email import mail

case_path = os.path.join(os.getcwd())
suite = unittest.defaultTestLoader.discover(case_path,'test_*.py')

now = time.strftime('%Y-%m-%d %H-%M-%S')
filename = 'C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/HTML/'+now+'result.html'
fb = open(filename, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fb,
                                         title='厚益云管理后台自动化测试报告',
                                         description='环境：win10  浏览器：Chrome')

runner.run(suite)
mail(filename)
fb.close()