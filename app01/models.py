from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
import os
import uuid

# 创建一个用户的个人文件夹
from django.utils.datetime_safe import datetime


def user_directory_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid.uuid4().hex[:8], ext)
    sub_folder = 'file'
    if ext.lower() in ["jpg", "png", "gif", "jpeg", "image"]:
        sub_folder = "avatar"
    if ext.lower() in ["pdf", "docx"]:
        sub_folder = "document"
    # print(instance.user.id, sub_folder, filename)
    return f'{sub_folder}/{instance.user_ab_id}/{filename}'  # MEDIA_ROOT/avatar/filename


# Create your models here.
# TODO:暂时把所有的表都放在这个app里
UserModel = get_user_model()


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


class Activity(models.Model):
    activityId = models.AutoField(primary_key=True)
    user_ab = models.ForeignKey(UserModel, verbose_name='活动发起者', on_delete=models.CASCADE)
    activityName = models.CharField(max_length=30, verbose_name='活动名称')
    activityBrief = models.CharField(max_length=30, verbose_name='活动简介')
    activityContent = models.FileField(verbose_name='活动详情', upload_to=user_directory_path)
    activityHeadPhoto = models.ImageField(verbose_name='活动头图', upload_to=user_directory_path,
                                          null=True, default='default.jpg')
    activityBegin = models.DateField(verbose_name='活动开始时间', auto_now_add=True)
    activityEnd = models.DateField(verbose_name='活动结束时间', auto_now_add=True)
    activityPersonCnt = models.IntegerField(verbose_name='活动参与人数', default=0)

    def __str__(self):
        return {'活动id': self.activityId, '活动名称': self.activityName}

    # 自定义表名
    class Meta:
        db_table = 'backend_activity'


# 这个模型不用管，我也不知道它是干什么用的
class ActivitySlide(models.Model):
    activity = models.ForeignKey(Activity, verbose_name='活动内容', on_delete=models.DO_NOTHING)
    images = models.ImageField(upload_to='slide', verbose_name='轮播图片')
    sort = models.IntegerField(default=0, verbose_name='排列顺序')
    create_date = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


class Merchant(models.Model):
    # merchantUser = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name="用户")
    merchantId = models.AutoField(primary_key=True)
    user_ab = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name="用户")
    isMerchant = models.BooleanField(verbose_name='是否是商家',
                                     choices=[(True, '是'), (False, '否')])
    merchantName = models.CharField(max_length=30, verbose_name='窗口名', unique=True)
    merchantPassword = models.CharField(max_length=25, verbose_name='窗口登录密码')
    merchantPortrait = models.ImageField(verbose_name='窗口头像', upload_to=user_directory_path)  # 不能为空
    merchantPhone = models.CharField(max_length=11, verbose_name='窗口电话', unique=True)
    merchantStars = models.FloatField(default='10', verbose_name='商家评分')
    merchantAddr = models.CharField(max_length=50, verbose_name='窗口地址', unique=True)
    merchantOpen = models.TimeField(verbose_name='窗口营业起始时间')
    merchantClose = models.TimeField(verbose_name='窗口营业结束时间')
    # merchantHead = models.ForeignKey(Canteen, verbose_name='窗口所属食堂',
    #                                  on_delete=models.CASCADE,
    #                                  related_name='mh')
    merchantHead = models.CharField(max_length=30, verbose_name='窗口所属食堂')
    merchantFollowerCnt = models.IntegerField(verbose_name='收藏人数', default=0)
    # merchantBlogs = models.ForeignKey(Blog, related_name="blog_merchant", on_delete=models.CASCADE)  # 商家发表博客 todo 不实现？

    merchantActivities = models.ManyToManyField(Activity)

    def __str__(self):
        return {'窗口名称': self.merchantName}

    # 自定义表名
    class Meta:
        db_table = 'backend_merchant'


