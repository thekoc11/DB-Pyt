import math as Math

class Vector:
    length = 0
    angle = 0
    X = 0
    Y = 0
    def __init__(self, x, y):
        self.setX(x)
        self.setY(y)
        self.setAngle(self.getAngle())
        self.setLength(self.getLength())
        # self.setLength(Math.sqrt(x**2 + y**2))
        # self.setAngle(Math.atan2(y, x))
        #return self
    def setX(self, x):
        self.X = x
    def setY(self, y):
        self.Y = y
    def setLength(self, l):
        self.length = l
    def setAngle(self, a):
        self.angle = a
    def getX(self):
        x = self.length * Math.cos(self.angle)
        return x
    def getY(self):
        y = self.length * Math.sin(self.angle)
        return y
    def getLength(self):
        l = Math.sqrt(self.X ** 2 + self.Y ** 2)
        return l

    def getAngle(self):
        a = Math.atan2(self.Y, self.X)
        return a
    def createP(self, l, a):
        self.setLength(l)
        self.setAngle(a)
        self.setX(self.getX())
        self.setY(self.getY())
        return self
    def addVec(self, V):
        self.setX(self.X + V.X)
        self.setY(self.Y + V.Y)
        return self
    def subtractVec(self, V):
        self.setX(self.X - V.X)
        self.setY(self.Y - V.Y)
        return self

