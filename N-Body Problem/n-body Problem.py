import math
import matplotlib.pyplot as plt

'''
These three boolean values allow different sets of pre-programmed bodies to used in the n-Body calculation.  Only one
of the three should be set to True at any given time.

Number of steps in the 'run simulation' function needs to be set to a ridiculously large number and the runtime is quite
long if solar_system_complete is set to True.  If using custom_planets, it is not recommended to specify more than 5
bodies, for the same reason.
'''
solar_system_gas_giants = False
solar_system_inner = False
custom_planets = True

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


class Body:
    def __init__(self, position, mass, velocity, name="", color=""):
        self.position = position
        self.mass = mass
        self.velocity = velocity
        self.name = name
        self.color = color

'''
Acceleration computation for single body.
'''
def compute_sba(bodies, body_index):
    grav = 6.67408e-11
    acc = Point(0, 0, 0)
    current_body = bodies[body_index]

    for index, other in enumerate(bodies):
        if index != body_index:
            r = (current_body.position.x - other.position.x) ** 2 + (
                        current_body.position.y - other.position.y) ** 2 + (
                            current_body.position.z - other.position.z) ** 2
            r = math.sqrt(r)
            tmp = grav * other.mass / r ** 3
            acc.x += tmp * (other.position.x - current_body.position.x)
            acc.y += tmp * (other.position.y - current_body.position.y)
            acc.z += tmp * (other.position.z - current_body.position.z)

    return acc


def update_velocity(bodies, time_step=1):
    for index, current_body in enumerate(bodies):
        acceleration = compute_sba(bodies, index)

        current_body.velocity.x += acceleration.x * time_step
        current_body.velocity.y += acceleration.y * time_step
        current_body.velocity.z += acceleration.z * time_step


def update_position(bodies, time_step=1):
    for body in bodies:
        body.position.x += body.velocity.x * time_step
        body.position.y += body.velocity.y * time_step
        body.position.z += body.velocity.z * time_step


def grav_step(bodies, time_step=1):
    update_velocity(bodies, time_step=time_step)
    update_position(bodies, time_step=time_step)


def plot_orbits(bodies):
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    max_range = 0

    for current_body in bodies:
        max_dim = max(max(current_body["x"]), max(current_body["y"]), max(current_body["z"]))
        if max_dim > max_range:
            max_range = max_dim
        ax.plot(current_body["x"], current_body["y"], current_body["z"], c=current_body["color"],
                label=current_body["name"])

    ax.set_xlim([-max_range, max_range])
    ax.set_ylim([-max_range, max_range])
    ax.set_zlim([-max_range, max_range])
    ax.legend()
    plt.show()


def run_simulation(bodies, names=None, time_step=1, number_of_steps=500000, report_freq=100):
    orbital_history = []

    for current_body in bodies:
        orbital_history.append({"x": [], "y": [], "z": [], "name": current_body.name, "color": current_body.color})

    for i in range(1, number_of_steps):
        grav_step(bodies, time_step=1000)

        if i % report_freq == 0:
            for index, position in enumerate(orbital_history):
                position["x"].append(bodies[index].position.x)
                position["y"].append(bodies[index].position.y)
                position["z"].append(bodies[index].position.z)

    return orbital_history


'''
The planets are being somewhat arbitrarily graphed as a 2d plane at the start.  This is supremely unlikely,
in reality... but much easier to deal with in code.  This data was not readily available or estimable for
Gliese.  These velocity figures are also extremely rough - lacking better values however, this is what the
program has to work with.

The second set of four bodies (one star and three planets) are for the 'custom_stars' set, and consist entirely
of positions taken from works of fiction. No attempt was made to match the values involved with these objects with
any existing information in the source material from which they exist. (I just needed some names, and I like science
fiction).  The values given here will plot a (wildly) unstable orbit.
'''

