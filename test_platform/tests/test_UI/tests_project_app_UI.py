from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver import Chrome
from time import sleep
from django.contrib.auth.models import User
from project_app.models import Project,Module
from django.test import Client


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
		self.client = Client()
		User.objects.create_user('admin', 'admin@163.com', 'admin')
		login_data = {'username':'admin','password':'admin'}
		self.client.post('/login_action/', data=login_data)
		Project.objects.create(name='初始化项目数据', describe='备注测试')

	def test_project_create(self):
		# 项目新建
		self.driver.get('%s%s' % (self.live_server_url, '/project/project_manage/'))
		self.driver.find_element_by_id("button_create").click()
		sleep(2)
		create_text = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/h2').text
		self.assertEquals('创建项目',create_text)
