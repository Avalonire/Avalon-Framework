from datetime import date


def date_front(request):
    request['date'] = date.today()


def main_front(request):
    request['key'] = 'key'


fronts = [date_front, main_front]
