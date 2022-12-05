from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# UserModel = get_user_model()

class Canteen(models.Model):
    canteenId = models.AutoField(primary_key=True)
    canteenName = models.CharField(max_length=30, verbose_name='食堂名称', unique=True)
    canteenAddr = models.CharField(max_length=50, verbose_name='食堂地址', unique=True)
    canteenPhone = models.CharField(max_length=11, verbose_name='食堂电话', unique=True)

    def __str__(self):
        return {'食堂名称': self.canteenName}

    # 自定义表名
    class Meta:
        db_table = 'backend_canteen'


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    userPortrait = models.CharField(max_length=25, verbose_name='用户头像的存储路径', default='')
    userPrefer = models.CharField(max_length=25, verbose_name='用户的口味偏好', default='')
    userExpense = models.FloatField(verbose_name="用户的支出金额", default=0.0)

    # to be continued

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username

    # 自定义表名
    class Meta:
        db_table = 'backend_user'
