from SolarClasses import Planet, Star
import turtle
import time

window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=0, starty=0)
window.bgcolor('black')
window.tracer(0)

sun = Star(5, 'yellow')

'''
Jupiter has been commented out because this angle does not allow for it to be seen - even on a 4k monitor, the radius
of its orbit is outside of the full size of the Turtle screen.  Uncomment and add it to the bodies list if you would
like, but since these calculations are all independent of one another, all that it will do is eat up processor cycles.
'''
earth = Planet(300, 'blue', 1, sun, 100)
mercury = Planet(117, 'burlywood', 0.6, sun, 0)
venus = Planet(217, 'magenta', 0.7, sun, 50)
mars = Planet(452, 'red', 0.9, sun, 100)
# jupiter = Planet(1509, 'orange', 4, sun, 100)

moon = Planet(40, 'grey', 0.27, earth, 0)
phobos = Planet(39, 'dim grey', 0.11, mars, 0)
deimos = Planet(33, 'light slate grey', 0.0981, mars, 0)

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

    moon.angle += 0.12
    phobos.angle += 0.6
    deimos.angle += 0.4

    mercury.angle += 0.0414
    venus.angle += 0.0162
    earth.angle += 0.01
    mars.angle += 0.005335
    # jupiter.angle += 0.00084315

    time.sleep(0.01)