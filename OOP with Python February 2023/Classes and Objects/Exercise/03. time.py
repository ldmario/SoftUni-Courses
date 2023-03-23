class Time:
    max_hours, max_minutes, max_seconds = 23, 59, 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hour, minute, second):
        self.hours = hour
        self.minutes = minute
        self.seconds = second

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        if self.seconds == Time.max_seconds:
            self.set_time(self.hours, self.minutes, 0)
            if self.minutes == Time.max_minutes:
                self.set_time(self.hours, 0, self.seconds)
                if self.hours == Time.max_hours:
                    self.set_time(0, self.minutes, self.seconds)
                else:
                    self.hours += 1
            else:
                self.minutes += 1
        else:
            self.seconds += 1

        return self.get_time()


