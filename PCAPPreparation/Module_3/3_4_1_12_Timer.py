class Timer:
    def __init__(self, hour, min, sec):
        self.__time = sec + (min * 60) + (hour * 3600)
        print("Constructor: ", self.__time)

    def __str__(self):
        hours = self.__time // 3600
        minutes = (self.__time - (hours * 3600)) // 60
        secs = (self.__time - (hours * 3600) - (minutes * 60))
        return f"{hours}:{minutes}:{secs}"

    def next_second(self):
        self.__time += 1
        if self.__time >= 86400:
            self.__time %= 86400

    def prev_second(self):
        self.__time -= 1
        if self.__time < 0:
            self.__time = 86399


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
