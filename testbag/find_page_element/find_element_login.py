from find_element import FindElement


class FindLoginElement(object):
    def __init__(self, driver):
        self.find_element_p = FindElement(driver)

    def find_username_element(self):
        return self.find_element_p.get_element("user_name")


    def find_password_element(self):
        return self.find_element_p.get_element("user_prd")


    def find_code_element(self):
        return self.find_element_p.get_element("code_send")


    def find_login_button(self):
        return self.find_element_p.get_element("login_button")


    def code_error_element(self):
        return self.find_element_p.get_element("code_error_element")
