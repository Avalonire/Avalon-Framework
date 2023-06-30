from datetime import date
from views import Index, Info, Guides, GuidesTopics, \
    CopyGuide, CreateGuide, CreateCategory, CategoryList


def date_front(request):
    request['date'] = date.today()


def main_front(request):
    request['key'] = 'key'


fronts = [date_front, main_front]

routes = {
    '/': Index(),
    '/info/': Info(),
    '/guides_topics/': GuidesTopics(),
    '/guides/': Guides(),
    '/create_guide/': CreateGuide(),
    '/create_category/': CreateCategory(),
    '/copy_guide/': CopyGuide(),
    # '/categories/': CategoryList(),
}
