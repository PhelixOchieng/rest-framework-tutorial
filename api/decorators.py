from rest_framework import status
from rest_framework.response import Response

from posts.models import Post
from blog.utils import get_user_from_token

def is_owner(func):
    def wrapper(context, request, *args, **kwargs):
        current_user = get_user_from_token(request)

        if current_user is not None:
            try:
                owner = Post.objects.get(pk=kwargs.get('pk')).user
            except Post.DoesNotExist:
                return Response({
                    'status_code': status.HTTP_404_NOT_FOUND,
                    'message': 'This post does not exist'
                })

            print('\n\n{}, {}\n\n'.format(current_user, owner))

            if current_user.id is not owner.id:
                response = {
                    "status_code": status.HTTP_401_UNAUTHORIZED,
                    "message": 'You do not have access to this post'
                }

                return Response(response)
        else:
            response = {
                'status_code': status.HTTP_401_UNAUTHORIZED,
                'message': 'Please log in to continue'
            }

            return Response(response)

        
        return func(context, request, *args, **kwargs)
    
    return wrapper