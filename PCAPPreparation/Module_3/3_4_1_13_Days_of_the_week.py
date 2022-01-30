class WeekDayError(Exception):
    pass


class Weeker:

    __allowed_values = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    __dict_days = {'Mon': 1, 'Tue': 2, 'Wed': 3, 'Thu': 4, 'Fri': 5, 'Sat': 6, 'Sun': 0}

    def __init__(self, day):
        if not day in Weeker.__allowed_values:
            raise WeekDayError
        self.day = day

    def __str__(self):
        return self.day

    def _get_day_for_value(self, i):
        for key in Weeker.__dict_days.keys():
            if i == Weeker.__dict_days[key]:
                return key

    def add_days(self, n):
        i_day = (Weeker.__dict_days[self.day] + n) % 7
        self.day = self._get_day_for_value(i_day)

    def subtract_days(self, n):
        i_day = (Weeker.__dict_days[self.day] - n) % 7
        if (i_day < 0):
            i_day += 7
        self.day = self._get_day_for_value(i_day)


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
