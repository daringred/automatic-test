import unittest
from lib.HTMLTestReportCN import HTMLTestRunner
from config.config import *
from lib.send_email import send_email
# 功能：生成测试报告（HTML报告、文本报告）
'''
项目结构：
config: 存放项目配置文件
data: 存放用例数据文件
lib: 公共方法库
log: 存放日志文件
report: 存放报告文件
test: 存放测试用例
'''
logging.info("================================== 测试开始 ==================================")

# 构建测试集
suite = unittest.defaultTestLoader.discover(test_path) # 从配置文件中读取用例路径

# 运行测试用例，产生测试报告
with open(report_file, 'wb') as f: # 从配置文件中读取
    HTMLTestRunner(stream=f, title='API test', description='和风天气接口测试报告', tester='syyao').run(suite)
# with open('text_test_report.txt', 'w') as f:
#     unittest.TextTestRunner(stream=f, descriptions='和风天气接口测试报告').run(suite)

# 将测试报告以邮件形式发送
send_email(report_file)

logging.info("================================== 测试结束 ==================================")

