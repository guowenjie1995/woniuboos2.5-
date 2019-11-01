import requests
import random
# 公用方法类
class Common:
    # get请求
    @classmethod
    def get(cls,*args):
        resp = requests.get(url=args[0],cookies=args[1])
        return resp

    #post请求
    @classmethod
    def post(cls,*args):
        resp = requests.post(url=args[0],data=args[1],cookies=args[2])
        return resp

    #text断言
    @classmethod
    def assert_text(cls,*args):
        if args[0] == args[1]:
            return "pass"
        else:
            return "fail"

    #json断言
    @classmethod
    def assert_json(cls,*args):
        content = args[1]
        if eval(args[0]):
            return "pass"
        else:
            return "fail"

    #html断言
    @classmethod
    def assert_html(cls,*args):
        if args[0] in args[1]:
            return "pass"
        else:
            return "fail"

    #code断言
    @classmethod
    def assert_code(cls,*args):
        if args[0] == args[1]:
            return "pass"
        else:
            return "fail"

if __name__ == '__main__':
    url = "http://xtwoniuboss:8080/WoniuBoss2.5/log/userLogin"
    data = {"userName":"WNCD000","userPass":"woniu123","checkcode":"0000"}
    result = getattr(Common,"post")(url,data).text
    print(result)
