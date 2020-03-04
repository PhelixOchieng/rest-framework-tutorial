from django.urls import path

from .views import users as user_views
from .views import posts as post_views

urlpatterns = [
    path('users/', user_views.UserListView.as_view()),
    path('users/<int:pk>/', user_views.UserDetailView.as_view()),


    path('posts/', post_views.PostListView.as_view(), name=None),
    path('posts/create/', post_views.PostCreateView.as_view(), name=None),
    path('posts/<int:pk>/', post_views.PostDetailView.as_view(), name=None),
]
