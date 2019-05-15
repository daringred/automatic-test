import logging
import os
'''增加log功能，产生日志文件log.txt'''

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 当前文件的绝对路径的上一级，__file__指当前文件

data_path = os.path.join(prj_path, 'data')
test_path = os.path.join(prj_path, 'test')

log_file = os.path.join(prj_path, 'log', 'log.txt')
report_file = os.path.join(prj_path, 'report', 'report.html')

# log配置
logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    filename=log_file,  # 日志输出文件
                    filemode='a')  # 追加模式


# 邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '1024217617@qq.com'
smtp_key = 'qukgpapyarhqbdie'

sender = smtp_user
receiver = 'syyao@whu.edu.cn'
mail_subject = '测试报告'

if __name__ == '__main__':
    logging.info("hello")