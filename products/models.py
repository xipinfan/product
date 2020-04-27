from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    app_name = models.CharField(max_length=50, verbose_name='APP名称')
    intro = models.TextField(verbose_name='介绍')
    url = models.CharField(default='Https://', verbose_name='链接', max_length=100)
    icon = models.ImageField(verbose_name='图标', upload_to='images/')
    image = models.ImageField(verbose_name='图片', upload_to='images/')

    votes = models.IntegerField(default=1, verbose_name='投票数量')
    pub_data = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.app_name
