# vector3d.py

import math

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_points(cls, p1, p2):
        return cls(p2.x - p1.x, p2.y - p1.y, p2.z - p1.z)

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z

    def cross(self, other):
        return Vector3D(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def unit(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot convert zero vector to unit vector")
        return Vector3D(self.x / mag, self.y / mag, self.z / mag)

    def __eq__(self, other):
        return math.isclose(self.x, other.x) and math.isclose(self.y, other.y) and math.isclose(self.z, other.z)

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"
