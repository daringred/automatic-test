import unittest
import requests
import  json
# import sys
# import os
from config.config import *
# sys.path.append(os.path.join(prj_path,'test'))
from lib.read_excel import *  # 从项目路径下导入
from lib.case_log import log_case_info

class TestWeatherApi(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 整个测试类只执行一次
        cls.data_list = excel_to_list(os.path.join(data_path, 'test_weather_data.xlsx'), "Sheet1")  # 读取该测试类所有用例数据, 增加data路径
        # cls.data_list 同 self.data_list 都是该类的公共属性

    # 用例执行顺序：并非按书写顺序执行，而是按用例名ascii码先后顺序执行
    def test_hw_weather_api(self):
        case_data = get_test_data(self.data_list, 'test_hw_weather_api')
        if not case_data:
            logging.error('用例数据不存在')
        url = case_data['url']
        expect_res = case_data['expect_res']
        data = case_data['data']

        response = requests.get(url=url)
        res = json.loads(response.text)
        # 断言，判断返回数据是否正确，这里是判断状态码是否为OK
        res = res['HeWeather6'][0]['status']
        log_case_info('test_hw_weather_api', url, data, expect_res, res)
        self.assertEqual(res, expect_res)
        # print(sys.path)


if __name__ == '__main__':
    unittest.main()
    # print(sys.path)

