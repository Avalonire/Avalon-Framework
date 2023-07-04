from wsgiref.simple_server import make_server, WSGIServer, WSGIRequestHandler
from frame.main import Framework, DebugApp
from urls import fronts
from views import routes


app = Framework(routes, fronts)

with make_server('', 8080, app, server_class=WSGIServer) \
        as httpd:
    print('Start server at: 127.0.0.1:8080')
    httpd.serve_forever()

app_debug = DebugApp(routes, fronts)

with make_server('', 8080, app_debug, server_class=WSGIServer) \
        as httpd:
    print('Start DEBUG server at: 127.0.0.1:8080')
    httpd.serve_forever()