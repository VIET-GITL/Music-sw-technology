from django.middleware.csrf import get_token
from django.http import JsonResponse

def csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})