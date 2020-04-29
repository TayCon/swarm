import sClass
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import uuid
"""
This is a test enviroment for tinkering around with 'floaters', or the small
little nodes that make up our swarm network. Better algorithms and more advanced
Tests ought to be written in other scripts for long-term preservation
"""

swarm_member_count = 50
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
    xF = []
    yF = []
    xA = []
    yA = []

    for i in swarm:
        i.moveRandomly()
        xF.append(i.x_coordinate)
        yF.append(i.y_coordinate)

    for i in swarm:
        for j in swarm:
            if i.id!=j.id and i.x_coordinate==j.x_coordinate and i.y_coordinate==j.y_coordinate:
                i.collide()
                j.collide()

    for i in swarm:
        if i.hasCollided:
            xA.append(i.x_coordinate)
            yA.append(i.y_coordinate)

    lineF.set_data(xF, yF)
    lineC.set_data(xA, yA)

    return lineF, lineC

ani = animation.FuncAnimation(fig, animate, init_func=init, frames = 100, interval=20, blit=True)
plt.show()