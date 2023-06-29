from datetime import date
from frame.jinja_plater import render
from patterns.creational import Engine, Logger


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


class Index:
    def __call__(self, request):
        # return '200 OK', 'MAIN PAGE'
        return '200 OK', render('mainpage.html', date=request.get('date', None))


class Info:
    def __call__(self, request):
        # return '200 OK', 'CONTACTS PAGE'
        return '200 OK', render('contacts.html', date=request.get('date', None))


class Guides:
    def __call__(self, request):
        return '200 OK', render('guides.html', date=date.today())



    