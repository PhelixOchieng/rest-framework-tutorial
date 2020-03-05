from django.db import models
from django.contrib.auth.models import AbstractUser

from blog.utils import user_directory_path

class User(AbstractUser):
    avatar = models.ImageField(upload_to=user_directory_path, default='default.jpg')
    pass
