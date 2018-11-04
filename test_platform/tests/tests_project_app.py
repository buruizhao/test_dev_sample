from django.test import TestCase,Client
from project_app.models import Project,Module

# Create your tests here.
# #
# 项目单元测试
#
# #

class ProjectTestCase(TestCase):
    #项目单元测试
    def setUp(self):
        Project.objects.create(name='测试项目',describe='备注测试')

    def test_project_select(self):
        #项目查询测试
        project = Project.objects.get(name='测试项目')
        self.assertEqual(project.describe, '备注测试')

    def test_project_create(self):
        #项目创建测试
        Project.objects.create(name='测试项目02', describe='备注测试02')
        project_create = Project.objects.get(name='测试项目02')
        self.assertEqual(project_create.describe, '备注测试02')

    def test_project_update(self):
        #项目修改测试
        project_update = Project.objects.get(name='测试项目')
        project_update.name = '测试项目03'
        project_update.save()

        project_update_test = Project.objects.get(name='测试项目03')
        self.assertEqual(project_update_test.name, '测试项目03')

    def test_project_delete(self):
        #项目删除测试
        project_delete = Project.objects.get(name='测试项目')
        project_delete.delete()

        project_delete_test = Project.objects.filter(name__contains='测试项目')
        self.assertEqual(len(project_delete_test),0)


class ModuleTestCase(TestCase):
    #模块单元测试
    def setUp(self):
        Project.objects.create(name='测试项目', describe='备注测试')
        Module.objects.create(project=1,name='测试模块',describe='备注测试')


    def test_module_select(self):
        #模块查询测试
        module = Module.objects.get(name='测试模块')
        self.assertEqual(module.describe, '备注测试')

    def test_module_create(self):
        #模块创建测试
        Module.objects.create(name='测试模块02', describe='备注测试02')
        module_create = Module.objects.get(name='测试模块02')
        self.assertEqual(module_create.describe, '备注测试02')

    def test_module_update(self):
        #模块修改测试
        module_update = Module.objects.get(name='测试模块')
        module_update.name = '测试模块03'
        module_update.save()

        module_update_test = Module.objects.get(name='测试模块03')
        self.assertEqual(module_update_test.name, '测试模块03')

    def test_module_delete(self):
        #模块删除测试
        module_delete = Module.objects.get(name='测试模块')
        module_delete.delete()

        module_delete_test = Module.objects.filter(name__contains='测试模块')
        self.assertEqual(len(module_delete_test),0)