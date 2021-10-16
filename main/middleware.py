from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class AuthRequiredMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if not request.user.is_authenticated and not 'register' in request.path and not 'login' in request.path and not 'vk' in request.path and not 'check' in request.path and not 'sendcode' in request.path  and not 'stats' in request.path and not 'plot' in request.path:
            return redirect("/register")