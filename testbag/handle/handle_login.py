# coding = utf-8
from find_element_login import FindLoginElement
import pytesseract
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains

class Login_handle(object):
    def __init__(self,driver):
        self.file_name = "D:/testpng/test1.png"
        self.driver = driver
        self.find_login_el = FindLoginElement(driver)

    def send_username(self,username):
        self.find_login_el.find_username_element().send_keys(username)

    def send_prd(self,prd):
        self.find_login_el.find_password_element().send_keys(prd)

    def send_code(self,code):
        self.find_login_el.find_code_element().send_keys(code)

    def click_login_btn(self):
        self.find_login_el.find_login_button().click()
    #def get_code_error(self):
    #    text = self.find_login_el.code_error_element().getText()
    #    return text
    '''''
    def get_code_error(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.find_login_el.code_error_element()
        print(code_element.location)
        left = code_element.location["x"]
        top = code_element.location["y"]
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        image = Image.open(file_name)
        text = pytesseract.image_to_string(image,lang=None)
        print(text)
        return text
    '''
    def save_picture(self,filename):
        self.driver.save_screenshot(filename)