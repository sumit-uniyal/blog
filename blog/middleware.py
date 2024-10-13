from django.shortcuts import redirect
from django.urls import resolve
from django.conf import settings
from django.http import JsonResponse


class LoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        
        requested_url = request.path_info
        
        is_ajax_request = request.headers.get('x-requested-with') == 'XMLHttpRequest'
        
        if (requested_url.startswith('/adminpanel') or requested_url.startswith('/ajax')) and not request.user.is_authenticated:
            if is_ajax_request:
                return JsonResponse({'not_authenticated': True, 'login_url': settings.LOGIN_URL}, status=401)
            return redirect(settings.LOGIN_URL)

        
        if requested_url.startswith('/adminpanel') and not request.user.is_superuser:
            return redirect(settings.CUSTOMER_DASHBOARD)
        
        response = self.get_response(request)
        return response