import time
from datetime import timedelta, datetime

from point import Point


class Robot(object):
    # Speed (m/s)
    speed = 0.1

    # How often to update position (seconds)
    updateDelay = 0.1

    # How long to move for, before re-evaluating the target (seconds)
    moveDuration = 1

    def __init__(self, id, match, arena):
        self.id = id
        self.match = match
        self.arena = arena
        self.opponents = set()
        self.location = Point()
        self._end = False

    def add_opponents(self, robots):
        for r in robots:
            if not r is self:
                self.opponents.add(r)

    def stop(self):
        self._end = True

    def run(self, corner, args = None):
        self.location = self.arena.corner_location(corner)
        self.match.wait_for_start()
        #print 'Game started: %d' % self._id

        while not self._end:
            target = self.get_target()
            self.move_towards(target)

    def move_towards(self, target):
        """
        Move towards the given Point for about a second
        """

        to_move = (target-self.location)
        #print 'to_move', to_move
        dist = to_move * self.speed
        #print 'dist', dist

        end = datetime.now() + timedelta(seconds = self.moveDuration)
        while datetime.now() < end:
        #print 'Location', self._location
            time.sleep(self.updateDelay)
            self.location = self.location + dist * self.updateDelay

    def get_target(self):
        """
        Figure out where to move towards.
        This is the interesting part of the robot's implementation
        """
        # move towards the middle of the arena
        return Point(self.arena.width / 2, self.arena.height / 2)

