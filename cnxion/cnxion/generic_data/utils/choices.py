from enum import Enum


class DATA_TYPE_CHOICES(Enum):
    number = ('int', 'Number')
    string = ('str', 'String')

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]
