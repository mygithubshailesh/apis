"""from functools import wraps
from rest_framework.response import Response
from rest_framework.status import HTTP_401_UNAUTHORIZED

def require_authentication(view_func):
    @wraps(view_func)
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({'detail': 'Unauthorized'}, status=HTTP_401_UNAUTHORIZED)
        return view_func(self, request, *args, **kwargs)
    return wrapper"""

