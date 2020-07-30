class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

    def __gt__(self, other):
        if self.x == other.x:
            return self.y > other.y
        else:
            return self.x > other.x


points = [Point(10, 20), Point(1, 2), Point(20, 30)]

for p in sorted(points):
    print(p)
