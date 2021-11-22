from dataclasses import dataclass, field
from itertools import count

ID_GENERATOR = count(start=1)

@dataclass(frozen = True)
class User:
    name: str
    email: str
    password: str
    _id: int = field(default_factory=lambda: next(ID_GENERATOR))