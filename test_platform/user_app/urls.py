from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
	path('login_action/', views.login_action),
	path('logout/', views.logout),

]