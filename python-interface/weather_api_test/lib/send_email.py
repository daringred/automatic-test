# 负责发邮件
import smtplib
# 负责写邮件
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config.config import *

# 功能：发送邮件
#
# # 1.编写邮件正文（Email邮件需要专门的MIME格式）
# msg = MIMEText('test email', 'plain', 'utf-8')
#
# # 2.组装邮件头（发件人，收件人，主题），email头也要放到邮件内容里，和邮件正文一起组成完整的邮件
#
# from_addr = '发件人'
# to_addr = '收件人'
# msg['From'] = from_addr
# msg['To'] = to_addr
# msg['Subject'] = '邮件主题'
#
# # 3.连接SMTP服务器并发送邮件
# smtp = smtplib.SMTP_SSL('smtp服务器地址')
# smtp.login('发件人的邮箱地址', '发件人的口令密码')
# smtp.sendmail(from_addr, [to_addr], msg.as_string())
# smtp.quit()

# 改进
# 1.  编写邮件内容
# with open('report.html', encoding='utf-8') as f:  # 打开html报告
#     email_body = f.read()  # 读取报告内容
#
# msg = MIMEMultipart()  # 混合MIME格式
# msg.attach(MIMEText(email_body, 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）
#
# # 2. 组装Email头（发件人，收件人，主题）
# msg['From'] = 'test_results@sina.com'  # 发件人
# msg['To'] = '2375247815@qq.com'  # 收件人
# msg['Subject'] = Header('接口测试报告', 'utf-8')  # 中文邮件主题，指定utf-8编码
#
# # 3. 构造附件1，传送当前目录下的 test.txt 文件
# att1 = MIMEText(open('report.html', 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
# msg.attach(att1)
#
# # 4. 连接smtp服务器并发送邮件
# smtp = smtplib.SMTP_SSL('smtp.sina.com')  # smtp服务器地址 使用SSL模式
# smtp.login('test_results@sina.com', 'hanzhichao123')  # 用户名和密码
# smtp.sendmail("test_results@sina.com", "2375247815@qq.com", msg.as_string())
# smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
# smtp.quit()
# from config import *

# 功能：
# 1.邮件正文为HTML格式
# 2.邮件主题为中文
# 3.邮件包含附件
def send_email(report_file):

    # 1.  编写邮件内容，
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    # 2. 组装Email头（发件人，收件人，主题）
    from_addr = sender
    key = smtp_key
    # key = 'Daddy12345'
    to_addr = receiver
    subject = mail_subject
    msg['From'] = from_addr  # 发件人
    msg['To'] = to_addr  # 收件人
    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，指定utf-8编码

    # 3. 构造附件1，附件也是MIME格式
    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'  # filename为邮件中附件显示的名字
    msg.attach(att1)

    # 4. 连接smtp服务器并发送邮件
    smtp_addr = smtp_server
    try:
        smtp = smtplib.SMTP_SSL(smtp_addr, 465)  # smtp服务器地址 使用SSL模式
        smtp.login(from_addr, key)  # 用户名和口令
        smtp.sendmail(from_addr, to_addr, msg.as_string())
        # smtp.sendmail("test_results@sina.com", "superhin@126.com", msg.as_string())  # 发送给另一个邮箱
        # logging.info("邮件发送完成！")
        smtp.quit()
    except Exception as e:
        # logging.error(str(e))
        print(str(e))

