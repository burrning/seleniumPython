from selenium import webdriver
#import sys
#sys.path.appen("C:/Users/hyy/PycharmProjects/untitled1")
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest
from testbag.public.find_element import FindElement


class Page_function(object):
    def __init__(self, url):
        self.driver = self.get_drver(url)

    def get_drver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.get_user_element("code_image")
        print(code_element.location)
        left = code_element.location["x"]
        top = code_element.location["y"]
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)

    def code_online(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "34")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text

    def main(self):
        file_name = "D:/testpng/test.png"
        code_text = self.code_online(file_name)
        self.send_user_info("user_name", "sunpenghui")
        self.send_user_info("user_prd", "123456")
        self.send_user_info("code_send", code_text)
        self.get_user_element("login_button").click()
        time.sleep(10)
        self.driver.close()


if __name__ == '__main__':
    page_unction = Page_function("https://betamweb.houyicloud.com/#/user/login")
    page_unction.main()
