'''

'''
from SolarClasses import Planet
from SolarClasses import Star
import turtle
import time

window = turtle.Screen()
window.setup(1280, 900, startx=0, starty=0)
window.bgcolor('black')
window.tracer(0)

sun = Star(5, 5, 'yellow')


earth = Planet(300, 'blue', 1, sun, 100)
mercury = Planet(110, 'burlywood', 0.6, sun, 0)
venus = Planet(180, 'magenta', 0.8, sun, 50)
mars = Planet(550, 'red', 0.9, sun, 100)

moon = Planet(40, 'grey', 0.27, earth, 0)
phobos = Planet(39, 'dim grey', 0.241, mars, 0)
deimos = Planet(33, 'light slate grey', 0.1981, mars, 0)

bodies = [earth, mercury, venus, mars, moon, phobos, deimos]

for body in bodies:
    body.penup()
    body.goto(body.radius, 0)
    if body.star == sun:
        body.pendown()

while True:
    window.update()
    for body in bodies:
        body.x_y_motion()

    moon.angle += 0.08
    phobos.angle += 0.06
    deimos.angle += 0.08

    mercury.angle += 0.05
    venus.angle += 0.03
    earth.angle += 0.01
    mars.angle += 0.007

    time.sleep(0.01)