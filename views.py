from frame.jinja_plater import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html', date=request.get('date', None))


class Info:
    def __call__(self, request):
        return '200 OK', render('contacts.html', date=request.get('date', None))
