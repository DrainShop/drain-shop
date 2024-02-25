from .models import *

class ColorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        page_url = request.path
        request.tag_active_page = page_url.split('/')[1]
        request.uniq_active_page_ = page_url.split('/')[0]
        response = self.get_response(request)
        return response