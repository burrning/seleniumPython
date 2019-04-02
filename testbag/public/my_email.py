# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
#from log import getcwd
import os
from log import log1
from Base_Page import BasePage
import time

rq = time.strftime('%Y%m%d', time.localtime(time.time()))  # 获取本地时间 转换成日期
my_mail = BasePage(driver=1)
sender = my_mail.config_get('email', 'sender')  # 发件人邮箱账号
password = my_mail.config_get('password', 'sender')  # 发件人邮箱密码
username = my_mail.config_get('username', 'sender')  # 发件人姓名
users = my_mail.config_options('addressed')  # 收件人
addressed_eamils = my_mail.get_addkey(users)  # 收件人邮箱

#path = 'C:/Users/hyy/PycharmProjects/untitled1/testbag/testcase/repot/HTML'
#file = os.path.join(path + '/xxxUI自动化测试报告.html')


def mail(file_name):
    try:
        # 创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr([username, sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        log1.info('发件人姓名：%s' % username)
        log1.info('发件人邮箱：%s' % sender)
        message['To'] = ';'.join(addressed_eamils)  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        log1.info('收件人邮箱：' + ';'.join(addressed_eamils))
        message['Subject'] = rq + "厚益云UI自动化测试报告.html"  # 邮件的主题，也可以说是标题

        # 邮件正文内容
        message.attach(MIMEText('附件为厚益云UI自动化测试报告.html', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
        log1.info('读取附件')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", "厚益云UI自动化测试报告.html"))
        # 附件名称非中文时的写法
        # att["Content-Disposition"] = 'attachment; filename="test.html")'
        message.attach(att1)
        log1.info('添加附件')

        server = smtplib.SMTP_SSL("smtp.163.com")  # 发件人邮箱中的SMTP服务器，端口是25
        log1.info('连接163邮箱smtp服务')
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        log1.info('连接成功')
        server.sendmail(sender, addressed_eamils, message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        log1.info("邮件发送成功")
    except Exception:
        log1.error("邮件发送失败", exc_info=1)

