from enum import Enum, auto

class Status(Enum):
    NEW = auto()
    IN_PROGRESS = auto()
    REOPENED = auto()
    ON_HOLD = auto()
    CLOSED = auto()