from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional


@dataclass
class DrawDate:
    day_of_the_week: int
    hour: int
    minute: int


class DatesCalc:
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

    OPTIONS = (
        DrawDate(
            day_of_the_week=TUESDAY,
            hour=21,
            minute=30,
        ),
        DrawDate(
            day_of_the_week=SUNDAY,
            hour=21,
            minute=30,
        ),
    )

    @classmethod
    def _apply_dt_replace(cls, dd: DrawDate, dt: datetime):
        """
        :param dd:
        :param dt:
        :return:
        """
        return dt.replace(
            hour=dd.hour,
            minute=dd.minute,
            second=0,
            microsecond=0,
        )

    @classmethod
    def time_to_dow(cls, draw_date: DrawDate, dt: datetime):
        """
        :param draw_date:
        :param dt:
        :return:
        """
        current_dow = dt.weekday()
        days_ahead = draw_date.day_of_the_week - current_dow
        if days_ahead == 0:
            # it's today!
            if dt >= cls._apply_dt_replace(draw_date, dt):
                # if this time for today already passed, checking for the next week
                days_ahead += 7

        elif days_ahead < 0:
            # Desired day already happened this week
            days_ahead += 7

        return cls._apply_dt_replace(draw_date, dt + timedelta(days=days_ahead))

    @classmethod
    def next_draw_day(cls, dt: Optional[datetime] = None):
        """

        >>> monday = datetime(year=2020, month=6, day=1, hour=10)
        >>> closest_draw_date_is_tuesday = datetime(year=2020, month=6, day=2, hour=21, minute=30)
        >>> assert DatesCalc.next_draw_day(monday) == closest_draw_date_is_tuesday

        >>> wednesday = datetime(year=2020, month=6, day=3, hour=10)
        >>> closest_draw_date_is_sunday = datetime(year=2020, month=6, day=7, hour=21, minute=30)
        >>> assert DatesCalc.next_draw_day(wednesday) == closest_draw_date_is_sunday

        >>> sunday_evening = datetime(year=2020, month=6, day=7, hour=22)
        >>> closest_draw_date_is_tuesday_next_week = datetime(year=2020, month=6, day=9, hour=21, minute=30)
        >>> assert DatesCalc.next_draw_day(sunday_evening) == closest_draw_date_is_tuesday_next_week

        :param dt:
        :return:
        """
        if dt is None:
            dt = datetime.now()

        return min(map(lambda dd: cls.time_to_dow(dd, dt), cls.OPTIONS))
