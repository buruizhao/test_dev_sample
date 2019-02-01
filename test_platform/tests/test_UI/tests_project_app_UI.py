from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project,Module


class ProjectAppTests(StaticLiveServerTestCase):
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
		Project.objects.create(name='初始化项目数据', describe='备注测试')

	def test_project_create(self):
		# 测试项目新建

		# 先登录
		self.driver.get('%s%s' % (self.live_server_url, '/'))
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('admin')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('admin')
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div/form/button').click()

		# 进入创建项目页面
		self.driver.find_element_by_id("button_create").click()
		sleep(2)
		create_text = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/h2').text
		self.assertEquals('创建项目',create_text)

