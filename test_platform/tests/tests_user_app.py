from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
# #
# User用户的测试
# index页面的测试
# 登陆处理的的测试
# #

class UserTestCase(TestCase):
    # User用户的测试

    def setUp(self):
        # User用户数据初始化
        User.objects.create_user('testDev01','testDev01@123.com','test123')

    def test_user_select(self):
        # 测试数据查询是否正确
        user_select = User.objects.get(username='testDev01')
        self.assertEqual(user_select.email,'testDev01@123.com')

    def test_user_create(self):
        # 测试数据创建
        User.objects.create_user('testDev02', 'testDev02@456.com', 'test456')
        user_create = User.objects.get(username='testDev02')
        self.assertEqual(user_create.email,'testDev02@456.com')

    def test_user_update(self):
        # 测试数据修改
        user_update = User.objects.filter(username__contains='testDev01')[0]
        # username = User.objects.get(username='testDev01')
        user_update.username = 'testDev03'
        user_update.email = 'testDev03@456.com'
        user_update.save()

        user_update_test = User.objects.get(username ='testDev03')

        self.assertEqual(user_update_test.email, 'testDev03@456.com')

    def test_user_delete(self):
        # 测试数据删除
        user_delete = User.objects.filter(username__contains='testDev01')
        # username = User.objects.get(username='testDev01')
        user_delete.delete()

        user_delete_test = User.objects.filter(username__contains='testDev01')
        self.assertEqual(len(user_delete_test),0)


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

    def test_user_logout(self):
        # 退出登陆
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 302)

