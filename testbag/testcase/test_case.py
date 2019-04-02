# coding=utf-8
import unittest
from login_page_bussines import LoginBussines
from selenium import webdriver
from handle_login import Login_handle
import time
import ddt
from excel_util import ExcelUtil
import HTMLTestRunner
import os
from excel_util import ExcelUtil

ex = ExcelUtil()
data = ex.get_data()

@ddt.ddt
class FirstCase01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):



        print("开始执行")

    @classmethod
    def tearDownClass(cls):
        print("结束执行")

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://betamweb.houyicloud.com/#/user/login")
        self.login_b = LoginBussines(driver=self.driver)
        self.login_h = Login_handle(driver=self.driver)
        time.sleep(5)

    def tearDown(self):
        case_name = self._testMethodName
        self.driver.save_screenshot(filename="C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/picture/"+case_name+".png")
        '''
        for method_name,error in self._outcome.error:
            if error:
                case_name = self._testMethodName
                self.driver.save_screenshot(filename="C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/picture"+case_name+".png")
        '''
        time.sleep(5)
        self.driver.close()

    @ddt.data(*data)
    def test_login_code_error4(self,data):

        username, password, code = data
        self.login_b.login(username,password,code)
        print(data)
        print("这是第四条")
    '''
    def test_login_code_error5(self):
        self.login_b.login("sunpenghui", "123456", "11111")
        print("这是第五条")

    def test_login_code_error6(self):
        self.login_b.login("sunpenghui", "123456", "123456")
        print("这是第六条")
    '''

'''
        try:
            a = self.login_h.get_code_error(file_name="D:/testpng/test1.png")
            print(a)
            self.assertEqual(a, '验证码错误')
        except Exception as e:
            print("%s",e)
        finally:
            pass
'''

if __name__ == '__main__':
    unittest.main()

