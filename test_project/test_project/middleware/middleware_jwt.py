from django.http import JsonResponse
from test_project.utils.jwt_utils import verify_jwt


class JWTAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/login/'):
            return self.get_response(request)

        token = request.COOKIES.get('access_token')
        print(token)
        if token:
            user_id = verify_jwt(token)
            if user_id:
                request.user_id = user_id
            else:
                return JsonResponse(
                    {'error': 'Invalid or expired token'}, status=401
                )
        else:
            return JsonResponse(
                {'error': 'Authentication required'}, status=401
            )
        return self.get_response(request)
