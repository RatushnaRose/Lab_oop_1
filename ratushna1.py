import math

filenames = [
   "input01.txt",
    "input02.txt",
   "input03.txt",
]


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return f"Rectangle(a={self.a}, b={self.b})"


class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        base_diff = abs(self.a - self.b)
        if base_diff == 0:
            return 0
        term1 = (-self.a + self.b + self.c + self.d)
        term2 = (self.a - self.b + self.c + self.d)
        term3 = (self.a - self.b + self.c - self.d)
        term4 = (self.a - self.b - self.c + self.d)
        numerator = term1 * term2 * term3 * term4
        if numerator <= 0:
            return 0
        h = math.sqrt(numerator) / (2 * base_diff)
        return (self.a + self.b) / 2 * h

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def __str__(self):
        return f"Trapeze(a={self.a}, b={self.b}, c={self.c}, d={self.d})"


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r

    def __str__(self):
        return f"Circle(r={self.r})"


class Parallelogram:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return (self.a + self.b) * 2

    def __str__(self):
        return f"Parallelogram(a={self.a}, b={self.b}, h={self.h})"


FIGURE_MAP = {
    "Rectangle":    lambda p: Rectangle(int(p[0]), int(p[1])),
    "Trapeze":      lambda p: Trapeze(int(p[0]), int(p[1]), int(p[2]), int(p[3])),
    "Circle":       lambda p: Circle(int(p[0])),
    "Parallelogram":lambda p: Parallelogram(int(p[0]), int(p[1]), int(p[2])),
}

figures = []
for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if parts and parts[0] in FIGURE_MAP:
                figures.append(FIGURE_MAP[parts[0]](parts[1:]))

if figures:
    max_fig = max(figures, key=lambda f: f.area())
    print(f"Figure with max area: {max_fig}")
    print(f"Area:      {max_fig.area():.4f}")
    print(f"Perimeter: {max_fig.perimeter():.4f}")
