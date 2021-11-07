from enum import Enum, auto



class Status(Enum):

    @classmethod
    def parse_status(cls, string):
        statuses = [(status.value, status.name.lower(), status) for status in list(cls)]
        string = str(string).lower()
        for value, name, status in statuses:
            if string == value or string == name:
                return status
            if name.startswith(string) or string.endswith(name):
                return status
        raise ValueError('Wrong status')

    NEW = auto()
    IN_PROGRESS = auto()
    REOPENED = auto()
    ON_HOLD = auto()
    CLOSED = auto()
