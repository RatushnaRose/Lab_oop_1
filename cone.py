import math
from circle import Circle

class Cone(Circle):
    def __init__(self, r, h_cone):
        super().__init__(r)
        self.h_cone = h_cone

    def dimension(self): return 3
    def perimetr(self): return None
    def square(self): return None

    def squareBase(self): return math.pi * self.r**2
    def height(self): return self.h_cone

    def squareSurface(self):
        l = math.sqrt(self.r**2 + self.h_cone**2)
        return math.pi * self.r * (self.r + l)

    def volume(self):
        return (1/3) * math.pi * self.r**2 * self.h_cone
