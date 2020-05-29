### 002

Python - The Canadian National Lottery draw takes place twice per week, on Tuesday and Sunday at 9.30 pm.
Write a class in Python that returns the next valid draw date based on the current date.
Make your code able to calculate the next draw based on an optionally supplied date and time.


#### Example

```python
from datetime import datetime
from dates_calc import DatesCalc

monday = datetime(year=2020, month=6, day=1, hour=10)
closest_draw_date_is_tuesday = datetime(year=2020, month=6, day=2, hour=21, minute=30)
assert DatesCalc.next_draw_day(monday) == closest_draw_date_is_tuesday

wednesday = datetime(year=2020, month=6, day=3, hour=10)
closest_draw_date_is_sunday = datetime(year=2020, month=6, day=7, hour=21, minute=30)
assert DatesCalc.next_draw_day(wednesday) == closest_draw_date_is_sunday

sunday_evening = datetime(year=2020, month=6, day=7, hour=22)
closest_draw_date_is_tuesday_next_week = datetime(year=2020, month=6, day=9, hour=21, minute=30)
assert DatesCalc.next_draw_day(sunday_evening) == closest_draw_date_is_tuesday_next_week
```
