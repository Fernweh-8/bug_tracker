from dataclasses import dataclass, field
from itertools import count
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

    def __repr__(self):
        return (f"Issue(title='{self.title}', user='{self.user}', "
                f"description='{self.description}', status={self.status},"
                f" _id={self._id}, date_created='{self.date_created.strftime('%d/%m/%Y, %H:%M:%S')}',"
                f" flagged={self.flagged})")








