from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User


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

    def setUp(self):
        User.objects.create_user('admin', 'admin@163.com', 'admin')

    def test_login_error_null(self):
        # 用户名或密码不能为空
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/form/button').click()
        error_text = self.driver.find_element_by_id("error").text
        self.assertEqual('用户名或密码不能为空，请重新登录！', error_text)
        sleep(2)

    def test_login_error_error(self):
        # 用户名或密码错误
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('error')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('error')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/form/button').click()
        error_text = self.driver.find_element_by_id("error").text
        self.assertEqual('用户名或密码错误，请重新登录！', error_text)
        sleep(2)

    def test_login_success(self):
        # 一般情况需要get一个URL地址
        self.driver.get('%s%s' % (self.live_server_url, '/'))
        username_input = self.driver.find_element_by_name("username")
        username_input.send_keys('admin')
        password_input = self.driver.find_element_by_name("password")
        password_input.send_keys('admin')
        sleep(2)
        self.driver.find_element_by_xpath('/html/body/div/form/button').click()
        success_text = self.driver.find_element_by_class_name('navbar-brand').text
        self.assertEqual('测试平台', success_text)
        sleep(2)


