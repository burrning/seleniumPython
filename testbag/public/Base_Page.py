from log import log1
from selenium.common.exceptions import NoSuchElementException
#from log import getcwd
import os
import time
import configparser
#from until.file_system import get_init_path


config_path = "C:\\Users\hyy\PycharmProjects\\untitled1\config\localElement.ini"
class BasePage():
    '''测试基类'''

    def __init__(self, driver):
        self.driver = driver

    def config_get(self, key, section=None):
        '''读取配置文件字段的值并返回'''
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8-sig")
        switch = config.get('environment', 'switch')
        if section == None and switch == str(0):
            section = 'test'
        elif section == None and switch == str(1):
            section = 'prod'
        config_get = config.get(section, key)
        return config_get



    def get_img(self):
        '''截图'''
        path = 'C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/picture/'  # 拼接截图保存路径
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))  # 按格式获取当前时间
        screen_name = path + rq + '.png'  # 拼接截图文件名
        try:
            self.driver.get_screenshot_as_file(screen_name)
            log1.info("截图保存成功")
        except BaseException:
            log1.error("截图失败", exc_info=1)

    def find_element(self, selector):
        '''定位元素'''
        by = selector[0]
        value = selector[1]
        element = None
        if by == 'id' or by == 'name' or by == 'class' or by == 'tag' or by == 'link' or by == 'plink' or by == 'css' or by == 'xpath':
            try:
                if by == 'id':
                    element = self.driver.find_element_by_id(value)
                elif by == 'name':
                    element = self.driver.find_element_by_name(value)
                elif by == 'class':
                    element = self.driver.find_element_by_class_name(value)
                elif by == 'tag':
                    element = self.driver.find_element_by_tag_name(value)
                elif by == 'link':
                    element = self.driver.find_element_by_link_text(value)
                elif by == 'plink':
                    element = self.driver.find_element_by_partial_link_text(value)
                elif by == 'css':
                    element = self.driver.find_element_by_css_selector(value)
                elif by == 'xpath':
                    element = self.driver.find_element_by_xpath(value)
                else:
                    log1.error('没有找到元素')
                    log1.info('元素定位成功。定位方式：%s，使用的值%s：' % (by, value))
                return element
            except NoSuchElementException:
                log1.error("报错信息：", exc_info=1)
                self.get_img()  # 调用截图
        else:
            log1.error('输入的元素定位方式错误')

    def type(self, selector, value):
        '''输入内容'''
        element = self.find_element(selector)
        element.clear()
        log1.info('清空输入内容')
        try:
            element.send_keys(value)
            log1.info('输入的内容：%s' % value)
        except BaseException:
            log1.error('内容输入报错', exc_info=1)
            self.get_img()

    def click(self, selector):
        '''点击元素'''
        element = self.find_element(selector)
        try:
            element.click()
            log1.info('点击元素成功')
        except BaseException:
            log1.error('点击元素报错', exc_info=1)
            self.get_img()

    def sleep(self, secondes):
        '''强制暂停'''
        time.sleep(secondes)
        log1.info('暂停%d秒' % secondes)

    def get_title(self):
        '''获取title'''
        title = self.driver.title
        log1.info('当前窗口的title是:%s' % title)
        return title

    def quit(self):
        self.driver.quit()
        log1.info('关闭浏览器')

    def config_options(self, section):
        '''读取配置文件某section下所有键'''
        config = configparser.ConfigParser()

        config.read(config_path, encoding="utf-8-sig")
        username = config.options(section)
        return username

    def get_addkey(self, user):
        '''遍历获得配置文件收件人email'''
        sum = 0
        L = []
        for i in user:
            if sum < len(user):
                emails = self.config_get(i, 'addressed')
                L.append(emails)
                sum += 1
        return L


