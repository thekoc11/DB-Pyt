from vec import Vector
from par import Particle
from side import Side
from math import *
import random as rn
class Shape:
    sides = []
    verts = []
    vertsX = []
    vertsY = []
    side = 3
    noOfVert = 3
    _vertX = 0
    _vertY = 0
    _sideX = []
    _sideY = []

    def __init__(self, n, T):
        side = 3
        self.noOfVert = self.getRandomInt(n)
        print("No of Vertices is: ", self.noOfVert)

        for i in range(self.noOfVert):
            if T is 1:
                self.generateRandomPoint()
            else:
                self.generateRandomPointRational()

            vertLen = len(self.verts)
            if i > 0:
                for j in range(1):
                    self._sideX.append(self.verts[vertLen - (2 - j)].getX())
                    self._sideY.append(self.verts[vertLen - (2 - j)].getY())
                __s = Side(self._sideX[0], self._sideY[0], self._sideX[1], self._sideY[1])
                self.sides.append(__s)
                self._sideX.pop()
                self._sideY.pop()
        if len(self.sides) == len(self.verts) - 1:
            l = len(self.verts) - 1
            __S = Side(self.verts[1].getX, self.verts[1].getY(), self.verts[0].getX, self.verts[0].getY())
            self.sides.append(__S)


    def getRandomInt(self, max):
        max = floor(max)
        return floor(rn.random * (max - 3) + 3)

    def generateRandomPoint(self):
        if len(self.verts) < 1:
            _side = Vector(50, 50)
            _length = _side.getLength()
            lenGen = rn.random * _length / 4 + 0.75 * _length
            angleGen = 0
            tempVert = Vector(0, 0)
            tempVert = Vector.createP(tempVert, lenGen, angleGen)
            self.verts.append(tempVert)
        else:
            lv = len(self.verts)
            recentAngle = self.verts[lv - 1].getAngle()
            angleGen = rn.random * (360 / self.noOfVert) + recentAngle
            lenGen = self.verts[lv - 1].getLength()

            tempVert = Vector(0, 0)
            tempVert = Vector.createP(tempVert, lenGen, angleGen)

            self.verts.append(tempVert)

    def generateRandomPointRational(self):
        if len(self.verts) < 1:
            _side = Vector(50, 50)
            _length = _side.getLength()
            lenGen = rn.random * _length/4 + 0.75*_length
            angleGen = 0
            tempVert = Vector(0, 0)
            tempVert = Vector.createP(tempVert, lenGen, angleGen)
            self.verts.append(tempVert)
        else:
            lv = len(self.verts)
            recentAngle  = self.verts[lv-1].getAngle()
            angleGen = (360/self.noOfVert) + recentAngle
            lenGen = self.verts[lv-1].getLength()

            tempVert = Vector(0, 0)
            tempVert = Vector.createP(tempVert, lenGen, angleGen)

            self.verts.append(tempVert)
    def particleInitiator(self):
        s = []
        l = len(self.sides)

        for i in range(l):
            s.append(self.sides[i])

        return rn.random #* min of sides[i].distance from origin

    def getDirection(self, sides, verts):
        s1 = sides[0]
        s2 = sides[1]
        s3 = sides[3]
        for i in range(3):
            print("from function", sides[i].getAngle(), "  ", sides[i].getSlope())

        angle1 = s1.getAngle()
        angle2 = s2.getAngle()
        angle3 = s3.getAngle()

        return (angle2 - angle1)

    def calcTimeIndex(self, p):
        _an = p.v.getAngle()
        time = 1
        ti = []
        tj = []
        least_index = 0

        x1 = p.p.getX()
        y1 = p.p.getY()
        vx = p.v.getX()
        vy = p.v.getY()

        print("Particle Position and Velocity are", x1, " ", y1, " : ", vx, " ", vy)

        s = len(self.sides)
        for i in range(s):
            m = self.sides[i].getSlope()
            c = self.sides[i].getY_Intercept()
            ti.append((m*x1 + c - y1)/(vy - m*vx))
            if ti[i] <= 0.00001:
                tj.append(inf)
            else:
                tj.append(ti[i])
            if tj[i] < tj[least_index]:
                least_index = i

        p.setTime(tj[least_index])

        return least_index
