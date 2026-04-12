"""
Керування:
- Kлавіша '1' перемикає цифровий формат на 12-годинний.
- Kлавіша '2' перемикає цифровий формат на 24-годинний.
- Kлавіша 'q' закриває вікно.
"""

from __future__ import annotations

import math
import time
import turtle
from datetime import datetime


class Digit:

    def __init__(self, value: int, radius: int, color: str = "black") -> None:
        self.value = value
        self.radius = radius
        self.color = color

    def draw(self, pen: turtle.Turtle) -> None:
        angle_deg = 90 - self.value * 30
        angle_rad = math.radians(angle_deg)

        x = (self.radius - 25) * math.cos(angle_rad)
        y = (self.radius - 25) * math.sin(angle_rad)

        pen.penup()
        pen.goto(x, y - 10)
        pen.color(self.color)
        pen.write(
            str(self.value),
            align="center",
            font=("Arial", 16, "bold"),
        )


class ClockFace:

    def __init__(self, radius: int = 200) -> None:
        self.radius = radius
        self.digits = [Digit(i, radius) for i in range(1, 13)]

    def draw(self, pen: turtle.Turtle) -> None:
        pen.penup()
        pen.goto(0, -self.radius)
        pen.setheading(0)
        pen.pendown()
        pen.pensize(3)
        pen.color("black")
        pen.circle(self.radius)

        for step in range(60):
            angle = 90 - step * 6
            rad = math.radians(angle)

            if step % 5 == 0:
                inner = self.radius - 18
                width = 3
            else:
                inner = self.radius - 10
                width = 1

            outer = self.radius

            x1 = inner * math.cos(rad)
            y1 = inner * math.sin(rad)
            x2 = outer * math.cos(rad)
            y2 = outer * math.sin(rad)

            pen.penup()
            pen.goto(x1, y1)
            pen.pensize(width)
            pen.pendown()
            pen.goto(x2, y2)

        for digit in self.digits:
            digit.draw(pen)


class Hand:

    def __init__(self, length: int, width: int, color: str) -> None:
        self.length = length
        self.width = width
        self.color = color

    def draw(self, pen: turtle.Turtle, angle_deg: float) -> None:
        rad = math.radians(angle_deg)
        x = self.length * math.cos(rad)
        y = self.length * math.sin(rad)

        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.pensize(self.width)
        pen.color(self.color)
        pen.goto(x, y)


class Watch:

    def update(self) -> None:
        raise NotImplementedError("Метод update має бути перевизначений у нащадку.")


class AnalogWatch(Watch):

    def __init__(self) -> None:
        self.face_pen = turtle.Turtle(visible=False)
        self.face_pen.speed(0)
        self.face_pen.hideturtle()

        self.hand_pen = turtle.Turtle(visible=False)
        self.hand_pen.speed(0)
        self.hand_pen.hideturtle()

        self.center_pen = turtle.Turtle(visible=False)
        self.center_pen.speed(0)
        self.center_pen.hideturtle()

        self.face = ClockFace(radius=200)
        self.hour_hand = Hand(length=100, width=6, color="black")
        self.minute_hand = Hand(length=145, width=4, color="blue")
        self.second_hand = Hand(length=170, width=2, color="red")
        self.face.draw(self.face_pen)

    def update(self) -> None:

        self.hand_pen.clear()
        self.center_pen.clear()

        now = datetime.now()

        second_angle = 90 - now.second * 6

        minute_angle = 90 - (now.minute + now.second / 60) * 6

        hour_in_12 = now.hour % 12
        hour_angle = 90 - (hour_in_12 + now.minute / 60) * 30

        self.hour_hand.draw(self.hand_pen, hour_angle)
        self.minute_hand.draw(self.hand_pen, minute_angle)
        self.second_hand.draw(self.hand_pen, second_angle)

        self.center_pen.penup()
        self.center_pen.goto(0, 0)
        self.center_pen.dot(12, "black")


class DigitalWatch(Watch):

    def __init__(self, is_24h: bool = True) -> None:
        self.is_24h = is_24h

        self.text_pen = turtle.Turtle(visible=False)
        self.text_pen.speed(0)
        self.text_pen.hideturtle()

    def set_12h(self) -> None:
        self.is_24h = False

    def set_24h(self) -> None:
        self.is_24h = True

    def update(self) -> None:
        self.text_pen.clear()
        now = datetime.now()

        if self.is_24h:
            text = now.strftime("%H:%M:%S") + " (24h)"
        else:
            text = now.strftime("%I:%M:%S %p") + " (12h)"

        self.text_pen.penup()
        self.text_pen.goto(0, -255)
        self.text_pen.color("darkgreen")
        self.text_pen.write(
            text,
            align="center",
            font=("Courier New", 20, "bold"),
        )


class ClockApp:

    def __init__(self, update_seconds: int = 1) -> None:
        self.update_seconds = update_seconds

        self.screen = turtle.Screen()
        self.screen.setup(width=700, height=700)
        self.screen.title("Лабораторна 2.4.1: Аналоговий + Цифровий годинник")
        self.screen.bgcolor("white")

        self.screen.tracer(0)

        self.analog_watch = AnalogWatch()
        self.digital_watch = DigitalWatch(is_24h=True)

        self.screen.listen()
        self.screen.onkey(self.switch_to_12h, "1")
        self.screen.onkey(self.switch_to_24h, "2")
        self.screen.onkey(self.close, "q")

        self.is_running = True

    def switch_to_12h(self) -> None:
        self.digital_watch.set_12h()

    def switch_to_24h(self) -> None:
        self.digital_watch.set_24h()

    def close(self) -> None:
        self.is_running = False
        turtle.bye()

    def run(self) -> None:
        while self.is_running:
            self.analog_watch.update()
            self.digital_watch.update()
            self.screen.update()
            time.sleep(self.update_seconds)


if __name__ == "__main__":
    app = ClockApp(update_seconds=1)
    app.run()
