from copy import deepcopy
from quopri import decodestring
from patterns.behavioral import FileWriter, Subject


# Users architecture
class User:
    def __init__(self, name):
        self.name = name


class Officer(User):
    pass


class Member(User):
    pass


class Candidate(User):

    def __init__(self, name):
        self.guides = []
        super().__init__(name)


class UserFactory:
    types = {
        'officer': Officer,
        'member': Member,
        'candidate': Candidate
    }

    @classmethod
    def create(cls, _type, name):
        return cls.types[_type](name)


# Guides architecture
class GuidePrototype:

    def clone(self):
        return deepcopy(self)


class Guide(GuidePrototype, Subject):

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.category.guides.append(self)
        self.candidates = []
        super().__init__()

    def __getitem__(self, item):
        return self.candidates[item]

    def add_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)
        candidate.guides.append(self)
        self.notify()


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

    def guide_count(self):
        result = len(self.guides)
        if self.category:
            result += self.category.guide_count()
        return result


class Engine:
    def __init__(self):
        self.officer = []
        self.member = []
        self.candidate = []
        self.guides = []
        self.categories = []

    @staticmethod
    def create_user(_type, name):
        return UserFactory.create(_type, name)

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

    def get_candidate(self, name):
        for item in self.candidate:
            if item.name == name:
                return item

    @staticmethod
    def decode_value(val):
        val_b = bytes(val.replace('%', '=').replace("+", " "), 'UTF-8')
        decode_str = decodestring(val_b)
        return decode_str.decode('UTF-8')


class Logger:

    def __init__(self, name, writer=FileWriter()):
        self.name = name
        self.writer = writer

    def log(self, text):
        text = f'(!) Loging ---> {text}'
        self.writer.write(text)
