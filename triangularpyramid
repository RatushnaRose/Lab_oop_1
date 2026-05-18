import math
from triangle import Triangle

class TriangularPyramid(Triangle):
    def __init__(self, a, h_pyr):
        super().__init__(a, a, a)
        self.h_pyr = h_pyr

    def dimension(self): return 3
    def perimetr(self): return None
    def square(self): return None

    def squareBase(self):
        return math.sqrt(3) / 4 * self.a**2

    def height(self): return self.h_pyr

    def squareSurface(self):
        l = math.sqrt(self.h_pyr**2 + self.a**2 / 12)
        return self.squareBase() + 3 * 0.5 * self.a * l

    def volume(self):
        return (1/3) * self.squareBase() * self.h_pyr
