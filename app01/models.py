from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import uuid


# 创建一个用户的个人文件夹
def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
    return os.path.join(instance.user.id, sub_folder, filename)


# Create your models here.
# TODO:暂时把所有的表都放在这个app里
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


class Comment(models.Model):
    commentId = models.AutoField(primary_key=True)
    commentContent = models.CharField(max_length=300, verbose_name='评论内容')
    commentDeliverTime = models.DateTimeField(verbose_name='发布时间')

    def __str__(self):
        return {'评论id': self.commentId, '评论内容': self.commentContent}

    # 自定义表名
    class Meta:
        db_table = 'backend_comment'


class CommentReplyComment(models.Model):
    commentId = models.ForeignKey(Comment, verbose_name='评论id',
                                  on_delete=models.CASCADE, related_name='crc_ci')
    replyCommentId = models.ForeignKey(Comment, primary_key=True, verbose_name='回评id',
                                       on_delete=models.CASCADE, related_name='crc_rci')


class Activity(models.Model):
    activityId = models.AutoField(primary_key=True)
    activityName = models.CharField(max_length=30, verbose_name='活动名称')
    activityBrief = models.CharField(max_length=30, verbose_name='活动简介')
    activityContent = models.FileField(verbose_name='活动详情', upload_to=user_directory_path)
    activityHeadPhoto = models.ImageField(verbose_name='活动头图', upload_to=user_directory_path,
                                          null=True, default='default.jpg')
    activityBegin = models.DateTimeField(verbose_name='活动开始时间')
    activityEnd = models.DateTimeField(verbose_name='活动结束时间')
    activityPersonCnt = models.IntegerField(verbose_name='活动参与人数', default=0)

    def __str__(self):
        return {'活动id': self.activityId, '活动名称': self.activityName}

    # 自定义表名
    class Meta:
        db_table = 'backend_activity'


class Merchant(models.Model):
    merchantId = models.AutoField(primary_key=True)
    merchantName = models.CharField(max_length=30, verbose_name='窗口名', unique=True)
    merchantPassword = models.CharField(max_length=25, verbose_name='窗口登录密码')
    merchantPortrait = models.ImageField(max_length=25, verbose_name='窗口头像',
                                         null=True, default='default.jpg', upload_to=user_directory_path)
    merchantPhone = models.CharField(max_length=11, verbose_name='窗口电话', unique=True)
    merchantStars = models.FloatField(verbose_name='商家评分')
    merchantAddr = models.CharField(max_length=50, verbose_name='窗口地址', unique=True)
    merchantOpen = models.TimeField(verbose_name='窗口营业起始时间')
    merchantClose = models.TimeField(verbose_name='窗口营业结束时间')
    merchantHead = models.ForeignKey(Canteen, verbose_name='窗口所属食堂',
                                     on_delete=models.CASCADE,
                                     related_name='mh')
    merchantFollowerCnt = models.IntegerField(verbose_name='收藏人数')

    merchantActivityId = models.ManyToManyField(Activity)

    def __str__(self):
        return {'窗口名称': self.merchantName}

    # 自定义表名
    class Meta:
        db_table = 'backend_merchant'


class Dish(models.Model):
    dishId = models.AutoField(primary_key=True)
    dishName = models.CharField(max_length=30, verbose_name='菜品名')
    dishPrice = models.FloatField(verbose_name='菜品价格')
    dishPicture = models.ImageField(max_length=25, verbose_name='菜品头像',
                                    null=True, default='default.jpg', upload_to=user_directory_path)
    dishStars = models.FloatField(verbose_name='菜品评分')
    dishRaw = models.CharField(verbose_name='菜品原料', max_length=50,
                               null=True, default='暂未提供原料信息')
    dishTaste = models.CharField(verbose_name='菜品口味', max_length=30,
                                 null=True, default='暂未提供口味信息')
    dishBrief = models.TextField(verbose_name='菜品简介', max_length=300,
                                 null=True, default='暂未提供菜品简介')
    dishFollowerCnt = models.IntegerField(verbose_name='收藏人数')
    dishAvailable = models.BooleanField(verbose_name='当日售罄',
                                        choices=[(True, '是'), (False, '否')],
                                        null=True)
    dishSeller = models.ForeignKey(Merchant, verbose_name='销售窗口',
                                   on_delete=models.CASCADE,
                                   related_name='ds')

    def __str__(self):
        return {'菜品id': self.dishId, '菜品名称': self.dishName}

    # 自定义表名
    class Meta:
        db_table = 'backend_dish'


