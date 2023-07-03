from frame.jinja_plater import render
from patterns.creational import Engine, Logger
from patterns.structures import AppRoute

site = Engine()
logger = Logger('main')
routes = {}


class NotFound404:
    def __call__(self, request):
        return '404 WHAT', '404 PAGE Not Found'


@AppRoute(routes=routes, url='/')
class Index:
    def __call__(self, request):
        # return '200 OK', 'MAIN PAGE'
        return '200 OK', render('mainpage.html', date=request.get('date', None))


@AppRoute(routes=routes, url='/info/')
class Info:
    def __call__(self, request):
        # return '200 OK', 'CONTACTS PAGE'
        return '200 OK', render('contacts.html', date=request.get('date', None))


@AppRoute(routes=routes, url='/topics/')
class GuidesTopics:
    def __call__(self, request):
        return '200 OK', render('guides_topics.html', objects_list=site.categories)


@AppRoute(routes=routes, url='/guides/')
class Guides:
    def __call__(self, request):
        logger.log('guides list')
        try:
            category = site.find_category_by_id(
                int(request['request_params']['id']))
            return '200 OK', render('guides.html',
                                    objects_list=category.guides,
                                    name=category.name, id=category.id)
        except KeyError:
            return '200 OK', 'No guides have been added yet'


@AppRoute(routes=routes, url='/create_guide/')
class CreateGuide:
    category_id = -1

    def __call__(self, request):
        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category = None
            if self.category_id != -1:
                category = site.find_category_by_id(int(self.category_id))

                guide = site.create_guide('Video', name, category)
                site.guides.append(guide)

            return '200 OK', render('guides.html',
                                    objects_list=category.guides,
                                    name=category.name, id=category.id)
        else:
            try:
                self.category_id = int(request['request_params']['id'])
                category = site.find_category_by_id(int(self.category_id))

                return '200 OK', render('create_guide.html',
                                        name=category.name,
                                        id=category.id)
            except KeyError:
                return '200 OK', 'No guides have been added yet'


@AppRoute(routes=routes, url='/create_category/')
class CreateCategory:
    def __call__(self, request):

        if request['method'] == 'POST':
            data = request['data']
            name = data['name']
            name = site.decode_value(name)
            category_id = data.get('category_id')
            category = None
            if category_id:
                category = site.find_category_by_id(int(category_id))

            new_category = site.create_category(name, category)
            site.categories.append(new_category)

            return '200 OK', render('guides_topics.html',
                                    objects_list=site.categories)
        else:
            categories = site.categories
            return '200 OK', render('create_category.html',
                                    categories=categories)


@AppRoute(routes=routes, url='/copy_guide/')
class CopyGuide:
    def __call__(self, request):
        request_params = request['request_params']

        try:
            name = request_params['name']
            old_guide = site.get_guide(name)
            if old_guide:
                new_name = f'Copied guide - {name}'
                new_guide = old_guide.clone()
                new_guide.name = new_name
                site.guides.append(new_guide)

                return '200 OK', render('guides.html',
                                        objects_list=site.guides,
                                        name=new_guide.category.name)
        except KeyError:
            return '200 OK', 'No guides have been added yet'

# class CategoryList:
#     def __call__(self, request):
#         logger.log('Category list')
#         return '200 OK', render('category_list.html',
#                                 objects_list=site.categories)
