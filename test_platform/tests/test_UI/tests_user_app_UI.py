from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from time import sleep

from selenium.webdriver import Chrome

class MySeleniumTests(StaticLiveServerTestCase):
    # fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        # 引用当前类的父类的setUpClass()类去初始化
        super().setUpClass()

        cls.driver = Chrome()
        cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login(self):
        # 一般情况需要get一个URL地址
        # self.driver.get('http://127.0.0.1:8000')

        # Django中不需要指定URL测试地址，由django自启动一个测试环境
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('admin')
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div/form/button').click()
        sleep(5)
