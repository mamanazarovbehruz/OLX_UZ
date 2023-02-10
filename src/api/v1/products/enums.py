from enum import Enum

class Status(Enum):
    n = 'new'
    p = 'in progress'
    r = 'rejected'
    a = 'active'

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]

class ValueType(str ,Enum):
    p = 'price'
    f = 'free'
    e = 'exchange'

    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]