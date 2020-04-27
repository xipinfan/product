from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from django.utils import timezone

# Create your views here.
def products_list(request):
    return render(request, 'products.html')

@login_required
def publsh(request):
    if request.method == 'GET':
        return render(request, 'publsh.html')
    elif request.method == 'POST':
        app_name = request.POST['APP名称']
        intro = request.POST['介绍']
        url = request.POST['APP链接'] 
        #try:
        icon = request.FILES['APP图标']
        image = request.FILES['大图']
        product = Product()
        product.app_name = app_name
        product.intro = intro
        product.url = url
        product.icon = icon
        product.image = image
        product.pub_data = timezone.datetime.now()
        product.hunter = request.user
        product.save()
        return redirect('主页面')
        #except Exception as err:
            #return render(request, 'publsh.html', {'错误':'请上传图片'})