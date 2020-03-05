from rest_framework.authtoken.models import Token

def get_user_from_token(request):

    try:
        headers = request.META
        token = headers.get('HTTP_AUTHORIZATION', '').split(' ')[-1]
    except:
        token = request

    try:
        user = Token.objects.get(key=token).user
    except Token.DoesNotExist:
        user = None
    
    return user