
#filenames = ["input01.txt", "input02.txt", "input03.txt"]
#with open(filenames) as f:
   # for line in f:
        #parts = line.split()
import math
class Figure:
    def __init__(self, is_three_dimensional = False):
        self.is_three_dimensional = is_three_dimensional
    def dimention(self):
       return self.is_three_dimensional
    def perimeter(self, parts):
        self.parts = parts
        perim = 0
        if not self.is_three_dimensional:
            for i in range(1, len(self.parts)):
                perim = perim + parts[i]
            return perim
        return None
    def square(self, parts):
        return None
    def squareSurface(self):
       return None
    def squareBase(self):
       return None
    def height(self):
        return None
    def volume(self):
        return None


class Triangle(Figure):
    def __init__(self, parts,  is_three_dimensional = False):
        self.parts = parts
        super().__init__(is_three_dimensional)
    def perimeter(self, parts):
       return super().perimeter(parts)
    def square(self, parts):
        self.parts = parts
        perim = self.perimeter(parts)
        p = perim /2
        sq = abs(p * (p-parts[0])* (p-parts[1]) * (p-parts[2])** 0.5)
        if sq > 0:
            return sq
        return "Такої площі не існує"

    def squareSurface(self):
        return super().squareSurface()
    def height(self, parts):
        return super().height()
    def volume(self):
        return self.square(self.parts)

class Rectangle(Figure):
    def __init__(self, parts, is_three_dimensional = False):
        self.parts = parts
        super().__init__(is_three_dimensional)

    def perimeter(self, parts):
        return super().perimeter(parts)

    def square(self, parts):
        self.parts = parts
        sq = parts[0]* parts[1]
        if sq > 0:
            return sq
        return "Такої площі не існує"

    def squareBase(self):
        return super().squareBase()
    def squareSurface(self):
        return super().squareSurface()

    def height(self, parts):
        return super().height()

    def volume(self):
        return self.square(self.parts)


class Trapeze(Figure):
    def __init__(self, parts, is_three_dimensional=False):
        self.parts = parts
        super().__init__(is_three_dimensional)

    def perimeter(self, parts):
        return super().perimeter(parts)

    def height_2D(self, parts):
        self.parts = parts
        base_diff = abs(parts[0]- parts[1])

        term1 = (-parts[0] + parts[1] + parts[2] + parts[3])
        term2 = (parts[0] - parts[1] + parts[2] + parts[3])
        term3 = (parts[0] - parts[1] + parts[2] - parts[3])
        term4 = (parts[0] - parts[1] - parts[2] + parts[3])

        numerator = abs(term1 * term2 * term3 * term4)
        if numerator <= 0 or base_diff == 0:
            print("Trapeze does not exist")
            return 0
        return math.sqrt(numerator) / (2 * base_diff)
    def square(self, parts):
        self.parts = parts
        h = self.height_2D(parts)
        sq =  abs((parts[0] + parts[1]) / 2 * h)
        if h == 0 or sq <= 0:
            return 0
        return sq
    def squareSurface(self):
        return super().squareSurface()
    def squareBase(self):
        return super().squareBase()

    def height(self, parts):
        return super().height()

    def volume(self):
        return self.square(self.parts)

class Circle(Figure):
    def __init__(self, parts, is_three_dimensional=False):
        self.parts = parts
        super().__init__(is_three_dimensional)

    def perimeter(self, parts):
        return 2* math.pi * parts[0]

    def square(self, parts):
        self.parts = parts
        sq =  abs(math.pi * parts[0] * parts[0])
        if sq > 0:
            return sq
        return "Такої площі не існує"
    def squareBase(self):
        return super().squareBase()

    def squareSurface(self):
        return super().squareSurface()

    def height(self, parts):
        return super().height()

    def volume(self):
        return self.square(self.parts)


