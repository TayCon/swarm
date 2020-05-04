import random
import numpy
import math
import uuid

squarea = 200  # The Square Area of the window


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set(self, x, y):
        self.x = x
        self.y = y

class Floater:
    def __init__(self):
        self.id = uuid.uuid4()
        self.isLeader = False
        self.hasCollided = False
        self.size = 5
        self.position = Coordinate(random.randint(1, squarea - 1), random.randint(1, squarea - 1))
        self.destination = Coordinate(squarea / 2, squarea / 2)
        self.detour = Coordinate(None, None)
        self.trajectory = Coordinate(None, None)

    def makeLeader(self):
        self.isLeader = True
        #TODO Change color to Blue at this point

    def collide(self):
        self.hasCollided = True
        #TODO Change color to Red at this point

    def moveRandomly(self):
        if not self.hasCollided:
            if abs(self.position.x - self.destination.x) < 1 and abs(self.position.y - self.destination.y) < 1:
                self.destination.set(random.randint(0, squarea), random.randint(0, squarea))
            else:
                self.moveToDestination()


    def moveToDestination(self):
        detour_flag = False
        if not self.hasCollided:
            if self.detour.x == None and self.detour.y == None:
                target = self.destination
            else:
                target = self.detour
                detour_flag = True

            y_dist = target.y - self.position.y
            x_dist = target.x - self.position.x
            distToDestination = math.sqrt((y_dist ** 2) + (x_dist ** 2))

            if distToDestination == 0:
                return

            self.trajectory.x = (x_dist / distToDestination)
            self.trajectory.y = (y_dist / distToDestination)

            self.position.x += self.trajectory.x
            self.position.y += self.trajectory.y

            if detour_flag and abs(self.position.x - target.x) < 1 and abs(self.position.y - target.y) < 1:
                self.detour.set(None, None)

    def makeDetour(self):
        detour_distance = 5
        trajectory_angle = numpy.arctan2(self.trajectory.y, self.trajectory.x)
        detour_angle = trajectory_angle - (numpy.pi / 4)  # angle 45 degrees right
        self.detour.x = self.position.x + (detour_distance * numpy.cos(detour_angle))
        self.detour.y = self.position.y + (detour_distance * numpy.sin(detour_angle))


class Swarm:
    def __init__(self, memberSize):
        self.collision_tolerance = 3
        self.detour_radius = 5
        "" \
        ""
        self.member_count = memberSize
        self.members = []

        for i in range(self.member_count):
            self.members.append(Floater())

    def addMember(self, new_floater):
        self.members.append(new_floater)
        self.member_count += 1

    def withinTolerance(self, num1, num2):
        if abs(num1 - num2) <= self.collision_tolerance:
            return True
        else:
            return False

    def checkForDetourNeeds(self):
        for i in self.members:
            for j in self.members:
                if i.id != j.id:
                    if numpy.sqrt((i.position.x-j.position.x)**2 + (i.position.y-j.position.y)**2) < self.detour_radius:
                        i.makeDetour()
    def checkCollisions(self):
        for i in self.members:
            for j in self.members:
                if i.id != j.id:
                    if self.withinTolerance(i.position.x, j.position.x) and self.withinTolerance(i.position.y,
                                                                                                 j.position.y):
                        i.collide()
                        j.collide()

    def moveSwarmStochasticly(self):
        for i in self.members:
            i.moveRandomly()

    def moveSwarmToDestinations(self):
        for i in self.members:
            i.moveToDestination()

    def setCommonDestination(self, x, y):
        for i in self.members:
            i.destination.set(x, y)

    def setRandomDestination(self):
        for i in self.members:
            i.destination.set(random.randint(0, squarea), random.randint(0, squarea))

    def getUncollided(self):
        uncollided = []
        for i in self.members:
            if not i.hasCollided:
                uncollided.append(i)
        return uncollided

    def getCollided(self):
        collided = []
        for i in self.members:
            if i.hasCollided:
                collided.append(i)
        return collided