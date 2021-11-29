from collections import defaultdict
from dataclasses import dataclass, field
from typing import List, Dict, Set, Optional
from itertools import count
from pprint import pprint
from datetime import datetime as dt
from status import Status
from user import User

ID_GENERATOR = count(start=1)


@dataclass()
class Issue:
    title: str
    user: str = field(default=User)
    description: str = field(default='')
    status: Status = field(default=Status.NEW, repr=True)
    _id: int = field(default_factory=lambda: next(ID_GENERATOR))
    date_created: dt = field(default=dt.now(), repr=True)
    flagged: bool = field(default=False)

    # def __repr__(self):
    #     return f'(user: {self.user}, title: {self.title}, description: {self.description})'

    #
    # @property
    # def date_created(self):
    #     return self.date_created.strftime("%m/%d/%Y, %H:%M:%S")








