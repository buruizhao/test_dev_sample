from django.test import TestCase,Client
from django.contrib.auth.models import User

# Create your tests here.
# #
# User用户的测试
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
