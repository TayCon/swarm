from classes import sClass as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This is a test environment for tinkering around with 'floaters', or the small
little nodes that make up our swarm network. Better algorithms and more advanced
Tests ought to be written in other scripts for long-term preservation
"""

swarm_member_count = 0
swarm = s.Swarm(swarm_member_count)

f1 = s.Floater()
f1.position.set(s.squarea / 3, s.squarea / 2)
f1.destination.set(s.squarea * 19 / 20, s.squarea / 2)

f2 = s.Floater()
f2.position.set(s.squarea * 2 / 3, s.squarea / 2)
f2.destination.set(s.squarea / 20, s.squarea / 2)

swarm.add_member(f1)
swarm.add_member(f2)

fig = plt.figure()
ax = plt.axes(xlim=(0, s.squarea), ylim=(0, s.squarea))
lineF, = ax.plot([], [], 'bo')
lineC, = ax.plot([], [], 'ro')


def init():
    lineF.set_data([], [])
    lineC.set_data([], [])
    return lineF, lineC


def animate(*args):
    xf = []
    yf = []
    xa = []
    ya = []

    swarm.move_swarm_to_destinations()

    for i in swarm.get_uncollided():
        xf.append(i.position.x)
        yf.append(i.position.y)

    swarm.check_for_detour_needs()
    swarm.check_collisions()

    for i in swarm.get_collided():
        xa.append(i.position.x)
        ya.append(i.position.y)

    lineF.set_data(xf, yf)
    lineC.set_data(xa, ya)

    return lineF, lineC


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
plt.show()
