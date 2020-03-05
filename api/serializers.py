from rest_framework import serializers

from users.models import User
from posts.models import Post



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'avatar')


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title', 'content', 'image', 'is_featured', 'time_created', 'time_modified')

    def save(self, **kwargs):
        super(PostSerializer, self).save(**kwargs)
