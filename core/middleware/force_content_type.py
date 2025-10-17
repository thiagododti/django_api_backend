from django.http import JsonResponse

class EnforceJSONContentTypeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se está acessando o endpoint de token
        if request.path.startswith('/api/token/') and request.method == 'POST':
            if request.content_type != 'application/json':
                return JsonResponse(
                    {'detail': 'Content-Type must be application/json'},
                    status=415
                )
        return self.get_response(request)
