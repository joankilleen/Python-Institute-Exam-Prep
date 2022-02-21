from calendar import Calendar


class MyCalendar(Calendar):
    """extension of Calendar"""
    def count_weekday_in_year(self, year, weekday):
        """Counting"""
        count = 0
        for month in range(1,13):
            for week in self.monthdays2calendar(year, month):
                for day_number, weekday_number in week:
                    if day_number == 0:
                        """Not in month"""
                        continue
                    if weekday_number == weekday:
                        count += 1
        return count


c = MyCalendar()
my_count = c.count_weekday_in_year(2000, 6)
print(my_count)