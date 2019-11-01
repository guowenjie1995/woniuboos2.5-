from WoniuBoss_Protocol_Testing.common.common import Common
from WoniuBoss_Protocol_Testing.util.data_util import DataUtil
import requests
import unittest
from parameterized import parameterized
# 获取测试数据
test_data = DataUtil.get_protocol_data()
# 定义测试类并继承TestCase抽象类
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # 获取cookie
        url = "http://xtwoniuboss:8080/WoniuBoss2.5/log/userLogin"
        data = {"userName": "WNCD000", "userPass": "woniu123", "checkcode": "0000"}
        cls.cookie = requests.post(url,data).cookies
        requests.post("http://xtwoniuboss:8080/WoniuBoss2.5/second?vp=woniu123", cookies=cls.cookie)
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass
    @parameterized.expand(test_data)
    def test_protocol(self,id,module,title,url,method,param,code,content,type,expect):
        self._testMethodDoc = module+"--"+title
        result = ""
        # 发送get请求
        if method == "get":
            resp = getattr(Common,method)(url+param,self.cookie)
            # 响应为文本的断言
            if type == "text":
                result = getattr(Common,"assert_"+type)(content,resp.text)
            # 响应为json的断言
            elif type == "json":
                result = getattr(Common,"assert_"+type)(content,resp.json())
            #  使用状态码断言
            elif type == "html":
                result = getattr(Common,"assert_"+type)(content,resp.content.decode())
            elif type == "code":
                result = getattr(Common,"assert_"+type)(code,resp.status_code())
            else:
                pass
        # 发送post请求
        elif method == "post":
            resp = getattr(Common,method)(url,eval(param),self.cookie)
            # 响应为文本的断言
            if type == "text":
                result = getattr(Common,"assert_"+type)(content,resp.text)
            # 响应为json的断言
            elif type == "json":
                result = getattr(Common,"assert_"+type)(content,resp.json())
            #  使用状态码断言
            elif type == "html":
                result = getattr(Common,"assert_"+type)(content,resp.content.decode())
            elif type == "code":
                result = getattr(Common,"assert_"+type)(code,resp.status_code())
            else:
                pass
        else:
            pass
        self.assertEquals(result, expect)

if __name__ == '__main__':
    unittest.main()
