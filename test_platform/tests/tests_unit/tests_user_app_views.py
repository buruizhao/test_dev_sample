from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
# #
# index页面的测试
# 登陆处理的的测试
# 退出登陆的测试
# #

class IndexTest(TestCase):
    # index页面的测试

    def setUp(self):
        self.client = Client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        # 汉字转码
        # print(response.content.decode("UTF-8"))

        # 断言index模板页面是否可用的
        self.assertTemplateUsed(response, "index.html")

class LoginActionTest(TestCase):
    # 登陆处理的的测试
    def setUp(self):
        User.objects.create_user('test_username','test_username@test.com','test_password')
        self.client = Client()
        login_data = {'username': 'test_username1', 'password': 'test_password1'}
        response = self.client.post('/login_action/', data=login_data)
        # print(response.content.decode("UTF-8"))

    def test_user_isnull(self):
        # 用户名或密码不能为空
        login_data = {'username':'','password':''}
        response = self.client.post('/login_action/', data=login_data)
        login_html = response.content.decode("UTF-8")

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '用户名或密码不能为空，请重新登录！')
        self.assertIn('用户名或密码不能为空，请重新登录！',login_html)

    def test_user_error(self):
        # 用户名或密码错误
        login_data = {'username':'a','password':'b'}
        response = self.client.post('/login_action/', data=login_data)
        login_html = response.content.decode("UTF-8")

        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, '用户名或密码错误，请重新登录！')
        self.assertIn('用户名或密码错误，请重新登录！',login_html)

    def test_user_sucess(self):
        # 登陆成功
        login_data = {'username':'test_username','password':'test_password'}
        response = self.client.post('/login_action/', data=login_data)

        # 因登陆成功后只跳转，不能返回页面，所以不能断言页面的元素
        self.assertEqual(response.status_code, 302)

class LogoutTest(TestCase):
    # 退出登陆的测试
    def setUp(self):
        User.objects.create_user('test_username','test@163.com','test_password')
        self.client = Client()

        login_data = {'username':'test_username','password':'test_password'}
        response = self.client.post('/login_action/', data=login_data)

    def test_user_logout(self):
        logout_response = self.client.get('/logout/')
        self.assertEqual(logout_response.status_code, 302)
