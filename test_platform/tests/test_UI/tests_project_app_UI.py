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
		Project.objects.create(name='初始化项目数据2', describe='备注测试2')

	def test_project_create(self):
		# 测试项目创建
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

	def test_project_update(self):
		# 测试项目修改
		# 先登录
		self.driver.get('%s%s' % (self.live_server_url, '/'))
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('admin')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('admin')
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div/form/button').click()
		# 进入修改页面
		self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a[1]').click()
		sleep(2)
		update_text = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/h2').text
		self.assertEqual('修改项目',update_text)
		update_project_name = self.driver.find_element_by_xpath('//*[@id="id_name"]').get_attribute('value')
		self.assertIn('初始化项目数据',update_project_name)

	def test_project_delete(self):
		# 测试删除
		# 先登录
		self.driver.get('%s%s' % (self.live_server_url, '/'))
		username_input = self.driver.find_element_by_name("username")
		username_input.send_keys('admin')
		password_input = self.driver.find_element_by_name("password")
		password_input.send_keys('admin')
		sleep(2)
		self.driver.find_element_by_xpath('/html/body/div/form/button').click()

		# 删除校验
		delete_1 = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[1]/td[2]').text
		print(delete_1)
		self.assertEqual('初始化项目数据', delete_1)
		sleep(5)

		# self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[1]/td[7]/a[2]').click()
		# delete_text = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div/table/tbody/tr[1]/td[2]').text
		# print(delete_text)
		# self.assertIn('初始化项目数据',delete_text)