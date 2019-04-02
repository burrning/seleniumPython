from selenium import webdriver
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest

driver = webdriver.Chrome()


def driver_init():
    driver.get("https://betamweb.houyicloud.com/#/user/login")
    driver.maximize_window()
    time.sleep(5)


def get_element(id):
    element = driver.find_element_by_id(id)
    return element


def get_code_image(file_name):
    driver.save_screenshot("D:/testpng/test.png")
    code_element = driver.find_element_by_xpath('//*[@id="imgVerify"]')
    print(code_element.location)
    left = code_element.location["x"]
    top = code_element.location["y"]
    right = code_element.size["width"] + left
    height = code_element.size["height"] + top
    print(right)
    print(height)
    im = Image.open("D:/testpng/test.png")
    img = im.crop((left, top, right, height))
    img.save(file_name)


def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    text = res.json()["showapi_res_body"]["Result"]
    return text


def run_main():
    user_name = "sunpenghui"
    user_passworld = "123456"
    file_name = "D:/testpng/test1.png"
    driver_init()
    get_element("LAY-user-login-username").send_keys(user_name)
    get_element("LAY-user-login-password").send_keys(user_passworld)
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("LAY-user-login-vercode").send_keys(text)
    get_element("logins").click()
    time.sleep(10)
    driver.close()


run_main()
