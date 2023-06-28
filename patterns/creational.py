from copy import deepcopy


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


class CourseFactory:
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

    def create_user(_type):
        return UserFactory.create(_type)

    def 
