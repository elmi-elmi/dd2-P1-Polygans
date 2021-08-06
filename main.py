# main.py
import math
from math import sin, cos, pi


class Polygon:
    def __init__(self, n, R):
        self.n = n
        self.R = R
        self.angle = (n - 2) * 180 / n
        self.s = 2 * R * sin(pi / n)
        self.a = R * cos(pi / n)
        self.area = 0.5 * n * self.s * self.a
        self.perimeter = n * self.s


    