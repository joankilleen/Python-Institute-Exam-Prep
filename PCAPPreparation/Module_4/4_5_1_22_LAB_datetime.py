from datetime import datetime
import time



datet1 = datetime(2020, 11,4, 14, 53)
formats = ['%Y/%m/%d %H:%M:%S','%y/%B/%d %H:%M:%S %p',  '%A, %Y %B %d', 'Weekday: %w', 'Day of the year: %j', 'Week number of the year: %W']

for f in formats:
    print(datet1.strftime(f))

