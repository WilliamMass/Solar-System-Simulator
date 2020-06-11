import turtle
from math import *


class Star(turtle.Turtle):
    def __init__(self, size, color):
        super().__init__(shape='circle')
        self.size = size
        self.shapesize(size, size)
        self.c = color
        self.color(self.c)


class Planet(turtle.Turtle):
    def __init__(self, radius, color, size, star, offset=0):
        super().__init__(shape='circle')
        self.radius = radius  # this is really equivalent to the semi-major axis... but everything is a circle anyway
        self.c = color
        self.color(self.c)
        self.size = size
        self.shapesize(size, size)
        self.up()
        self.angle = 0
        self.star = star
        self.offset = offset
        self.draw = 'on'
        self.ellipse = 0.3  # Altering this could draw more accurate orbits; but it's easier to just use n-body calcs?

    '''
    This is the measurement of the angle in radians - whenever this is called, the object's perceived angle on the unit
    circle, as compared to the x and y axes in Python is recalculated.
    '''
    def x_y_motion(self):
        x = self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)

        self.goto(self.star.xcor()+x, self.star.ycor()+y)

    '''
    The addition of an offset on the x value "simulates" a three-dimensional plot in 2 dimensions, by foreshortening the
    orbits.  The offsets are individually defined when the planet is instantiated, with zero representing a circular
    orbit.
    '''
    def x_y_offset_motion(self):
        x = self.offset + self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)*(self.ellipse)

        self.goto(self.star.xcor()+x, self.star.ycor()+y)