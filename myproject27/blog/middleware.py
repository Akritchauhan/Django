import datetime
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self, request):
        print(f"Request received at {datetime.datetime.now()} for path: {request.path}")

    def process_response(self, request, response):
        print(f"Response sent at {datetime.datetime.now()} for path: {request.path}")
        return response

class BlockIPMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ['127.0.0.1']  # Example blocked IP

    def process_request(self, request):
        ip =request.META.get('REMOTE_ADDR')
        if ip in self.BLOCKED_IPS:
            return HttpResponse("Your IP is blocked.", status=403)
    