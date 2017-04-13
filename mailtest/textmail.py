# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def text_mail():
    msg = MIMEText('你好', 'text', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    return msg


def attachment_mail():
    msg = MIMEMultipart('related')
    msg['Subject'] = 'test message'

    att = MIMEText(open(r'../test.py', 'rb').read(), 'base64', 'utf-8')
    att['Content-Type'] = 'application/octet-stream'
    att['Content-Disposition'] = 'attachment;filename="demo.py"'
    msg.attach(att)
    return msg


sender = 'hitchenghengchao@163.com'
receiver = 'hitchenghengchao@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'hitchenghengchao@163.com'
passwd = 'ChengHchao108049'

# msg = text_mail()
msg = attachment_mail()
smtp = smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(username, passwd)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()