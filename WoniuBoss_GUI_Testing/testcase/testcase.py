import unittest
from WoniuBoss_GUI_Testing.common.common import Common
from WoniuBoss_GUI_Testing.util.data_util import DataUtil
from parameterized import parameterized
# 读取gui测试用例
GUI_test_data = DataUtil.get_gui_data()
# 定义测试类
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass
    @classmethod
    def tearDownClass(cls):
        pass
    # 初始化common对象
    def setUp(self):
        self.common = Common()
    # 关闭浏览器
    def tearDown(self):
        self.common.driver.close()
    # 定义gui测试方法
    @parameterized.expand(GUI_test_data)
    def test_gui(self,id,module,title,script,content,method,expect):
        self._testMethodDoc = module+"--"+title
        # 将关键字脚本按行分割
        line_list = script.split("\n")
        for line in line_list:
            # 将每行脚本再进行分割
            key_list = line.strip().split(",")
            # 分割后第一项为动作，后面均为参数
            operation = key_list[0]
            # 定义空列表用于存放参数
            args = []
            for i in range(1,len(key_list)):
                args.append(key_list[i])
            # 利用反射机制逐行调用动作对应的方法
            getattr(self.common,operation)(*args)
        # 利用反射机制调用断言方法得到实际结果
        result = getattr(self.common,method)(content)
        # 将实际结果与预期结果进行对比
        self.assertEquals(result,expect)

if __name__ == '__main__':
    unittest.main()