class Parallelogram(Figure):
    def __init__(self, parts, is_three_dimensional=False):
        self.parts = parts
        super().__init__(is_three_dimensional)

    def perimeter(self, parts):
        return super().perimeter(parts)

    def square(self, parts):
        self.parts = parts
        sq = abs(parts[0] * parts[2])
        if sq > 0:
            return sq
        return "Такої площі не існує"

    def squareSurface(self):
        return super().squareSurface()

    def squareBase(self):
        return super().squareBase()

    def height(self, parts):
        return super().height()

    def volume(self):
        return self.square(self.parts)


class Ball(Figure):
    def __init__(self, parts, is_three_dimensional=True):
        self.parts = parts
        self.is_three_dimensional = is_three_dimensional
    def perimeter(self, parts):
        return 2* math.pi * parts[0]

    def square(self, parts):
        return super().square()

    def squareBase(self):
        return super().squareBase()

    def squareSurface(self, parts):
        self.parts = parts
        sq = abs(4 * math.pi * parts[0] ** 2)
        if sq > 0:
            return sq
        return None

    def height(self, parts):
        return super().height()

    def volume(self, parts):
        self.parts = parts
        return 4/3 * math.pi * parts[0] ** 3

class TriangularPyramid(Triangle):
    def __init__(self, parts, is_three_dimensional=True):
        self.parts = parts
        self.is_three_dimensional = is_three_dimensional

    def perimeter(self, parts):
        return super().perimeter(parts)

    def square(self, parts):
        self.parts = parts
        sq1 = parts[0] **2 * math.sqrt(3) / 4
        sq2 = abs(3* parts[0]/ 2 * math.sqrt(parts[1]**2 + parts[0]**2/12))
        if sq1 > 0 and sq2 > 0:
            return sq1 + sq2
        return None

    def squareBase(self):
        sq1 = parts[0] ** 2 * math.sqrt(3) / 4
        if sq1 > 0:
            return sq1
        return None


    def squareSurface(self, parts):
        self.parts = parts
        sq2 = abs(3* parts[0]/ 2 * math.sqrt(parts[1]**2 + parts[0]**2/12))
        if sq2 > 0:
            return sq2
        return None

    def height(self, parts):
        return parts[1]

    def volume(self, parts):
        self.parts = parts
        v = abs(parts[0]**2 * parts[1] * math.sqrt(3)/12)
        if v > 0:
            return v
        return None




filenames = ["input01.txt", "input02 (1).txt", "input03 (1).txt"]
for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = list(line.split())
            transformed_parts = [int(x) for x in parts[1:]]
            if parts[0] == "Triangle":
                triangle = Triangle(transformed_parts , False)
                print(triangle.perimeter(transformed_parts ))
                print(triangle.square(transformed_parts ))
                print(triangle.squareSurface())
                print(triangle.height(transformed_parts ))
            elif parts[0] == "Rectangle":
                rectangle = Rectangle(transformed_parts, False)
                print(rectangle.perimeter(transformed_parts))
                print(rectangle.square(transformed_parts))
            elif parts[0] == "Parallelogram":
                parallelogram = Parallelogram(transformed_parts, False)
                print(parallelogram.perimeter(transformed_parts))
                print(parallelogram.square(transformed_parts))
            elif parts[0] == "Circle":
                circle = Circle(transformed_parts, False)
                print(circle.perimeter(transformed_parts))
                print(circle.square(transformed_parts))
            elif parts[0] == "Ball":
                ball = Ball(transformed_parts, True)
                print(ball.perimeter(transformed_parts))
                print(ball.squareSurface(transformed_parts))
                print(ball.volume(transformed_parts))
            elif parts[0] == "TriangularPyramid":
                triangularPyramid = TriangularPyramid(transformed_parts, True)
                print(triangularPyramid.perimeter(transformed_parts))
                print(triangularPyramid.squareSurface(transformed_parts))
                print(triangularPyramid.volume(transformed_parts))
            elif parts[0] == "Trapeze":
                trapeze = Trapeze(transformed_parts, False)
                print(trapeze.perimeter(transformed_parts))
                print(trapeze.square(transformed_parts))

