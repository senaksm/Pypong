import collections

from enums import Direction

Point = collections.namedtuple('Point', ['x', 'y'])


def intersection(self, other):
    if self.corners[0].x <= other.corners[0].x <= self.corners[1].x:
        if other.corners[0].y <= self.corners[0].y <= other.corners[1].y:
            return Direction.RIGHT
        return
    if self.corners[1].x <= other.corners[1].x <= self.corners[0].x:
        if other.corners[0].y <= self.corners[1].y <= other.corners[1].y:
            return Direction.LEFT
        return