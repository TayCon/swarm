from classes import sClass
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This is a test enviroment for tinkering around with 'floaters', or the small
little nodes that make up our swarm network. Better algorithms and more advanced
Tests ought to be written in other scripts for long-term preservation
"""

swarm_member_count = 100
swarm = []
collided = []

for i in range(swarm_member_count):
    swarm.append(sClass.Floater())

fig = plt.figure()
ax = plt.axes(xlim=(0, sClass.squarea), ylim=(0, sClass.squarea))
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

    for i in swarm:
        i.move_to_destination()
        xf.append(i.position.x)
        yf.append(i.position.y)

    for i in swarm:
        for j in swarm:
            if i.id != j.id and i.position.x == j.position.x and i.position.y == j.position.y:
                i.collide()
                j.collide()

    for i in swarm:
        if i.has_collided:
            xa.append(i.position.x)
            ya.append(i.position.y)

    lineF.set_data(xf, yf)
    lineC.set_data(xa, ya)

    return lineF, lineC


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
plt.show()
