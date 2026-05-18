from rectangle import Rectangle

class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimension(self): return 3
    def perimetr(self): return None
    def square(self): return None

    def squareBase(self): return self.a * self.b
    def height(self): return self.c
    def squareSurface(self): return 2 * (self.a*self.b + self.b*self.c + self.a*self.c)
    def volume(self): return self.a * self.b * self.c
