from django.urls import path
from . import views

urlpatterns = [
    #path('login/', ),
    path('publsh/', views.publsh, name= '发布页面'),
]