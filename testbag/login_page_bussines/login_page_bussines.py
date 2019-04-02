from handle_login import Login_handle
from find_element_login import FindLoginElement
from excel_util import ExcelUtil
import ddt

#ex = ExcelUtil()
#data = ex.get_data()



class LoginBussines(object):
    def __init__(self,driver):
        """

        :rtype: object
        """
        self.login_h = Login_handle(driver)
        self.login_F = FindLoginElement(driver)


    def login(self, username, password, code):

        self.login_h.send_username(username)
        self.login_h.send_prd(password)
        self.login_h.send_code(code)
        self.login_h.click_login_btn()
        #self.login_h.save_picture(filename)


