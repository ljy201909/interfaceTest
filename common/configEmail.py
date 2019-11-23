#coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.10


import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readConfig import ReadConfig


class ConfigEmail():

    #读取ini文件配置属性
    r = ReadConfig()
    mail_host = r.get_email('mail_host')
    #配置第三方SMTP服务
    #mail_host = 'smtp.163.com'    #设置服务器
    mail_user = r.get_email('mail_user')    #用户名
    mail_pass = r.get_email('mail_pass')    #密码

    #配置邮件属性
    sender = r.get_email('sender')
    receivers = r.get_email('receiver')
    content = r.get_email('content')
    msg = MIMEMultipart()


    def config_file(self):
        #配置附件属性
        file = self.find_file()
        print(file)
        sendfile = open(file,'rb').read()
        att = MIMEText(sendfile,'plain','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.sender
        self.msg['Subject'] = Header(u'Python自动化测试报告','utf-8')
        self.msg.attach(MIMEText(u'这是接口自动化报告邮件，如果想查看详情请查收附件','plain','utf-8'))


    def find_file(self):
        '''查找最新文件'''
        #获取当前路径
        current_path = os.path.dirname(os.path.abspath(__file__))

        #获取报告的存放路径
        filePath = os.path.dirname(current_path) + "/" + 'report'

        #获取filepath路径下全部文件名称的列表
        fileList = os.listdir(filePath)

        fileDict = {}
        fileTime = []

        for iName in fileList:
            #拼接文件路径和i-文件名
            filename  = filePath + "/" + iName
            #获取改文件的修改时间
            iTime = os.path.getmtime(filename)
            #将该文件的修改时间追加到时间列表中
            fileTime.append(iTime)
            #将文件名iname作为字典的value，文件的修改时间ITime作为字典的key存入
            fileDict[iTime] = iName

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        sendfile = filePath + "/" + sendfile
        return sendfile

    #发送邮件
    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            print(self.mail_host,self.mail_user,self.mail_pass,self.sender,self.receivers,self.msg.as_string())
            s.connect(self.mail_host,25)    #25为SMTP端口号
            #s.set_debuglevel(1)
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(self.sender,self.receivers,self.msg.as_string())
            print(u"邮件发送成功")

        except smtplib.SMTPException as msg:
            print(u"Error：无法发送邮件")

if __name__ == '__main__':
    pass
c = ConfigEmail()
c.send_mail()