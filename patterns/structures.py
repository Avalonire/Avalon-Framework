from time import time


# Routes decorator
class AppRoute:
    def __init__(self, routes, url):
        self.routes = routes
        self.url = url

    def __call__(self, cls):
        self.routes[self.url] = cls()


class TimeLogger:
    def __init__(self, name):
        self.name = name

    def __call__(self, cls):
        def logit(method):
            def logged(*args, **kwargs):
                ts = time()
                result = method(*args, **kwargs)
                te = time()
                delta = te - ts
                print(f'Log -> {self.name}')
                print(f'Page loading {delta:2.2f} ms')
                return result

            return logged

        return logit(cls)
