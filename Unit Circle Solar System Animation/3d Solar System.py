from SolarClasses import Planet, Star
import turtle
import time
import numpy as np

simulation, asteroids = True, True

window = turtle.Screen()
window.setup(1400, 768, startx=0, starty=0)
window.bgcolor('black')
window.tracer(0)

sun = Star(10, 5, 'yellow')

'''
300 pixels is, somewhat arbitrarily, equivalent to 1 AU (96 million miles, the distance from the earth to the sun).
This allows us to develop accurate ratios for the distances of the other planets from the sun.  This measurement does
not allow us to animate Jupiter particularly well (although it is there - if you watch you can see it in the upper right
hand corner, somewhere during Earth's 4th rotation.  Because the size of the window is fixed, it is possible that if you
have a very high resolution monitor and maximize the Turtle window after running the simulation, you can see more of
Jupiter's orbit.
'''

earth = Planet(300, 'blue', 1, sun, 100)
mercury = Planet(117, 'burlywood', 0.6, sun, 0)
venus = Planet(217, 'magenta', 0.7, sun, 50)
mars = Planet(452, 'red', 0.9, sun, 100)
jupiter = Planet(1509, 'orange', 4, sun, 100)

moon = Planet(40, 'grey', 0.27, earth, 0)
phobos = Planet(39, 'dim grey', 0.11, mars, 0)
deimos = Planet(33, 'light slate grey', 0.0981, mars, 0)

bodies = [earth, mercury, venus, mars, jupiter, moon, phobos, deimos]

for body in bodies:
    body.penup()
    body.goto(body.radius + body.offset, 0)
    if body.star == sun:
        body.pendown()

asteroid_list = []
angle = 0.001

if asteroids:
    for i in range(525):
        asteroid = Planet(np.random.randint(555, 700), 'peru', 0.1, sun, 100)
        asteroid.penup()
        asteroid_list.append(asteroid)
        asteroid.angle += angle
        angle += 0.0214121

while simulation:
    window.update()
    for body in bodies:
        body.x_y_offset_motion()

    moon.angle += 0.12
    phobos.angle += 0.6
    deimos.angle += 0.4

    mercury.angle += 0.0414
    venus.angle += 0.0162
    earth.angle += 0.01
    mars.angle += 0.005335
    jupiter.angle += 0.00084315

    for i in asteroid_list:
        i.x_y_offset_motion()
        i.angle += 0.002

    time.sleep(0.01)