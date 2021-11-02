from enum import Enum, auto

class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    REOPENED = auto()
    ON_HOLD = auto()
    CLOSED = auto()

    def parse_status(self, string):
        statuses = [(s.value, s.name.lower(), s) for s in list(Status)]
        string = string.string().lower()
        for v, n, s in statuses:
            if string == v or string == n:
                return s
            if n.startswith(string) or string.endswith(n):
                return s
        raise ValueError('Wrong status')