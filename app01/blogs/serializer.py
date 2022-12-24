from rest_framework import serializers
from app01.models import Blog, MyUser, Merchant


class BlogSerializer(serializers.ModelSerializer):
    blogPosterName = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = '__all__'

    def get_blogPosterName(self, instance):
        user = MyUser.objects.filter(user_ab_id=instance.user_ab_id)
        if user.exists():
            user_obj = user[0]
            return user_obj.username
        else:
            return Merchant.objects.get(user_ab_id=instance.user_ab_id).merchantName
