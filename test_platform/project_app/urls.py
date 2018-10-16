from django.urls import path
from . import views

urlpatterns = [
	path('project_manage/', views.project_manage), #项目管理
	path('project_manage_create/', views.project_manage_create), #跳转项目管理创建页面
	path('project_manage_update/', views.project_manage_update), #跳转项目管理修改页面
	path('project_module/', views.project_module), #模块管理
	path('project_module_create/', views.project_module_create),  # 跳转项目管理创建页面
	path('project_module_update/', views.project_module_update),  # 跳转项目管理修改页面



]