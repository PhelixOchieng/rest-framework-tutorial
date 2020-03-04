from rest_framework import generics, status
from rest_framework.response import Response

from users.models import User
from ..serializers import UserSerializer
from posts.api.serializers import PostSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        super(UserDetailView, self).retrieve(request, *args, **kwargs)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        posts = PostSerializer(instance.post_set.all, many=True)

        response = {
            'status_code': status.HTTP_200_OK,
            'message': 'Successfully retrieved user',
            'result': data
        }

        return Response(response)
    
    def patch(self, request, *args, **kwargs):
        super(UserDetailView, self).patch(request, *args, **kwargs)

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data

        response = {
            'status': status.HTTP_200_OK,
            'message': 'Successfully updated',
            'result': data
        }

        return Response(response)
    
    def delete(self, request, *args, **kwargs):
        super(UserDetailView, self).delete(request, *args, **kwargs)

        response = {
            'status': status.HTTP_200_OK,
            'message': 'Successfully deleted',
        }

        return Response(response)
