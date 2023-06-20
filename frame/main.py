from quopri import decodestring

from frame.requests import PostRequest, GetRequest


class PageNotFound:
    def __call__(self, request):
        return 'Error!\nPage Not Found'


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        # Request GET \ POST
        request = {}
        method = environ['REQUEST_METHOD']
        request['method'] = method

        if method == 'POST':
            data = PostRequest().get_request_params(environ)
            request['data'] = Framework.decode_value(data)
            print(f'Received POST request: {request}')
        if method == 'GET':
            request_params = GetRequest().get_request_params(environ)
            request['request_params'] = Framework.decode_value(request_params)
            print(f'Received GET parameters: {request}')

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound()

        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]

    @staticmethod
    def decode_value(data):
        new_data = {}
        for k, v in data.items():
            val = bytes(v.replace('%', '=').replace("+", " "), 'UTF-8')
            val_decode_str = decodestring(val).decode('UTF-8')
            new_data[k] = val_decode_str
        return new_data
