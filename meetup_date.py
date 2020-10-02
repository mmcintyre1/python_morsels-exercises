from calendar import monthrange
from datetime import datetime, timedelta
from enum import IntEnum
import operator
from typing import Union


class Weekday(IntEnum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


def meetup_date(
        year: int,
        month: int,
        nth: int = 4,
        weekday: Union[int, Weekday] = Weekday.THURSDAY
) -> datetime.date:

    if nth < 0:
        day = monthrange(year, month)[1]
        op = operator.sub
    else:
        day = 1
        op = operator.add
    day_matches = abs(nth)
    current_date = datetime(year=year, month=month, day=day)
    while day_matches:
        if current_date.weekday() == weekday:
            day_matches -= 1
        if day_matches:
            current_date = op(current_date, timedelta(days=1))

    return current_date.date()


if __name__ == '__main__':
    d = meetup_date(2018, 1, nth=1, weekday=Weekday.MONDAY)
    w = Weekday.MONDAY
    print(w == 0)
