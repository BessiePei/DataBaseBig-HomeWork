from django.db import models


# Create your models here.

class User(models.Model):
    # 如果没有指定主键的话Django会自动新增一个自增id作为主键
    userName = models.CharField(max_length=30, verbose_name='用户名', default='null')
    userPassword = models.CharField(max_length=25, verbose_name='用户密码', default='123456')
    userPortrait = models.CharField(max_length=25, verbose_name='用户头像的存储路径', default='')
    userPrefer = models.CharField(max_length=25, verbose_name='用户的口味偏好', default='')
    userExpense = models.FloatField(verbose_name="用户的支出金额", default=0.0)

    # to be continued

    def __unicode__(self):
        return self.userName

    def __str__(self):
        return self.userName

    # 自定义表名
    class Meta:
        db_table = 'backend_user'


