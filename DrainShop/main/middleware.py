import time
from django.http import HttpResponse
import requests


class ColorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        page_url = request.path
        request.tag_active_page = page_url.split('/')[1]
        request.uniq_active_page_ = page_url.split('/')[0]
        response = self.get_response(request)
        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


requests_count = {}
class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        timestamp = int(time.time())
        user_ip = get_client_ip(request)

        if user_ip not in requests_count:
            requests_count[user_ip] = {
                'count': 1,
                'timestamp': timestamp
            }
        else:
            if timestamp == requests_count[user_ip]["timestamp"] and requests_count[user_ip]["count"] >= 4:
                return HttpResponse({'error': 'Слишком много запросов'}, status=429)
            elif timestamp == requests_count[user_ip]["timestamp"] and requests_count[user_ip]["count"] < 4:
                requests_count[user_ip]['count'] += 1
            elif timestamp != requests_count[user_ip]["timestamp"]:
                requests_count[user_ip]['count'] = 1
                requests_count[user_ip]['timestamp'] = timestamp

        response = self.get_response(request)
        print(requests_count)
        return response






