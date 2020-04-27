from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html');
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        passname1 = request.POST['密码']
        passname2 = request.POST['确认密码']
        try:
            if User.objects.get(username=user_name):
                return render(request,'signup.html',{'name1':'用户名已存在'})
        except User.DoesNotExist:
                if passname1 == passname2:
                    User.objects.create_user(username= user_name, password= passname1)
                    return render(request, '主页面', {'user1': user_name})
                else:
                    return render(request, 'signup.html', {'name1': '两次输入的密码不一致'})
def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        user_name = request.POST['用户名']
        pass_name = request.POST['密码']
        user = auth.authenticate(username= user_name, password= pass_name)
        if user is None:
            return render(request, 'login.html',{'name1': '用户名或者密码错误'})
        else:
            auth.login(request, user)
            return redirect('主页面')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('主页面')


