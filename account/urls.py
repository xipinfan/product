from django.urls import path,include
from . import views

urlpatterns = [
    #path('login/', ),
    path('signup/', views.signup, name='注册页面'),
    path('login/', views.login, name='登录页面'),
]