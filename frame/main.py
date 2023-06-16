class PageNotFound:
    def __call__(self, request):
        return 'Error!\nPage Not Found'


class Framework:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, env, response):
        path = env['PATH_INFO']

        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.routes:
            view = self.routes[path]
        else:
            view = PageNotFound()
        request = {}

        for front in self.fronts:
            front(request)

        code, body = view(request)
        response(code, [('Content-Type', 'text/html')])
        return [body.encode('utf-8')]
