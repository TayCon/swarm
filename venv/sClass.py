import random
import numpy
import math
import uuid

squarea = 60 #The Square Area of the window

class Floater:
    def __init__(self):
        self.id = uuid.uuid4()
        self.isLeader = False
        self.hasCollided = False
        self.size = 2
        self.x_coordinate = random.randint(1, squarea - 1)
        self.y_coordinate = random.randint(1, squarea - 1)

    def makeLeader(self):
        self.isLeader = True
        #Change color to Blue at this point

    def collide(self):
        self.hasCollided = True
        #Change color to Red at this point
        
    
    def moveRandomly(self):
        if not self.hasCollided:
            self.x_coordinate = self.x_coordinate + random.randint(-1, 1)
            self.y_coordinate = self.y_coordinate + random.randint(-1, 1)
            
            #keeps random movements within bounds
            if self.x_coordinate>squarea:self.x_coordinate = squarea
            if self.x_coordinate<0:self.x_coordinate=0
            if self.y_coordinate>squarea:self.y_coordinate = squarea
            if self.y_coordinate<0:self.y_coordinate=0
