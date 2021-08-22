# -*- coding: UTF-8 -*-
# 使用了SMTP库，所以不用写SMTP命令,也不需要处理服务器response,直接按照SMTP报文格式发送
# 本次代码作为用户代理，并提前准备好一切参数
# 参考菜鸟教程
# 使用utf-8来兼容编码base-64
import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host = 'smtp.qq.com'   # 中转服务器
mail_user = 'your_qq@qq.com'
mail_pass = 'your_pass_word'

sender = 'your_qq@qq.com'       # 发送方
receivers = ['rpct_to@qq.com']       # 接收方
# MINEText第一个参数为邮件内容，第二个表示为纯文本，第三个为编码格式，在此函数中构造msg按照SMTP报文格式：FROM，TO，Subject来设置
message = MIMEText('python 测试', 'plain', 'utf-8')
message['From'] = Header("ennio", 'utf-8')
message['To'] = Header("测试", 'utf-8')
subject = 'python smtp 测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 连接TCP
    smtpObj.login(mail_user, mail_pass) # 连接服务器
    smtpObj.sendmail(sender, receivers, message.as_string())  # 用户代理向服务器发送邮件
    print("发送成功")
    smtpObj.close()
except smtplib.SMTPException:
    print("哎呀失败了......")
    smtpObj.close()
    # 想要更具体的报文发送SMTP命令情况可以看我的“telnet QQ邮箱”文章