sun = {"position": Point(0, 0, 0), "mass": 2e30, "velocity": Point(0, 0, 0)}
mercury = {"position": Point(0, 5.7e10, 0), "mass": 3.285e23, "velocity": Point(47000, 0, 0)}
venus = {"position": Point(0, 1.1e11, 0), "mass": 4.8e24, "velocity": Point(35000, 0, 0)}
earth = {"position": Point(0, 1.5e11, 0), "mass": 6e24, "velocity": Point(30000, 0, 0)}
mars = {"position": Point(0, 2.2e11, 0), "mass": 2.4e24, "velocity": Point(24000, 0, 0)}
jupiter = {"position": Point(0, 7.7e11, 0), "mass": 1e28, "velocity": Point(13000, 0, 0)}
saturn = {"position": Point(0, 1.4e12, 0), "mass": 5.7e26, "velocity": Point(9000, 0, 0)}
uranus = {"position": Point(0, 2.8e12, 0), "mass": 8.7e25, "velocity": Point(6835, 0, 0)}
neptune = {"position": Point(0, 4.5e12, 0), "mass": 1e26, "velocity": Point(5477, 0, 0)}
pluto = {"position": Point(0, 3.7e12, 0), "mass": 1.3e22, "velocity": Point(4748, 0, 0)}

rao = {"position": Point(0, 0, 0), "mass": 4.1e30, "velocity": Point(0, 0, 0)}
arrakis = {"position": Point(0, 2.2e11, 0), "mass": 5.1e24, "velocity": Point(36000, 0, 0)}
risa = {"position": Point(0, 3.4e11, 0), "mass": 4.8e24, "velocity": Point(10100, 0, 0)}
ego = {"position": Point(0, 3.9e11, 0), "mass": 2e26, "velocity": Point(9865, 0, 0)}

if __name__ == "__main__":
    if solar_system_gas_giants:
        bodies = [
            Body(position=sun["position"], mass=sun["mass"], velocity=sun["velocity"], name="Sun", color="gold"),
            Body(position=jupiter["position"], mass=jupiter["mass"], velocity=jupiter["velocity"], name="Jupiter",
                 color="orange"),
            Body(position=saturn["position"], mass=saturn["mass"], velocity=saturn["velocity"], name="Saturn",
                 color="lemonchiffon"),
            Body(position=neptune["position"], mass=neptune["mass"], velocity=neptune["velocity"], name="Neptune",
                 color="steelblue"),
            Body(position=uranus["position"], mass=uranus["mass"], velocity=uranus["velocity"], name="Uranus",
                 color="mediumturquoise")
        ]

    elif solar_system_inner:

        bodies = [
            Body(position=sun["position"], mass=sun["mass"], velocity=sun["velocity"], name="Sun", color="gold"),
            Body(position=mercury["position"], mass=mercury["mass"], velocity=mercury["velocity"], name="Mercury",
                 color="burlywood"),
            Body(position=venus["position"], mass=venus["mass"], velocity=venus["velocity"], name="Venus",
                 color="magenta"),
            Body(position=earth["position"], mass=earth["mass"], velocity=earth["velocity"], name="Earth",
                 color="mediumblue"),
            Body(position=mars["position"], mass=mars["mass"], velocity=mars["velocity"], name="Mars",
                 color="firebrick")
        ]

    elif custom_planets:

        bodies = [
            Body(position=rao["position"], mass=rao["mass"], velocity=rao["velocity"], name="Rao", color="red"),
            Body(position=arrakis["position"], mass=arrakis["mass"], velocity=arrakis["velocity"], name="Arrakis",
                 color="khaki"),
            Body(position=risa["position"], mass=risa["mass"], velocity=risa["velocity"], name="Risa",
                 color="magenta"),
            Body(position=ego["position"], mass=ego["mass"], velocity=ego["velocity"], name="Ego", color="teal")
        ]

    motions = run_simulation(bodies, time_step=100, number_of_steps=2000000, report_freq=1000)
    plot_orbits(motions)