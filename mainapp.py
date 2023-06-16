from wsgiref.simple_server import make_server
from frame.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

with make_server('', 8080, application) as httpd:
    print('Start server at: 127.0.0.1:8080')
    httpd.serve_forever()
