from datetime import date


def date_front(request):
    request['date'] = date.today()


def main_front(request):
    request['key'] = 'key'


fronts = [date_front, main_front]

# from views import Index, Info, Guides, GuidesTopics, \
#     CopyGuide, CreateGuide, CreateCategory

# routes = {
#     '/': Index(),
#     '/info/': Info(),
#     '/guides_topics/': GuidesTopics(),
#     '/guides/': Guides(),
#     '/create_guide/': CreateGuide(),
#     '/create_category/': CreateCategory(),
#     '/copy_guide/': CopyGuide(),
# }
