from django.urls import path
from project_app.views import project_manage_views,project_module_views

urlpatterns = [
    #项目管理
    path('project_manage/', project_manage_views.project_manage), #项目管理
    path('project_manage_create/', project_manage_views.project_manage_create), #跳转项目管理创建页面
    path('project_manage_update/<int:project_id>/', project_manage_views.project_manage_update), #跳转项目管理修改页面
    path('project_manage_delete/<int:project_id>/', project_manage_views.project_manage_delete), #项目管理删除

    #模块管理
    path('project_module/', project_module_views.project_module), #模块管理
    path('project_module_create/', project_module_views.project_module_create),  # 跳转项目管理创建页面
    path('project_module_update/<int:module_id>/', project_module_views.project_module_update),  # 跳转项目管理修改页面
    path('project_module_delete/<int:module_id>/', project_module_views.project_module_delete), #项目管理删除

]