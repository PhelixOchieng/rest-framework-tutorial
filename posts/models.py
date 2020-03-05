from django.db import models

from blog.utils import user_directory_path


class Post(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    is_featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to=user_directory_path)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name="Creation date")
    time_modified = models.DateTimeField(auto_now=True, verbose_name="Last modified date")

    def __str__(self):
        return self.title


