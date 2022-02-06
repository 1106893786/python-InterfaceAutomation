import smtplib
import configparser
from email.mime.text import MIMEText


class SendEmail:

    global send_user
    global email_host
    global password
    config = configparser.ConfigParser()
    config.read(r'C:\untitled2\config\setting.ini',encoding='utf-8')
    password = config.get('send_email','password')
    email_host = config.get('send_email','email_host')
    send_user = config.get('send_email','send_user')
    def send_mail(self,user_name,sub_title,content):
        user = '李沛宸' + "<"+ send_user + ">"
        message = MIMEText(content,_subtype='plain',_charset='utf-8')
        message['Subject'] = sub_title
        message['From'] = user
        message['To'] = ";".join(user_name)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user,password)
        server.sendmail(user,user_name,message.as_string())
        server.close()

    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))
        fail_num = float(len(fail_list))
        count_num = pass_num + fail_num
        #转化为百分号
        pass_result = "%.2f%%"%(pass_num / count_num * 100)
        fail_result = "%.2f%%"%(fail_num / count_num * 100)
        user_name = ['1106893786@qq.com']
        sub_title = self.config.get('send_email','sub_title')
        # user_name =self.config.get('send_email','user_name')
        # print('username',user_name)
        # user_list = user_name.split(',')
        # print('user_list',user_list)
        content = '此次一共运行接口个数为%s,通过个数为%s,失败个数为%s,通过率为%s,失败率为%s'%(count_num,pass_num,fail_num,pass_result,fail_result)
        # content = self.config.get('send_email', 'content')
        self.send_mail(user_name,sub_title,content)

if __name__ == '__main__':
    # user_name = ['1106893786@qq.com']
    # sub_title = '测试邮件'
    # content = '第一封测试邮件'
    sen = SendEmail()
    # sen.send_mail(user_name,sub_title,content)
    sen.send_main([1,2,3],[4,5,6,7,8,9])
