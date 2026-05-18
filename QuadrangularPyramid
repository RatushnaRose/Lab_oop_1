import math
from rectangle import Rectangle

class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h_pyr):
        super().__init__(a, b)
        self.h_pyr = h_pyr

    def dimension(self): return 3
    def perimetr(self): return None
    def square(self): return None

    def squareBase(self): return self.a * self.b
    def height(self): return self.h_pyr

    def squareSurface(self):
        la = math.sqrt(self.h_pyr**2 + (self.b / 2)**2)
        lb = math.sqrt(self.h_pyr**2 + (self.a / 2)**2)
        return self.squareBase() + self.a * la + self.b * lb

    def volume(self):
        return (1/3) * self.squareBase() * self.h_pyr
