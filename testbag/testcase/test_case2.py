# coding=utf-8
import unittest
from login_page_bussines import LoginBussines
from selenium import webdriver
from handle_login import Login_handle
import time

class FirstCase02(unittest.TestCase):
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
        self.driver.save_screenshot(filename="C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/picture"+case_name+".png")
        self.driver.close()

    def test_login_code_error1(self):
        self.login_b.login("sunpenghui","123456","11111")
        print("第一条")
    def test_login_code_error2(self):
        self.login_b.login("sunpenghui","123456","11111")
        print("第二条")
    def test_login_code_error3(self):
        self.login_b.login("sunpenghui","123456","123456")
        print("第三条")

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
    #unittest.FI

