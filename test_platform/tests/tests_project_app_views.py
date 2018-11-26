from django.test import TestCase,Client
from project_app.models import Project,Module
from django.contrib.auth.models import User

class ProjectManageTestCase(TestCase):
    # 项目管理
    def setUp(self):
        self.client = Client()
        User.objects.create_user('test_project', 'test123@163.com', 'test_password')
        login_data = {'username':'test_project', 'password':'test_password'}
        self.client.post('/login_action/', data=login_data)
        Project.objects.create(name='初始化项目数据', describe='备注测试')

    def test_project_manage(self):
        # 项目管理页面项目列表查询
        response = self.client.get('/project/project_manage/')
        project_manage_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('初始化项目数据', project_manage_html)
        self.assertIn('创建', project_manage_html)
        self.assertIn('修改', project_manage_html)
        self.assertIn('删除', project_manage_html)

    def test_project_create(self):
        # 项目管理创建
        response = self.client.get('/project/project_manage_create/')
        create_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('创建项目', create_html)

    def test_project_update(self):
        # 项目管理修改
        Project.objects.create(name='项目修改',describe='项目修改备注')
        response = self.client.get('/project/project_manage_update/2/')
        update_html = response.content.decode('utf-8')
        print(update_html)
        self.assertEqual(response.status_code, 200)
        self.assertIn('项目修改', update_html)
        self.assertIn('项目修改备注', update_html)

    def test_project_delete(self):
        # 项目信息删除
        Project.objects.create(name='需要删除的项目',describe='删除项目的备注')
        response = self.client.get('/project/project_manage/')
        first_html = response.content.decode('utf-8')
        self.assertIn('需要删除的项目', first_html)

        self.client.get('/project/project_manage_delete/2/')
        check_response = self.client.get('/project/project_manage/')
        check_html = check_response.content.decode('utf-8')
        self.assertEqual(check_response.status_code, 200)
        self.assertNotIn('需要删除的项目', check_html)

class ProjectModuleTestCase(TestCase):
    # 模块管理
    def SetUp(self):
        self.client = Client()
        User.objects.create_user('testusername','test@123.com','testpassword')
        login_data =
