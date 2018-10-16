from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
	path('index/', views.index),
	path('accounts/login/', views.index),
	path('login_action/', views.login_action),
	path('logout/', views.logout),

]