from django.db import models

# Create your models here.

#创建项目表
class Project(models.Model):
	name = models.CharField('名称', max_length=100, blank=False, null=True)
	describe = models.TextField('备注', default='')
	status = models.BooleanField('状态', default=True)
	create_time = models.DateTimeField('创建时间', auto_now=True)
	update_time = models.DateTimeField('更新时间', auto_now=True)

	#影响关联数据显示
	def __str__(self):
		return self.name

#创建模块表
class Module(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	name = models.CharField('名称', max_length=100, blank=False, default='')
	describe = models.TextField('备注', default='')
	create_time = models.DateTimeField('创建时间', auto_now=True)
	update_time = models.DateTimeField('更新时间', auto_now=True)

	# 影响关联数据显示
	def __str__(self):
		return self.name