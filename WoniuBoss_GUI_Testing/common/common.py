from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time, random, os


class Common:
    # 初始化
    def __init__(self):
        self.driver = None

    # 打开页面
    def open(self, *args):
        if args[0] == "Chrome":
            self.driver = webdriver.Chrome()
        elif args[0] == "Firefox":
            self.driver = webdriver.Firefox()
        elif args[0] == "IE":
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
        self.driver.get(args[1])

    # 强制等待
    def wait(self, *args):
        time.sleep(int(args[0]))

    # 查找元素
    def find(self, *args):
        method = args[0].split("=", 1)[0]
        value = args[0].split("=", 1)[1]
        if method == "id":
            return self.driver.find_element_by_id(value)
        elif method == "xpath":
            return self.driver.find_element_by_xpath(value)
        elif method == "link":
            return self.driver.find_element_by_link_text(value)
        elif method == "class":
            return self.driver.find_element_by_class_name(value)
        elif method == "css":
            return self.driver.find_element_by_css_selector(value)
        elif method == "name":
            return self.driver.find_element_by_name(value)
        else:
            pass

    # 文本输入
    def input(self, *args):
        self.find(args[0]).click()
        self.find(args[0]).clear()
        self.find(args[0]).send_keys(args[1])

    # 文件上传
    def upload(self, *args):
        self.find(args[0]).send_keys(args[1])

    # 单击
    def click(self, *args):
        self.find(args[0]).click()

    # 双击
    def doubleclick(self, *args):
        ActionChains(self.driver).double_click(self.find(args[0])).perform()

    # 右键单击
    def contextclick(self, *args):
        ActionChains(self.driver).context_click(self.find(args[0])).perform()

    # 下拉选择
    def select(self, *args):
        Select(self.find(args[0])).select_by_visible_text(args[1])

    # 通过下标进行下拉选择
    def select_by_index(self, *args):
        Select(self.find(args[0])).select_by_index(int(args[1]))

    # 警告框确认
    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    # 刷新页面
    def refresh(self):
        self.driver.refresh()

    # 以元素的文本值是否与预期一致进行断言
    def assert_text(self, *args):
        try:
            text = args[0].split(",", 1)
            result = self.find(text[0]).text
            if text[1] == result:
                return "pass"
            else:
                return "fail"
        except:
            return "fail"

    # 以元素的value值是否与预期一致进行断言
    def assert_value(self, *args):
        try:
            result = self.find(args[0]).get_attribute("value")
            if args[1] == result:
                return "pass"
            else:
                return "fail"
        except:
            return "fail"

    # 以元素是否存在为依据进行断言
    def assert_exist(self, *args):
        try:
            self.find(args[0])
            return "pass"
        except:
            return "fail"
