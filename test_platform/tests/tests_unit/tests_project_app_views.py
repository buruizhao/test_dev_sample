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
    def setUp(self):
        self.client = Client()
        User.objects.create_user('test_project', 'test123@163.com', 'test_password')
        login_data = {'username': 'test_project', 'password': 'test_password'}
        response = self.client.post('/login_action/', data=login_data)

        Project.objects.create(name='初始化项目数据', describe='备注项目测试')
        Module.objects.create(project_id=1,name='初始化模块数据', describe='备注模块测试')

    def test_project_module(self):
        # 模块查询列表
        response = self.client.get('/project/project_module/')
        response_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('初始化模块数据', response_html)
        self.assertIn('备注模块测试', response_html)
        self.assertIn('创建', response_html)
        self.assertIn('修改', response_html)
        self.assertIn('删除', response_html)

    def test_module_create(self):
        # 模块创建
        create = self.client.get('/project/project_module_create/')
        create_html = create.content.decode('utf-8')
        self.assertEqual(create.status_code, 200)
        self.assertIn('关联项目', create_html)
        self.assertIn('模块名称', create_html)

    def test_module_update(self):
        # 模块修改
        update = self.client.get('/project/project_module_update/1/')
        update_html = update.content.decode('utf-8')
        self.assertEqual(update.status_code, 200)
        self.assertIn('初始化模块数据', update_html)
        self.assertIn('备注模块测试', update_html)

    def test_module_delete(self):
        response = self.client.get('/project/project_module/')
        response_html = response.content.decode('utf-8')
        self.assertIn('初始化模块数据', response_html)

        self.client.get('/project/project_module_delete/1/')
        check = self.client.get('/project/project_module/')
        check_html = check.content.decode('utf-8')
        self.assertEqual(check.status_code, 200)
        self.assertNotIn('初始化模块数据', check_html)
