from copy import deepcopy
from quopri import decodestring


# Users architecture
class User:
    pass


class Officer(User):
    pass


class Member(User):
    pass


class Candidate(User):
    pass


class UserFactory:
    types = {
        'Officer': Officer,
        'Member': Member,
        'Candidate': Candidate
    }

    @classmethod
    def create(cls, _type):
        return cls.types[_type]()


# Guides architecture
class GuidePrototype:

    def clone(self):
        return deepcopy(self)


class Guide(GuidePrototype):

    def __int__(self, name, category):
        self.name = name
        self.category = category
        self.category.guides.append(self)


class VideoGuide(Guide):
    pass


class GuideLines(Guide):
    pass


class InteractiveGuide(Guide):
    pass


class GuideFactory:
    types = {
        'Video': VideoGuide,
        'Guidelines': GuideLines,
        'Interactive': InteractiveGuide
    }

    @classmethod
    def create(cls, _type, name, category):
        return cls.types[_type](name, category)


# Category architecture
class Category:
    auto_id = 0

    def __init__(self, name, category):
        self.id = Category.auto_id
        Category.auto_id += 1
        self.name = name
        self.category = category
        self.guides = []

    def guides_count(self):
        result = len(self.guides)
        if self.category:
            result += self.category.guides_count()
        return result


class Engine:
    def __int__(self):
        self.officer = []
        self.member = []
        self.candidate = []
        self.guides = []
        self.categories = []

    @staticmethod
    def create_user(_type):
        return UserFactory.create(_type)

    @staticmethod
    def create_category(name, category=None):
        return Category(name, category)

    def find_category_by_id(self, _id):
        for item in self.categories:
            print('item', item.id)
            if item.id == _id:
                return item
        raise Exception(f'Category with this {_id} not found')

    @staticmethod
    def create_guide(_type, name, category):
        return GuideFactory.create(_type, name, category)

    def get_guide(self, name):
        for item in self.guides:
            if item.name == name:
                return item
        return None

    @staticmethod
    def decode_value(val):
        val_bytes = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        decode_str = decodestring(val_bytes)
        return decode_str


class SingletonByName(type):

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls.__instance = {}

    def __call__(cls, *args, **kwargs):
        if args:
            name = args[0]
        if kwargs:
            name = kwargs['name']

        if name in cls.__instance:
            return cls.__instance[name]
        else:
            cls.__instance[name] = super().__call__(*args, **kwargs)
            return cls.__instance[name]


class Logger(metaclass=SingletonByName):

    def __int__(self, name):
        self.name = name

    @staticmethod
    def log(text):
        print('Logging: ', text)
