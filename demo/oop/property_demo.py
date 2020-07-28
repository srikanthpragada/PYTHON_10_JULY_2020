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
            raise ValueError("Invalid Hour")

        self.h = value


t = Time(10, 20, 30)
t.hour = 15
print(t.hour)
print(t.totalseconds)
