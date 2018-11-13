from django.test import TestCase,Client
from project_app.models import Project,Module
from django.contrib.auth.models import User

class ProjectManageTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User.objects.create_user('test_project', 'test123@163.com', 'test_password')
        login_data = {'username':'test_project', 'password':'test_password'}
        self.client.post('/login_action/', data=login_data)
        Project.objects.create(name='自动创建项目', describe='备注测试')

    def test_project_manage(self):
        response = self.client.get('/project/project_manage/')
        project_manage_html = response.content.decode('utf-8')
        self.assertEqual(response.status_code, 200)
        self.assertIn('自动创建项目', project_manage_html)
