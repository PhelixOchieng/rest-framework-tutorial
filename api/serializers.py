from rest_framework import serializers

from users.models import User
from posts.models import Post



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('user', 'title', 'content', 'is_featured', 'image')