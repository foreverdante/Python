#!/usr/local/env python3
#Created By: J.Medlock
#Created On: 2017.09.08

import math
from math import pi

class RectangleFinder(object):
    def __init__(self, length, width):
        self.length = length #Sets the square variable for later use
        self.width = width

    def rectangle(self):
        total = float(length * width)
        return "The total area is %0.2f " % total

class TriangleArea(object):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def triangle(self):
        total = float((base / 2) * height)
        return "The total area is %0.2f " % total

class CircleArea(object):
    def __init__(self, circ):
        self.circ = circ

    def circle(self):
        total = float(math.pi * math.pow(radius,2))
        #print("The total area is %d" % total)
        return "The total area is: %0.2f " % total

if __name__ == '__main__':
    choice = input("Enter R for rectangle, T for triangle or C for circle: ")

    if choice.upper() == "R":
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        rect = RectangleFinder(length, width)
        rect.rectangle()
        print(rect.rectangle())

    elif choice.upper() == "T":
        base = float(input("Please enter the base length: "))
        height = float(input("Please enter the height: "))

        tri = TriangleArea(base, height)
        tri.triangle()
        print(tri.triangle())

    elif choice.upper() == "C":
        radius = float(input("Enter the radius of the circle: "))

        circ = CircleArea(radius)
        circ.circle()
        print(circ.circle())
    else:
        print("Please enter a correct option.")
