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
        self.is_leader = False
        self.has_collided = False
        self.size = 5
        self.position = Coordinate(random.randint(1, squarea - 1), random.randint(1, squarea - 1))
        self.destination = Coordinate(squarea / 2, squarea / 2)
        self.detour = Coordinate(None, None)
        self.trajectory = Coordinate(None, None)

    def make_leader(self):
        self.is_leader = True
        # TODO Change color to Blue at this point

    def collide(self):
        self.has_collided = True
        # TODO Change color to Red at this point

    def move_randomly(self):
        if not self.has_collided:
            if abs(self.position.x - self.destination.x) < 1 and abs(self.position.y - self.destination.y) < 1:
                self.destination.set(random.randint(0, squarea), random.randint(0, squarea))
            else:
                self.move_to_destination()

    def move_to_destination(self):
        detour_flag = False
        if not self.has_collided:
            if self.detour.x is None and self.detour.y is None:
                target = self.destination
            else:
                target = self.detour
                detour_flag = True

            y_dist = target.y - self.position.y
            x_dist = target.x - self.position.x
            dist_to_destination = math.sqrt((y_dist ** 2) + (x_dist ** 2))

            if dist_to_destination == 0:
                return

            self.trajectory.x = (x_dist / dist_to_destination)
            self.trajectory.y = (y_dist / dist_to_destination)

            self.position.x += self.trajectory.x
            self.position.y += self.trajectory.y

            if detour_flag and abs(self.position.x - target.x) < 1 and abs(self.position.y - target.y) < 1:
                self.detour.set(None, None)

    def make_detour(self, other):
        detour_distance = 8
        trajectory_angle = numpy.arctan2(self.trajectory.y, self.trajectory.x)
        diff_x, diff_y = (other.position.x - self.position.x, other.position.y - self.position.y)
        angle_with_other = numpy.arctan2(diff_y, diff_x)
        # detour_angle = trajectory_angle - (numpy.pi / 4)  # angle 45 degrees right
        detour_angle = trajectory_angle - angle_with_other + (numpy.pi / 12)
        self.detour.x = self.position.x + (detour_distance * numpy.cos(detour_angle))
        self.detour.y = self.position.y + (detour_distance * numpy.sin(detour_angle))


class Swarm:
    def __init__(self, member_size):
        self.collision_tolerance = 3
        self.detour_radius = 10
        "" \
        ""
        self.member_count = member_size
        self.members = []

        for i in range(self.member_count):
            self.members.append(Floater())

    def add_member(self, new_floater):
        self.members.append(new_floater)
        self.member_count += 1

    def within_tolerance(self, num1, num2):
        if abs(num1 - num2) <= self.collision_tolerance:
            return True
        else:
            return False

    def check_for_detour_needs(self):
        for i in self.members:
            for j in self.members:
                if i.id != j.id:
                    if numpy.sqrt((i.position.x - j.position.x) ** 2 + (
                            i.position.y - j.position.y) ** 2) < self.detour_radius:
                        i.make_detour(j)
                        j.make_detour(i)

    def check_collisions(self):
        for i in self.members:
            for j in self.members:
                if i.id != j.id:
                    if self.within_tolerance(i.position.x, j.position.x) and self.within_tolerance(i.position.y,
                                                                                                   j.position.y):
                        i.collide()
                        j.collide()

    def move_swarm_stochastically(self):
        for i in self.members:
            i.move_randomly()

    def move_swarm_to_destinations(self):
        for i in self.members:
            i.move_to_destination()

    def set_common_destination(self, x, y):
        for i in self.members:
            i.destination.set(x, y)

    def set_random_destination(self):
        for i in self.members:
            i.destination.set(random.randint(0, squarea), random.randint(0, squarea))

    def get_uncollided(self):
        uncollided = []
        for i in self.members:
            if not i.has_collided:
                uncollided.append(i)
        return uncollided

    def get_collided(self):
        collided = []
        for i in self.members:
            if i.has_collided:
                collided.append(i)
        return collided
