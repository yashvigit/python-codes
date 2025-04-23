class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.normalize_time()

    def normalize_time(self):
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24

    def add_time(self, other):
        return Time(self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)

    def subtract_time(self, other):
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        total_seconds_diff = (total_seconds_self - total_seconds_other) % (24 * 3600)
        hours = total_seconds_diff // 3600
        minutes = (total_seconds_diff % 3600) // 60
        seconds = total_seconds_diff % 60
        return Time(hours, minutes, seconds)

    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"


if __name__ == "__main__":
    time1 = Time(10, 45, 30)
    time2 = Time(2, 20, 40)

    print("Time 1:", time1)
    print("Time 2:", time2)

    added_time = time1.add_time(time2)
    print("Added Time:", added_time)

    subtracted_time = time1.subtract_time(time2)
    print("Subtracted Time:", subtracted_time)