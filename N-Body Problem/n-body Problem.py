import math

import random
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Body:
    def __init__(self, location, mass, velocity, name=""):
        self.location = location
        self.mass = mass
        self.velocity = velocity
        self.name = name


def compute_sba(bodies, bi):
    '''
    Computes the acceleration of a single body, based on the gravitational constant and the influence of other bodies
    in the bodies table. Grav * mass / r ** 3 is the calculation, with grav being the gravitational constant, and mass
    being the mass of the other body.
    :param bodies: List type-item of defined bodies
    :param bi: index of current body being calculated in that bodies list
    :return:
    '''
    grav = 6.67408e-11  # m3 kg-1 s-2
    acc = Point(0, 0, 0)
    current_body = bodies[bi]
    for index, other in enumerate(bodies):
        if index != bi:
            r = (current_body.location.x - other.location.x) ** 2 + (
                        current_body.location.y - other.location.y) ** 2 + (
                            current_body.location.z - other.location.z) ** 2
            r = math.sqrt(r)
            tmp = grav * other.mass / r ** 3
            acc.x += tmp * (other.location.x - current_body.location.x)
            acc.y += tmp * (other.location.y - current_body.location.y)
            acc.z += tmp * (other.location.z - current_body.location.z)

    return acc


def update_velocity(bodies, time_step=1):
    for bi, current_body in enumerate(bodies):
        acceleration = compute_sba(bodies, bi)

        current_body.velocity.x += acceleration.x * time_step
        current_body.velocity.y += acceleration.y * time_step
        current_body.velocity.z += acceleration.z * time_step


def update_location(bodies, time_step=1):
    for body in bodies:
        body.location.x += body.velocity.x * time_step
        body.location.y += body.velocity.y * time_step
        body.location.z += body.velocity.z * time_step


def grav_step(bodies, time_step=1):
    update_velocity(bodies, time_step=time_step)
    update_location(bodies, time_step=time_step)


def plot_output(bodies):
    fig = plt.figure()
    palette = ['red', 'blue', 'green', 'yellow', 'magenta', 'cyan']
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0
    for current_body in bodies:
        max_dim = max(max(current_body["x"]), max(current_body["y"]), max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(current_body["x"], current_body["y"], current_body["z"], c=random.choice(palette),
                label=current_body["name"])

    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend()
    plt.show()


def run_simulation(bodies, names=None, time_step=1, number_of_steps=10000, report_freq=100):
    # create output container for each body
    orbital_history = []
    for current_body in bodies:
        orbital_history.append({"x": [], "y": [], "z": [], "name": current_body.name})

    for i in range(1, number_of_steps):
        grav_step(bodies, time_step=1000)

        if i % report_freq == 0:
            for index, location in enumerate(orbital_history):
                location["x"].append(bodies[index].location.x)
                location["y"].append(bodies[index].location.y)
                location["z"].append(bodies[index].location.z)

    return orbital_history


'''
The planets are being somewhat arbitrarily graphed as a 2d plane at the start.  This is supremely unlikely,
in reality... but much easier to deal with in code.
'''
sun = {"location": Point(0, 0, 0), "mass": 2e30, "velocity": Point(0, 0, 0)}
mercury = {"location": Point(0, 5.7e10, 0), "mass": 3.285e23, "velocity": Point(47000, 0, 0)}
venus = {"location": Point(0, 1.1e11, 0), "mass": 4.8e24, "velocity": Point(35000, 0, 0)}
earth = {"location": Point(0, 1.5e11, 0), "mass": 6e24, "velocity": Point(30000, 0, 0)}
mars = {"location": Point(0, 2.2e11, 0), "mass": 2.4e24, "velocity": Point(24000, 0, 0)}
jupiter = {"location": Point(0, 7.7e11, 0), "mass": 1e28, "velocity": Point(13000, 0, 0)}
saturn = {"location": Point(0, 1.4e12, 0), "mass": 5.7e26, "velocity": Point(9000, 0, 0)}
uranus = {"location": Point(0, 2.8e12, 0), "mass": 8.7e25, "velocity": Point(6835, 0, 0)}
neptune = {"location": Point(0, 4.5e12, 0), "mass": 1e26, "velocity": Point(5477, 0, 0)}
pluto = {"location": Point(0, 3.7e12, 0), "mass": 1.3e22, "velocity": Point(4748, 0, 0)}

if __name__ == "__main__":
    # build list of planets in the simulation, or create your own
    bodies = [
        Body(location=sun["location"], mass=sun["mass"], velocity=sun["velocity"], name="sun"),
        Body(location=earth["location"], mass=earth["mass"], velocity=earth["velocity"], name="earth"),
        Body(location=mars["location"], mass=mars["mass"], velocity=mars["velocity"], name="mars"),
        Body(location=venus["location"], mass=venus["mass"], velocity=venus["velocity"], name="venus"),
    ]

    motions = run_simulation(bodies, time_step=100, number_of_steps=80000, report_freq=1000)
    plot_output(motions)