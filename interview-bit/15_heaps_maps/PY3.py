def cmp(a, b):
    return (a > b) - (a < b)


# mixin class for Python3 supporting __cmp__
class PY3__cmp__:
    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return self.__cmp__(other) != 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

class Skill(PY3__cmp__):
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description
        print('New Level:', description)
        return
    def __cmp__(self, other):
        return cmp(self.priority, other.priority)