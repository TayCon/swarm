from classes import sClass as s
import matplotlib.pyplot as plt
import matplotlib.animation as animation

"""
This is a test enviroment for tinkering around with 'floaters', or the small
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

swarm.addMember(f1)
swarm.addMember(f2)

fig = plt.figure()
ax = plt.axes(xlim=(0, s.squarea), ylim=(0, s.squarea))
lineF, = ax.plot([], [], 'bo')
lineC, = ax.plot([], [], 'ro')


def init():
    lineF.set_data([], [])
    lineC.set_data([], [])
    return lineF, lineC


def animate(*args):
    xF = []
    yF = []
    xA = []
    yA = []

    swarm.moveSwarmToDestinations()

    for i in swarm.getUncollided():
        xF.append(i.position.x)
        yF.append(i.position.y)

    swarm.checkForDetourNeeds()
    swarm.checkCollisions()

    for i in swarm.getCollided():
        xA.append(i.position.x)
        yA.append(i.position.y)

    lineF.set_data(xF, yF)
    lineC.set_data(xA, yA)

    return lineF, lineC


ani = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)
plt.show()
