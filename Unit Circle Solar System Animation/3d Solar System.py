from SolarClasses import Planet, Star
import turtle
import time
import numpy as np
import sys

simulation = True

'''
Any system is able to be simulated, but only these sets of values are included which provide a (somewhat) realistic
simulation of actual planetary systems.  Please note that 'Sol' is not actually the name of the Sun, I just enjoy
science-fiction naming conventions.  All these things are initialized below in the if statements.  In order to change
the system being plotted, simply comment/uncomment the appropriate line.
'''
def getsystem():
    system = input("Print: which of the following systems would you like to simulate?\n"
                   "1) Sol\n"
                   "2) Gliese\n\n"
                   "Q) Quit\n\n"
                   "Please enter your choice now: ")
    if system not in ["1", "2", "Q", "Sol", "Gliese", "Quit", "Exit"]:
        print("Sorry, I didn't quite catch that.")
        getsystem()
    else:
        return system

system = getsystem()
normalize_ratios = False
if system == '1':
    system = 'Sol'
elif system == '2':
    system = 'Gliese'
    normalize_ratios = True
elif system == 'Q':
    system = 'Quit'

if system == 'Quit':
    print("Have a stellar day!")
    sys.exit(1)

window = turtle.Screen()
window.setup(width=1.0, height=1.0, startx=0, starty=0)
window.bgcolor('black')
window.tracer(0)

'''
300 pixels is, somewhat arbitrarily, equivalent to 1 AU (96 million miles, the distance from the earth to the sun).
This allows us to develop accurate ratios for the distances of the other planets from the sun.   Because the size of the
window is fixed to be the size of the screen on which the simulation is running, Jupiter may or may not be wholly
visible.  All the planets are drawn to scale as closely as possible.  All stars are NOT drawn to scale.
'''

if system == 'Sol':
    sun = Star(5, 'gold')
    earth = Planet(300, 'mediumblue', 1, sun, 70)
    mercury = Planet(117, 'burlywood', 0.38, sun, 0)
    venus = Planet(217, 'magenta', 0.95, sun, 50)
    mars = Planet(452, 'firebrick', .53, sun, 100)
    jupiter = Planet(1509, 'orange', 11.2, sun, 100)

    '''
    These lunar distances are quite inaccurate - in reality, the moon would have a distance of about .9, and each of
    the moons of mars would be somewhere around .011 and .039 respectively.  But that makes the plotting not look
    particularly good, so the 'Rule of Cool' was followed.
    '''
    moon = Planet(20, 'grey', 0.27, earth, 0)
    phobos = Planet(19, 'gainsboro', 0.11, mars, 3)
    deimos = Planet(19, 'light slate grey', 0.0981, mars, 0)

    '''
    Asteroids can be manually toggled off to avoid framerate issues.
    '''
    asteroids = True

    bodies = [earth, mercury, venus, mars, jupiter, moon, phobos, deimos]
    for body in bodies:
        body.penup()
        body.goto(body.radius + body.offset, 0)
        if body.star == sun:
            body.pendown()

elif system == 'Gliese':
    '''
    The planets in Gliese are in proximal order to Gliese 581, so closest to furthest.  Their names are alphabetical in
    order of their discovery. - The distances here (the radius/semimajor axis value defined when each Planet object is
    created) are 20% of what they are in our solar system.  For instance, Gliese 581e (defined ge, below) is .02815 of
    an astronomical unit from its star; plotting that in Turtle would make it draw its orbit essentially completely
    within its star, so the values have been scaled instead.  Once again, all Planets are scaled correctly, proportional
    to the size of Earth, and the star is _not_ drawn to realistic scale. These bodies are initialized in order of
    proximity to their star.
    '''
    g581 = Star(3, 'orangered')
    ge = Planet(168, 'tomato', 1.2, g581, 1)
    gb = Planet(242, 'chocolate', 3.8, g581, 1)
    gc = Planet(432, 'thistle', 1.4, g581, 10)
    gd = Planet(1260, 'deepskyblue', 2.2, g581, -180)

    '''
     The system is known to have a massive system of icy planetoids at its edge, similar but denser than the Kuiper Belt
     at the edge of our Solar System - but it is far beyond the distance able to be rendered by Turtle's ability to draw
     things around a fixed point on the screen!  So, to save processor cycles, we'll just turn asteroids off.
    '''
    asteroids = False

    bodies = [ge, gb, gc, gd]
    for body in bodies:
        body.penup()
        body.goto(body.radius + body.offset, 0)
        if body.star == g581:
            body.pendown()

asteroid_belt = []
angle = 0.001

if asteroids:
    for i in range(525):
        asteroid = Planet(np.random.randint(555, 900), 'peru', 0.1, sun, 100)
        asteroid.penup()
        asteroid_belt.append(asteroid)
        asteroid.angle += angle
        angle += 0.0214121

while simulation:
    window.update()
    for body in bodies:
        body.x_y_offset_motion()

    '''
    For each time slice, the position is increased by 0.0x radians, as based on the ratio of the planets orbital period
    to that of the Earth. In other words, over the time steps it takes for earth to complete an orbit in Turtle the
    angle is increased by .01.  In that same period of time, the angle for mercury is increased by 0.0414, since Mercury
    takes 88 days to complete one orbit of the sun.
    '''
    if system == 'Sol':
        moon.angle += 0.12
        phobos.angle += 0.6
        deimos.angle += 0.4

        mercury.angle += 0.0414
        venus.angle += 0.0162
        earth.angle += 0.01
        mars.angle += 0.005335
        jupiter.angle += 0.00084315

    '''
    For each time slice, the position is increased by 0.0x radians, as based on the ratio of the planets orbital period
    to that of the Gliese 581d.  This is the "outermost" planet in this system, which is right at the edge of the star's
    "Goldilocks Zone" and could potentially support life.  All of these planets have _much_ faster orbits than any of
    the planets in our Solar System - Gliese 581e completes one orbit in 3.149 Earth days!  The comments contain values
    with the ratios expressed as ratios of Earth's orbital period as well, so that the speed difference can be compared to that of our solar
    system.
    '''
    if system == 'Gliese':
        if normalize_ratios:
            ge.angle += 1.159  # (Ratio to Gliese 581d: 0.46956 - Ratio to Earth: 1.159)
            gb.angle += 0.6798  # (Ratio to Gliese 581d: 0.12455 - Ratio to Earth: 0.6798)
            gc.angle += 0.2993  # (Ratio to Gliese 581d: 0.05178 - Ratio to Earth: 0.2993)
            gd.angle += 0.055  # (If using Ratio to self for other calculations: 0.01 - Ratio to Earth: 0.055)

        else:
            ge.angle += 0.46956
            gb.angle += 0.12455
            gc.angle += 0.05178
            gd.angle += 0.01

    for i in asteroid_belt:
        i.x_y_offset_motion()
        i.angle += 0.002

    time.sleep(0.01)