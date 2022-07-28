'''
    邮件协议：
    smtp协议 发送邮件 默认端口25
    pop3协议 接受邮件 所有客户端的操作不会反馈到服务器 110
    imap协议 接受邮件 所有客户端的操作会反馈到服务器 143
    jkdydaprkbiceeba
'''

'''
    python中收发邮件 smtplib poplib imaplib
    发送邮件主要用的两个模块： smtplib(负责发送) email(负责构建邮件内容) 
'''

# from smtplib import SMTP
# s = SMTP("smtp.qq.com") # 指定邮件服务器
# s.login("1916259704@qq.com", "jkdydaprkbiceeba") # 登录
# msg = """\
# From: 1916259704@qq.com
# To: wujun8@xiaomi.com
# Subject: wj
#
# this is my test
# """
# s.sendmail("1916259704@qq.com", ["wujun8@xiaomi.com"], msg) # 发送

# from smtplib import SMTP
# from email.mime.text import MIMEText

# 第三方smtp服务设置
# mail_host = "smtp.qq.com"
# mail_user = "1916259704@qq.com"
# mail_pass = "jkdydaprkbiceeba"

# 收件人
# recv = "wujun8@xiaomi.com"
# recv = "1916259704@qq.com"

# 构造邮件内容
# message = MIMEText("Hello World!", "plain", "utf-8")
# # 讲一个对象使用字典的方法去赋值，是使用了__setitem__魔术方法
# message["from"] = mail_user
# message["To"] = recv
# message["Subject"] = "wj-email"

# html_msg = """<p>python邮件测试。。。。</p><p><a href="https://baidu.com">点击进入百度</a><a>
# """
# message = MIMEText(html_msg, "html", "utf-8")
#
# s = SMTP(mail_host)
# s.login(mail_user,mail_pass)
# s.sendmail(mail_user, recv, message.as_string())

import psutil
from smtplib import SMTP
from email.mime.text import MIMEText
mem = psutil.virtual_memory()
mem_total = mem.total
mem_used_percent = (mem.total - mem.available)/mem.total
mem_limit = 0.6
Subject = ""
if mem_used_percent < mem_limit:
    Subject = Subject + "总内存大小为:{}, 当前使用率为:{}, 阈值为:{}\n".format(mem_total, mem_used_percent, mem_limit)

cpu_usage = psutil.cpu_percent()
cpu_limit = 0.5
if cpu_usage < cpu_limit:
    Subject = Subject + "cpu使用率为:{}, 阈值为:{}\n".format(cpu_usage, cpu_limit)
disk = psutil.disk_usage("/")
disk_total = disk.total
disk_usage =  disk.percent/100
disk_limit = 0.7
if disk_usage < disk_limit:
    Subject = Subject + "磁盘空间大小为:{} 当前使用率为:{}, 阈值为:{}".format(disk.total, disk_usage, disk_limit)
print(Subject)
mail_host = "smtp.qq.com"
mail_user = "1916259704@qq.com"
mail_pass = "jkdydaprkbiceeba"
recv = "1916259704@qq.com"
s = SMTP(mail_host)
s.login(mail_user, mail_pass)
message = MIMEText(Subject, "html", "utf-8")
message["from"] = mail_user
message["To"] = recv
message["Subject"] = "wj-email"
s.sendmail(mail_user, recv, message.as_string())
