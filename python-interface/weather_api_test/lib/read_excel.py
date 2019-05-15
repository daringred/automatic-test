import xlrd

def excel_to_list(data_file, sheet):
    data_list = []
    wb = xlrd.open_workbook(data_file)
    sh = wb.sheet_by_name(sheet)
    header = sh.row_values(0)
    for i in range(1, sh.nrows):
        # print(sh.row_values(i))
        d = dict(zip(header, sh.row_values(i)))
        data_list.append(d)
    return data_list

def get_test_data(data_list, case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']:
            return case_data
        else:
            return None

if __name__ == '__main__':
    data_list = excel_to_list('test_weather_data.xlsx', 'Sheet1')
    case_data = get_test_data(data_list, 'test_hw_weather_api')
    print(case_data)