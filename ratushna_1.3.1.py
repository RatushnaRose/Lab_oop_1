import math
filenames = ["input01.txt", "input02.txt", "input03.txt"]
class Rectangle:
    def __init__(self, a=1, b=1):
        if isinstance(a, Rectangle):
            self.a = a.a
            self.b = a.b
        else:
            self.a = a
            self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def shaw(self):
        print(f"a={self.a},b={self.b}")

print("")
print("Rectangle")
print("")

max_area = 0
max_per = 0
rmax = Rectangle(0, 0)
for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if parts[0] == "Rectangle":

                a, b = map(int, parts[1:])
                r = Rectangle(a, b)
                s = r.area()
                print(f"Area = {s}")
                p = r.perimeter()
                print(f"Perimeter = {p}")
                if s > max_area:
                    max_area = s
                    rmax = r
                if p > max_per:
                    max_per = p
print(f"Max area = {max_area}")
print(f"Max perimeter = {max_per}")
rmax.shaw()




class Trapeze:
    def __init__(self, a, b, c, d):

        if isinstance(a, Trapeze):
            self.a = a.a
            self.b = a.b
            self.c = a.c
            self.d = a.d
        else:
            self.a = a
            self.b = b
            self.c = c
            self.d = d

    def shaw(self):
        print(f"a = {self.a},b = {self.b}, c = {self.c}, d = {self.d} ")

    def height(self):
        base_diff = abs(self.a - self.b)

        term1 = (-self.a + self.b + self.c + self.d)
        term2 = (self.a - self.b + self.c + self.d)
        term3 = (self.a - self.b + self.c - self.d)
        term4 = (self.a - self.b - self.c + self.d)

        numerator = term1 * term2 * term3 * term4
        if numerator <= 0:
            self.shaw()
            print("Trapeze does not exist")
            return 0
        self.shaw()
        return math.sqrt(numerator) / (2 * base_diff)

    def area(self):
        h = self.height()
        if h == 0:
            return 0
        return (self.a + self.b) / 2 * h

    def perimeter(self):
        return (self.a + self.b + self.c + self.d)

print("")
print("Trapeze")
print("")
max_area2 = 0
max_per = 0
rmax2 = Trapeze(0, 0, 0, 0)
for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if parts[0] == "Trapeze":
                a, b, c, d = map(int, parts[1:])
                r2 = Trapeze(a, b, c, d)
                s2 = r2.area()
                if s2 > 0:
                    print(f"Area = {s2}")
                if s2 > max_area2:
                    max_area2 = s2
                    rmax2 = r2
                p = r2. perimeter()
                print(f"Perimeter = {p}")
                if p > max_per:
                    max_per = p
print(f"Max area = {max_area2}")
print(f"Max perimeter = {max_per}")
rmax2.shaw()


class Circle:
    def __init__(self, r):
        if isinstance(r, Circle):
            self.r = r.r
        else:
            self.r = r

    def shaw(self):
        print(f"r = {self.r}")

    def area(self):
        return math.pi * self.r * self.r

    def length_c(self):
        return 2* self.r * math.pi
print("")
print("Circle")
print("")

max_area = 0
max_l = 0
rmax = Circle(0)


for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if parts[0] == "Circle":
                r = int(parts[1])

                if r <= 0:
                    print(f"Circle does not exist")
                    continue

                c = Circle(r)
                s = c.area()
                l = c.length_c()

                print(f"Area = {s}, Length = {l}")

                if s > max_area:
                    max_area = s
                    rmax = c
                if l > max_l:
                    max_l = l

print("-" * 20)
print(f"Max area = {max_area}")
print(f"Max length = {max_l}")
if rmax.r > 0:
    rmax.shaw()


class Parallelogram:
    def __init__(self, a, b , h):
        if isinstance(a, Parallelogram):
            self.a = a.a
            self.b = a.b
            self.h = a.h
        else:
            self.a = a
            self.b = b
            self.h = h

    def area(self):
        return self.a * self.h

    def perimeter(self):
        return (self.a + self.b) * 2

    def shaw(self):
        print(f"a={self.a},b={self.b} ,h={self.h}")

print("")
print("Parallelogram")
print("")

max_area = 0
max_per = 0
rmax = Parallelogram(0, 0, 0)
for filename in filenames:
    with open(filename) as f:
        for line in f:
            parts = line.split()
            if parts[0] == "Parallelogram":

                a, b, h = map(int, parts[1:])
                r = Parallelogram(a, b, h)
                s = r.area()
                if s > 0:
                    print(f"Area = {s}")
                p = r.perimeter()
                print(f"Perimeter = {p}")
                if s > max_area:
                    max_area = s
                    rmax = r
                if p > max_per:
                    max_per = p
print(f"Max area = {max_area}")
print(f"Max perimeter = {max_per}")
rmax.shaw()




