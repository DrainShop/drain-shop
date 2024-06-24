from .models import Tag

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        request.tags = Tag.objects.all()



        response = self.get_response(request)
        return response