import math
from figure import Figure

class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimension(self): return 2
    def perimetr(self): return self.a + self.b + self.c + self.d

    def square(self):
        a, b, c, d = self.a, self.b, self.c, self.d
        p = a - b
        if p == 0:
            return 0
        x = (p**2 + c**2 - d**2) / (2 * p)
        h2 = c**2 - x**2
        if h2 <= 0:
            return 0
        return (a + b) / 2 * math.sqrt(h2)

    def volume(self): return self.square()
