import turtle
import math


class Petal:
    def __init__(self, color="pink", radius=80, angle=60):
        self.color = color
        self.radius = radius
        self.angle = angle

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()

        for _ in range(2):
            t.circle(self.radius, self.angle)
            t.left(180 - self.angle)

        t.end_fill()


class Leaf:
    def __init__(self, color="green", radius=50, angle=70):
        self.color = color
        self.radius = radius
        self.angle = angle

    def draw(self, t):
        t.fillcolor(self.color)
        t.begin_fill()

        for _ in range(2):
            t.circle(self.radius, self.angle)
            t.left(180 - self.angle)

        t.end_fill()


class Stem:
    def __init__(self, color="green", length=200, thickness=6):
        self.color = color
        self.length = length
        self.thickness = thickness

    def draw(self, t):
        t.pensize(self.thickness)
        t.pencolor(self.color)
        t.forward(self.length)


class Flower:
    def __init__(self, petal, leaf, stem, petal_count=6, center_color="yellow"):
        self.petal = petal
        self.leaf = leaf
        self.stem = stem
        self.petal_count = petal_count
        self.center_color = center_color

    def draw_center(self, t, radius=20):
        t.fillcolor(self.center_color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

    def draw_petals(self, t):
        for _ in range(self.petal_count):
            self.petal.draw(t)
            t.left(360 / self.petal_count)

    def draw_leaves(self, t):

        t.penup()
        t.backward(self.stem.length * 0.45)
        t.pendown()

        t.left(25)
        self.leaf.draw(t)


    def draw(self, t, x = 0, y = -250):
        t.penup()
        t.goto(x, y)
        t.setheading(90)
        t.pendown()
        self.stem.draw(t)


        self.draw_leaves(t)

        t.penup()
        t.goto(x, y + self.stem.length)
        t.setheading(0)
        t.pendown()

        self.draw_petals(t)
        t.penup()
        t.goto(x, y + self.stem.length - 20)
        t.setheading(0)
        t.pendown()
        self.draw_center(t)

screen = turtle.Screen()

t = turtle.Turtle()
t.speed(0)

petal = Petal(color="pink", radius=60, angle=90)
leaf = Leaf(color="green", radius=50, angle=80)
stem = Stem(color="green", length=220, thickness=8)

flower = Flower(petal=petal, leaf=leaf, stem=stem, petal_count=6, center_color="yellow")
with open('number of flowers', 'r',) as file:
    number = int(file.read())
    print(number)
    x = 0
    for i in range( number):
        x = x + 100
        flower.draw( t, x, -150)

    screen.exitonclick()
    turtle.done()
