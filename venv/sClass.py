import random
import numpy
import math
import uuid

squarea = 400  # The Square Area of the window


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
        self.destination = Coordinate(squarea/2, squarea/2)

    def makeLeader(self):
        self.isLeader = True
        # Change color to Blue at this point

    def collide(self):
        self.hasCollided = True
        # Change color to Red at this point

    def moveRandomly(self):
        if not self.hasCollided:
            self.position.x = self.position.x + random.randint(-1, 1)
            self.position.y = self.position.y + random.randint(-1, 1)

            # keeps random movements within bounds
            if self.position.x > squarea: self.position.x = squarea
            if self.position.x < 0: self.position.x = 0
            if self.position.y > squarea: self.position.y = squarea
            if self.position.y < 0: self.position.y = 0

    def moveToDestination(self):
        if not self.hasCollided:
            if self.position.x < self.destination.x: self.position.x += 1
            if self.position.x > self.destination.x: self.position.x -= 1
            if self.position.y < self.destination.y: self.position.y += 1
            if self.position.y > self.destination.y: self.position.y -= 1
