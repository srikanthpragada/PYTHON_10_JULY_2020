class InvalidTimeError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    # Readonly property
    @property
    def totalseconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    # Read-write property
    @property
    def hour(self):
        return self.h

    @hour.setter
    def hour(self, value):
        if value < 0 or value > 23:
            raise InvalidTimeError(f"Invalid Hour : {value}")

        self.h = value


t = Time(10, 20, 30)
try:
    t.hour = 35
except InvalidTimeError as ex:
    print(ex)

print(t.hour)
print(t.totalseconds)
