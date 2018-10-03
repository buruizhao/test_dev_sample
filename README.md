## test_dev_sample

*2018-09-21*

	*	创建项目test_platform
	*	创建应用user_app
	*	加git过滤文件（.gitignore）
	*	实现简单的登陆功能

*2018-09-26*

	*	增加登录用户信息验证
	*	使用bootstrap简单样式

*2018-10-03*

	*	迁移templates模板文件至项目根目录
	
	"""
	修改配置setting.py文件

	TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        **'DIRS': [os.path.join(BASE_DIR, 'templates')],**
    ...
	"""

	*	页面的bootstrap样式引用修改为本地静态样式
	
	1.	根目录创建static文件夹
	2.	setting.py文件，增加配置

	"""
	STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
	]
	"""

	3.页面引用修改
	
	"""
	{% load static %}
    <link href="{% static 'css/bootstrap.min.css' %}" rel="stylesheet" type="text/css">
    <link href="{%static 'css/signin.css'%}" rel="stylesheet" type="text/css">
	"""

	*	调用页面cookie

	*	调用页面session

	*