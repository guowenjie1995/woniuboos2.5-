import unittest
from WoniuBoss_Protocol_Testing.util.HTMLTestRunnerCN import HTMLTestRunner
from WoniuBoss_Protocol_Testing.testcase.testcase import Test
# 启动测试并生成测试报告
class TestStart:
    @classmethod
    def start(cls):
        ts = unittest.TestSuite()
        loader = unittest.TestLoader()
        test1 = loader.loadTestsFromTestCase(Test)
        ts.addTests(test1)
        with open('../report/WoniuBoss2.5_Protocol_Testing_Report.html',"w",encoding="utf-8") as file:
            hr = HTMLTestRunner(stream=file,verbosity=2,title='WoniuBoss2.5 Protocol Testing Report',tester="搬砖小分队")
            hr.run(ts)

if __name__ == '__main__':
    TestStart.start()