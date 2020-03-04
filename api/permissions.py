from rest_framework.permissions import BasePermission
from rest_framework.authtoken.models import Token


class IsOwner(BasePermission):

    def has_permission(self, request, view):
        token = request.META.get('Authorization')
        # user = Token.objects.get(key=)
        print('\n\n\n{}\n\n\n'.format(token))

