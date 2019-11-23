#coding:utf-8
__author__ = 'ljy'
#create_time = 2019.11.10


import smtplib,os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from common.readConfig import ReadConfig


class ConfigEmail():

    #
    r = ReadConfig()
    mail_host = r.get_email('mail_host')
    #
    mail_host = 'smtp.163.com'
    mail_user = r.get_email('mail_user')
    mail_pass = r.get_email('mail_pass')


    sender = r.get_email('sender')
    receivers = r.get_email('receiver')
    content = r.get_email('content')
    msg = MIMEMultipart()


    def config_file(self):

        file = self.find_file()
        print(file)
        sendfile = open(file,'rb').read()
        att = MIMEText(sendfile,'plain','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment; filename=report.html'
        self.msg.attach(att)
        self.msg['From'] = self.mail_user
        self.msg['To'] = self.sender
        self.msg['Subject'] = Header('baog','utf-8')
        self.msg.attach(MIMEText('fujian','plain','utf-8'))


    def find_file(self):

        current_path = os.path.dirname(os.path.abspath(__file__))


        filePath = os.path.dirname(current_path) + "/" + 'report'


        fileList = os.listdir(filePath)

        fileDict = {}
        fileTime = []

        for iName in fileList:

            filename  = filePath + "/" + iName

            iTime = os.path.getmtime(filename)

            fileTime.append(iTime)

            fileDict[iTime] = iName

        sendfilekey = max(fileTime)
        sendfile = fileDict[sendfilekey]
        sendfile = filePath + "/" + sendfile
        return sendfile


    def send_mail(self):
        self.config_file()
        try:
            s = smtplib.SMTP()
            print(self.mail_host,self.mail_user,self.mail_pass,self.sender,self.receivers,self.msg.as_string())
            s.connect(self.mail_host,25)
            #s.set_debuglevel(1)
            s.login(self.mail_user,self.mail_pass)
            s.sendmail(self.sender,self.receivers,self.msg.as_string())
            print("success")

        except smtplib.SMTPException as msg:
            print("Error")

if __name__ == '__main__':
    pass
c = ConfigEmail()
c.send_mail()