import time
from django.utils.deprecation import MiddlewareMixin

class LoggerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.start_time = time.time()

        request.body_data = request.body.decode('utf-8') if request.body else ''

    def process_response(self, request, response):
        latency = (time.time() - request.start_time) * 1000

        method = request.method
        path = request.path
        query = request.META.get('QUERY_STRING', '')
        client_ip = request.META.get('REMOTE_ADDR', '')

        status_code = response.status_code

        log_message = (
            f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {method} {path} - {query} {status_code} "
            f"({latency:.2f}ms) {client_ip}\nRequest: {request.body_data}\nResponse: {response.content.decode('utf-8')}\n"
        )

        with open('logs/logs.txt', 'a') as log_file:
            log_file.write(log_message)

        return response