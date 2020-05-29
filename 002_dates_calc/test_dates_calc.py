from datetime import datetime
import pytest
from dates_calc import DatesCalc


class TestDatesCalc:
    @pytest.mark.parametrize(
        'current_date, closest_draw_date',
        [
            (
                datetime(
                    # this is Monday
                    year=2020,
                    month=6,
                    day=1,
                    hour=10,
                ),
                datetime(
                    # closest is Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    hour=21,
                    minute=30,
                ),
            ),

            (
                datetime(
                    # this is Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    # but in the morning
                    hour=10,
                ),
                datetime(
                    # closest is this Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    # but in the evening
                    hour=21,
                    minute=30,
                ),
            ),
            (
                datetime(
                    # this is Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    hour=21,
                    # one minute before
                    minute=29,
                ),
                datetime(
                    # closest is this Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    # but in the evening
                    hour=21,
                    minute=30,
                ),
            ),
            (
                datetime(
                    # this is Tuesday
                    year=2020,
                    month=6,
                    day=2,
                    hour=21,
                    # and already it's time
                    minute=30,
                ),
                datetime(
                    # so now closest is next Sunday
                    year=2020,
                    month=6,
                    day=7,
                    hour=21,
                    minute=30,
                ),
            ),
            (
                datetime(
                    # this is Wednesday
                    year=2020,
                    month=6,
                    day=3,
                    hour=10,
                ),
                datetime(
                    # so now closest is next Sunday
                    year=2020,
                    month=6,
                    day=7,
                    hour=21,
                    minute=30,
                ),
            ),
            (
                datetime(
                    # this is Sunday
                    year=2020,
                    month=6,
                    day=7,
                    # in the morning
                    hour=10,
                ),
                datetime(
                    # so it's today
                    year=2020,
                    month=6,
                    day=7,
                    hour=21,
                    minute=30,
                ),
            ),
            (
                datetime(
                    # this is Sunday
                    year=2020,
                    month=6,
                    day=7,
                    # already gone
                    hour=22,
                ),
                datetime(
                    # so it's next Tuesday
                    year=2020,
                    month=6,
                    day=9,
                    hour=21,
                    minute=30,
                ),
            ),
        ],
    )
    def test_gets_next_draw_day(self, current_date, closest_draw_date):
        """
        :param current_date:
        :param closest_draw_date:
        :return:
        """
        res = DatesCalc.next_draw_day(current_date)
        assert res == closest_draw_date
