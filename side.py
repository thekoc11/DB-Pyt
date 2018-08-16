from vec import Vector
from math import *
class side:
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    slope = 0
    length = 0
    angle = 0
    _s = None

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self._s = Vector(x2-x1, y2-y1)
        self.length = sqrt((x2-x1)**2 + (y2-y1)**2)
        self.slope = self._s.getSlope()
        self.angle = self._s.getAngle()

    def getX1(self):
        return self.x1
    def getX2(self):
        return self.x2
    def getY1(self):
        return self.y1
    def getY2(self):
        return self.y2

    def getLength(self):
        return self.length

    def getX_Intercept(self):
        return (self.slope*self.x1 - self.y1)/self.slope

    def getY_Intercept(self):
        m = self.slope
        return self.y1 - m * self.x1

    def distanceFromOrigin(self):
        a = self.slope
        b = -1
        c = self.getY_Intercept()
        dist = abs(a*0 + b*0 + c)/sqrt(a*a + b*b)
        return dist


