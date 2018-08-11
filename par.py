from vec import Vector

class Particle(Vector):
    mass = 0
    p = None
    v = None
    a = 0
    timeToNextCollision = 0
    def __init__(self, x, y, vx, vy):
        self.setPosition(x, y)
        self.setVelocity(vx, vy)
        self.timeToNextCollision = 0

    def setVelocity(self, vx, vy):
        self.v = Vector(vx, vy)

    def setPosition(self, x, y):
        self.p = Vector(x, y)

    def setTime(self, t):
        self.timeToNextCollision = t

    def getPosition(self):
        if self.p is None:
            return self.p
        else:
            print("position not set")

    def getVelocity(self):
        if self.v is None:
            return self.v
        else:
            print("Velocity not set")

    def update(self):
        incident = self.v.getAngle()


