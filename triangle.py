import math
from figure import Figure

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimension(self): return 2
    def perimetr(self): return self.a + self.b + self.c

    def square(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(max(0, s * (s - self.a) * (s - self.b) * (s - self.c)))

    def volume(self): return self.square()
