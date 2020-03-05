from rest_framework import serializers

from users.models import User
from posts.models import Post



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_featured', 'image')

    def save(self, **kwargs):
        super(PostSerializer, self).save(**kwargs)
