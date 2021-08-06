# main.py
import math
from math import sin, cos, pi


class Polygon:
    def __init__(self, n, R):
        self.n = n  # edges / vertices
        self.R = R  # circumradius
        self.angle = (n - 2) * 180 / n
        self.s = 2 * R * sin(pi / n)  # edge length
        self.a = R * cos(pi / n)  # apothem
        self.area = 0.5 * n * self.s * self.a
        self.perimeter = n * self.s

    def __repr__(self):
        return f'Polygon(edges={self.n}, interior_angle={self.angle:0.3f},' \
               f'apothem={self.a:0.3f}, area={self.area:0.3f}, perimeter={self.perimeter:0.3f})'

    def __eq__(self, other):
        if isinstance(other, Polygon):
            return self.n == other.n and self.R == other.R

    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.n > other.n



