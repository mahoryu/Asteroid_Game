from point import Point
from velocity import Velocity
from game import HIGHT, WIDTH

class FlyingObject():
    """
    The base class for any object that will fly accross the game screen.
    """
    def __init__(self):
        self._point = Point()
        self._velocity = Velocity()
        self._alive = True
        self._angle = 0
        self._radius = 0

    # Getters
    def getPoint(self):
        return self._point

    def getVelocity(self):
        return self._velocity

    def isAlive(self):
        return self._alive

    def getAngle(self):
        return self._angle

    def getRadius(self):
        return self._radius

    # Setters
    def setPoint(self, point):
        self._point = point

    def setVelocity(self, velocity):
        self._velocity = velocity

    def kill(self):
        self._alive = False

    def setAngle(self, angle):
        self._angle = angle

    def setRadius(self, radius):
        self._radius = radius

    # Properties
    point = property(getPoint,setPoint)
    velocity = property(getVelocity, setVelocity)
    angle = property(getAngle,setAngle)
    radius = property(getRadius, setRadius)

    def wrap(self):
        pass

    def advance(self):
        pass