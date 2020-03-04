from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from posts.models import Post

from .. import serializers
from ..utils import get_user_from_token
# from ..permissions import IsOwner


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated, )

    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def create(self, request, *args, **kwargs):
        super(PostCreateView, self).create(request, *args, **kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data
        }

        return Response(response)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):
        super(PostDetailView, self).retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "result": data
        }
        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully updated",
            "result": data
        }
        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully deleted"
        }

        current_user = get_user_from_token(request)
        owner = Post.objects.get(pk=kwargs.get('pk')).user

        if current_user.id is not owner.id:
            response['status_code'] = status.HTTP_401_UNAUTHORIZED
            response['message'] = 'You do not have access to this post'
        else:
            super(PostDetailView, self).delete(request, *args, **kwargs)

        return Response(response)

