import math
from triangle import Triangle

class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h_prism):
        super().__init__(a, b, c)
        self.h_prism = h_prism

    def dimension(self): return 3
    def perimetr(self): return None
    def square(self): return None

    def squareBase(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(max(0, s * (s - self.a) * (s - self.b) * (s - self.c)))

    def height(self): return self.h_prism

    def squareSurface(self):
        return 2 * self.squareBase() + (self.a + self.b + self.c) * self.h_prism

    def volume(self):
        return self.squareBase() * self.h_prism
