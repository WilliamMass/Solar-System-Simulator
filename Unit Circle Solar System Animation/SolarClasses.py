import turtle
from math import *


class Star(turtle.Turtle):
    def __init__(self, shapesize_x, shapesize_y, color):
        super().__init__(shape='circle')
        self.shapesize = (shapesize_x, shapesize_y)
        self.c = color
        self.color(self.c)


class Planet(turtle.Turtle):
    def __init__(self, radius, color, size, star, offset=0):
        super().__init__(shape='circle')
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size, size)
        self.up()
        self.angle = 0
        self.star = star
        self.offset = offset
        self.draw = 'on'
        self.ellipse = 0.3

    def x_y_motion(self):
        x = self.radius*cos(self.angle)  # Measurement of angle in radians
        y = self.radius*sin(self.angle)

        self.goto(self.star.xcor()+x, self.star.ycor()+y)

    def x_y_offset_motion(self):
        x = self.offset + self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)*0.3

        self.goto(self.star.xcor()+x, self.star.ycor()+y)