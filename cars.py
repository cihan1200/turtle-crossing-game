from turtle import Turtle
import random


class Cars(Turtle):
    car_speed = 10

    def __init__(self):
        super().__init__()
        self.random_y = random.randint(-255, 255)
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=320, y=self.random_y)
        self.random_color()

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        color = (r, g, b)
        self.color(color)

    def move(self):
        self.goto(x=self.xcor() - Cars.car_speed, y=self.ycor())
