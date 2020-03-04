from rest_framework.authtoken.models import Token

def get_user_from_token(request):
    headers = request.META
    key = headers.get('HTTP_AUTHORIZATION').split(' ')[-1]

    try:
        user = Token.objects.get(key=key).user
    except Token.DoesNotExist:
        user = None
    
    return user