class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    # userExpense = models.FloatField(verbose_name="用户的支出金额", default=0.0)
    userSignature = models.CharField(max_length=45, verbose_name='用户个性签名',
                                     blank=True, default='这个人很懒，什么也没留下~')
    userNumber = models.CharField(max_length=15, verbose_name='用户学工号', unique=True)
    sex_choice = (
        (0, '女性'),
        (1, '男性'),
    )
    userSex = models.IntegerField(verbose_name='用户性别', choices=sex_choice,
                                  null=True, default=1)  # choices关键字固定的
    userGrade = models.CharField(max_length=25, verbose_name='用户年级', blank=True)
    userPortrait = models.ImageField(max_length=25, verbose_name='用户头像',
                                     null=True, default='default.jpg', upload_to=user_directory_path)
    userPrefer = models.CharField(max_length=25, verbose_name='用户的口味偏好',
                                  blank=True, default='')
    # 设置多对多关系
    userFavoriteMerchantId = models.ManyToManyField(Merchant)
    userFavoriteDishId = models.ManyToManyField(Dish)
    userActivityId = models.ManyToManyField(Activity)

    # to be continued

    def __unicode__(self):
        return self.username

    def __str__(self):
        return {'用户姓名': self.username}

    # 自定义表名
    class Meta:
        db_table = 'backend_user'

# 用户与评论
class UserDeliverOrReceivedComments(models.Model):
    commentId = models.ForeignKey(Comment, primary_key=True, verbose_name='帖子id',
                                  on_delete=models.CASCADE, related_name='uc_ci')
    userId = models.ForeignKey(User, verbose_name='用户id',
                               on_delete=models.CASCADE, related_name='uc_ui')
    commentSort = models.IntegerField(verbose_name='评论性质',
                                      choices=((0, '发布'), (1, '收到')))


# 窗口与评论
class MerchantDeliverOrReceivedComments(models.Model):
    commentId = models.ForeignKey(Comment, primary_key=True, verbose_name='帖子id',
                                  on_delete=models.CASCADE, related_name='mc_ci')
    merchantId = models.ForeignKey(Merchant, verbose_name='窗口id',
                                   on_delete=models.CASCADE, related_name='mc_mi')
    commentSort = models.IntegerField(verbose_name='评论性质',
                                      choices=((0, '发布'), (1, '收到')))


class Blog(models.Model):
    blogId = models.AutoField(primary_key=True)
    blogPrivate = models.BooleanField(verbose_name='是否公开',
                                      choices=[(True, '是'), (False, '否')],
                                      null=True)
    blogTitle = models.CharField(max_length=45, verbose_name='帖子标题')
    blogContent = models.FileField(verbose_name='帖子内容存储路径', upload_to='blogs/contents')
    blogDeliverTime = models.DateTimeField(verbose_name='帖子发布时间')
    blogFavoriterCnt = models.IntegerField(verbose_name='帖子的收藏人数', null=True, default=0)
    blogLikeCnt = models.IntegerField(verbose_name='帖子的喜欢人数', null=True, default=0)

    # 多对多关系
    blogsFavoritedUserIds = models.ManyToManyField(User)
    blogsActivitys = models.ManyToManyField(Activity)
    blogsDishes = models.ManyToManyField(Dish)

    def __str__(self):
        return {'帖子id': self.blogId, '帖子标题': self.blogTitle}

    # 自定义表名
    class Meta:
        db_table = 'backend_blog'


class BlogUnderComments(models.Model):
    commentId = models.ForeignKey(Comment, primary_key=True, verbose_name='帖子id',
                                  on_delete=models.CASCADE, related_name='bc_ci')
    blogId = models.ForeignKey(Blog, verbose_name='帖子id',
                               on_delete=models.CASCADE, related_name='bc_bi')


class BlogPicture(models.Model):
    blogPictureId = models.AutoField(primary_key=True)
    blogPicture = models.ImageField(max_length=25, verbose_name='帖子照片',
                                    null=True, default='default.jpg', upload_to=r'blogs/imgs')
    blogId = models.ManyToManyField(Blog)

    # 自定义表名
    class Meta:
        db_table = 'backend_blog_picture'


class BlogLabel(models.Model):
    blogLabelId = models.AutoField(primary_key=True)
    blogLabelContent = models.CharField(max_length=30, verbose_name='标签名称', unique=True)
    blogId = models.ManyToManyField(Blog)

    def __str__(self):
        return self.blogLabelContent

    # 自定义表名
    class Meta:
        db_table = 'backend_blog_Label'


class UserDeliverBlog(models.Model):
    blogId = models.ForeignKey(Blog, primary_key=True,
                               verbose_name='帖子id', on_delete=models.CASCADE,
                               related_name='ubi')
    userId = models.ForeignKey(User, verbose_name='发布者id',
                               on_delete=models.CASCADE, related_name='ub_ui')

    def __str__(self):
        return {'帖子id': self.blogId, '用户id': self.userId}

    class Meta:
        db_table = 'backend_UserDeliverBlog'


class MerchantDeliverBlog(models.Model):
    blogId = models.ForeignKey(Blog, primary_key=True,
                               verbose_name='帖子id', on_delete=models.CASCADE,
                               related_name='mbi')
    merchantId = models.ForeignKey(Merchant, verbose_name='发布者id',
                                   on_delete=models.CASCADE, related_name='mb_mi')

    def __str__(self):
        return {'帖子id': self.blogId, '商家id': self.merchantId}

    class Meta:
        db_table = 'backend_MerchantDeliverBlog'
