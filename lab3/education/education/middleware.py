import logging
from django.http import HttpResponse


class ErrorMiddleware:
    async_capable = True

    def __init__(self, get_response):
        self._get_response = get_response

    def __call__(self, request):
        response = self._get_response(request)
        return response

    def process_exception(self, request, exception):
        logger = logging.getLogger(request)
        logger.error(str(exception))
        return HttpResponse('Exception')
