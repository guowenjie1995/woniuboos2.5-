import xlrd

class DataUtil:
    # 获取测试用例
    @classmethod
    def get_gui_data(cls):
        # 打开Excel
        book = xlrd.open_workbook("../data/gui_test_data.xlsx")
        # 定义空列表用来存储测试用例
        test_data = []
        # 打开sheet
        for i in range(1,2):
            sheet = book.sheet_by_index(i)
            # 从第二行开始遍历每行数据转为元组并存入test_data列表
            for i in range(1,sheet.nrows):
                li = tuple(sheet.row_values(i))
                test_data.append(li)
        return test_data


if __name__ == '__main__':
    result = getattr(DataUtil,"get_gui_data")()
    print(result)