class Dish(models.Model):
    dishId = models.AutoField(primary_key=True)
    user_ab = models.ForeignKey(UserModel, verbose_name='销售窗口', on_delete=models.CASCADE)  # dishSeller
    dishName = models.CharField(max_length=30, verbose_name='菜品名')
    dishPrice = models.FloatField(verbose_name='菜品价格')
    dishPicture = models.ImageField(max_length=25, verbose_name='菜品头像',
                                    null=True, default='default.jpg', upload_to=user_directory_path)
    dishStars = models.FloatField(verbose_name='菜品评分', null=True)
    dishRaw = models.CharField(verbose_name='菜品原料', max_length=50,
                               null=True, default='暂未提供原料信息')
    dishTaste = models.CharField(verbose_name='菜品口味', max_length=30,
                                 null=True, default='暂未提供口味信息')
    dishBrief = models.TextField(verbose_name='菜品简介', max_length=300,
                                 null=True, default='暂未提供菜品简介')
    dishFollowerCnt = models.IntegerField(verbose_name='收藏人数', default=0)
    dishAvailable = models.BooleanField(verbose_name='当日售罄',
                                        choices=[(True, '是'), (False, '否')],
                                        null=True)

    def __str__(self):
        return {'菜品id': self.dishId, '菜品名称': self.dishName}

    # 自定义表名
    class Meta:
        db_table = 'backend_dish'


class Blog(models.Model):
    blogId = models.AutoField(primary_key=True)
    user_ab = models.ForeignKey(UserModel, verbose_name="发布者", related_name="post_blog",
                                on_delete=models.CASCADE)  # 用户或商家发表博客
    blogPrivate = models.BooleanField(verbose_name='是否公开',
                                      choices=[(True, '是'), (False, '否')],
                                      null=True)
    blogTitle = models.CharField(max_length=45, verbose_name='帖子标题')
    blogContent = models.FileField(verbose_name='帖子内容存储路径', upload_to='blogs/contents')
    blogDeliverTime = models.DateTimeField(verbose_name='帖子发布时间', auto_now_add=True)
    blogFavoriterCnt = models.IntegerField(verbose_name='帖子的收藏人数', null=True, default=0)
    blogLikeCnt = models.IntegerField(verbose_name='帖子的喜欢人数', null=True, default=0)

    # 多对多关系
    blogsFavoritedUsers = models.ManyToManyField(UserModel)
    blogsActivitys = models.ManyToManyField(Activity)
    blogsDishes = models.ManyToManyField(Dish)

    def __str__(self):
        return {'帖子id': self.blogId, '帖子标题': self.blogTitle}

    # 自定义表名
    class Meta:
        db_table = 'backend_blog'


class MyUser(models.Model):
    id = models.AutoField(primary_key=True)
    user_ab = models.OneToOneField(UserModel, on_delete=models.CASCADE, verbose_name="用户")  # primary_key=True,
    username = models.CharField(max_length=45, verbose_name='用户昵称', unique=True)
    # userExpense = models.FloatField(verbose_name="用户的支出金额", default=0.0)
    userSignature = models.CharField(max_length=45, verbose_name='用户个性签名',
                                     blank=True, default='这个人很懒，什么也没留下~')
    # userNumber = models.CharField(max_length=15, verbose_name='用户学工号', unique=True)
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
    userFavoriteMerchants = models.ManyToManyField(Merchant)
    userFavoriteBlogs = models.ManyToManyField(Blog)
    userFavoriteDishes = models.ManyToManyField(Dish)
    userActivities = models.ManyToManyField(Activity)

    # to be continued

    def __unicode__(self):
        return self  # .username

    def __str__(self):
        return {'用户姓名': self}  # .username}

    # 自定义表名
    class Meta:
        db_table = 'backend_user'


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
    blogs = models.ManyToManyField(Blog)

    def __str__(self):
        return self.blogLabelContent

    # 自定义表名
    class Meta:
        db_table = 'backend_blog_Label'


#
# class MerchantComment(models.Model):
#     commentId = models.AutoField(primary_key=True)
#     commentContent = models.CharField(max_length=300, verbose_name='评论内容')
#     commentDeliverTime = models.DateTimeField(verbose_name='发布时间')
#     commentSort = models.IntegerField(verbose_name='评论性质',
#                                       choices=((0, '发布'), (1, '收到')))
#
#     merchant = models.ForeignKey(Merchant, related_name="merchant_comment", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return {'评论id': self.commentId, '评论内容': self.commentContent}
#
#     # 自定义表名
#     class Meta:
#         db_table = 'backend_merchant_comment'
#
#
# class UserComment(models.Model):
#     commentId = models.AutoField(primary_key=True)
#     commentContent = models.CharField(max_length=300, verbose_name='评论内容')
#     commentDeliverTime = models.DateTimeField(verbose_name='发布时间')
#     commentSort = models.IntegerField(verbose_name='评论性质',
#                                       choices=((0, '发布'), (1, '收到')))
#
#     user = models.ForeignKey(MyUser, related_name="user_comment", on_delete=models.CASCADE)
#
#     def __str__(self):
#         return {'评论id': self.commentId, '评论内容': self.commentContent}
#
#     # 自定义表名
#     class Meta:
#         db_table = 'backend_user_comment'


class ActivityComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    commenter = models.ForeignKey(UserModel, verbose_name="评论者", on_delete=models.CASCADE)  # 商家或者用户
    commentContent = models.CharField(max_length=300, verbose_name='评论内容')
    commentDeliverTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    # commentSort = models.IntegerField(verbose_name='评论性质',
    #                                   choices=((0, '发布'), (1, '收到')))

    activity = models.ForeignKey(Activity, related_name="activity_comment", on_delete=models.CASCADE)

    def __str__(self):
        return {'评论id': self.commentId, '评论内容': self.commentContent}

    # 自定义表名
    class Meta:
        db_table = 'backend_activity_comment'


class BlogComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    commenter = models.ForeignKey(UserModel, verbose_name="评论者", on_delete=models.CASCADE)  # 商家或者用户
    commentContent = models.CharField(max_length=300, verbose_name='评论内容')
    commentDeliverTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    # commentSort = models.IntegerField(verbose_name='评论性质',
    #                                   choices=((0, '发布'), (1, '收到')))

    blog = models.ForeignKey(Blog, related_name="blog_comment", on_delete=models.CASCADE)

    def __str__(self):
        return {'评论id': self.commentId, '评论内容': self.commentContent}

    # 自定义表名
    class Meta:
        db_table = 'backend_blog_comment'


class DishComment(models.Model):
    commentId = models.AutoField(primary_key=True)
    commenter = models.ForeignKey(UserModel, verbose_name="评论者", on_delete=models.CASCADE)  # 商家或者用户
    commentContent = models.CharField(max_length=300, verbose_name='评论内容')
    commentDeliverTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
    # commentSort = models.IntegerField(verbose_name='评论性质',
    #                                   choices=((0, '发布'), (1, '收到')))

    dish = models.ForeignKey(Dish, related_name="dish_comment", on_delete=models.CASCADE)

    def __str__(self):
        return {'评论id': self.commentId, '评论内容': self.commentContent}

    # 自定义表名
    class Meta:
        db_table = 'backend_dish_comment'


class FeedBack(models.Model):
    # poster = models.ForeignKey(UserModel, verbose_name="发布者", on_delete=models.CASCADE)   # 匿名或实名
    content = models.CharField(max_length=300, verbose_name="用户反馈")
    commentDeliverTime = models.DateTimeField(verbose_name='发布时间', auto_now_add=True)
# class CommentReplyComment(models.Model):
#     commentId = models.ForeignKey(Comment, verbose_name='评论id',
#                                   on_delete=models.CASCADE, related_name='crc_ci')
#     replyCommentId = models.ForeignKey(Comment, primary_key=True, verbose_name='回评id',
#                                        on_delete=models.CASCADE, related_name='crc_rci')


# # 用户与评论
# class UserDeliverOrReceivedComments(models.Model):
#     commentId = models.ForeignKey(Comment, primary_key=True, verbose_name='帖子id',
#                                   on_delete=models.CASCADE, related_name='uc_ci')
#     userId = models.ForeignKey(MyUser, verbose_name='用户id',
#                                on_delete=models.CASCADE, related_name='uc_ui')
#     commentSort = models.IntegerField(verbose_name='评论性质',
#                                       choices=((0, '发布'), (1, '收到')))


# 窗口与评论
# class MerchantDeliverOrReceivedComments(models.Model):
#     commentId = models.ForeignKey(Comment, primary_key=True, verbose_name='帖子id',
#                                   on_delete=models.CASCADE, related_name='mc_ci')
#     merchantId = models.ForeignKey(Merchant, verbose_name='窗口id',
#                                    on_delete=models.CASCADE, related_name='mc_mi')
