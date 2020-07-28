class Time:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    @property
    def hour(self):
        return self.h

    def __str__(self):
        return f"{self.h:02}:{self.m:02}:{self.s:02}"

    def __int__(self):
        return self.h * 3600 + self.m * 60 + self.s

    def __eq__(self, other):
        return int(self) == int(other)

    def __gt__(self, other):
        return int(self) > int(other)


t1 = Time(10, 20, 30)
print(t1.hour)

t2 = Time(10, 20, 30)
t3 = Time(1, 2, 3)
print(t1 == t2)
print(t1 == t3)
print(t1 > t3)
print(t1)  # str(t1)   t1.__str__()
