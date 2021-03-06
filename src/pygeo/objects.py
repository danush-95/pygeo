import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self._point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Point({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False


class Ray:
    """This class represents a ray"""
    def __init__(self,origin_p,dir_r):
        self._origin = np.array(origin_p)
        self._direction = np.array(dir_r)
        
    def __repr__(self):
        return f"Ray origin ({self._origin.tolist()}) and  Ray direction({self._direction.tolist()})"
        
     
    def __eq__(self,other):
        if isinstance(other, Ray):
            return np.array_equal(self._origin,other._origin) and np.array_equal(self._direction,other._direction)
        return False 

class Sphere:
    """A Sphere class with centre and radius"""
    def __init__(self,centre,radius):
        self._centre = np.array(centre)
        self._radius = np.array(radius)
    
    def __repr__(self):
        return f"Sphere centre ({self._centre.tolist()}) and  Sphere radius({self._radius.tolist()})"
        
     
    def __eq__(self,other):
        if isinstance(other,Sphere):
            return np.array_equal(self._centre,other._centre) and np.array_equal(self._radius,other._radius)
        return False 

class Triangle:
    """ Triangle class with 3 vertices"""
    def __init__(self,vertices):
        self.v = np.array(vertices)
        self.v0 = np.array(vertices[0])
        self.v1 = np.array(vertices[1])
        self.v2 = np.array(vertices[2])
        
    def __repr__(self):
        return f"Traingle vertices({self.v.tolist()})"
         
    def __eq__(self,other):
        if isinstance(other,Triangle):
            return np.array_equal(self.v,other.v)
        return False 
    
    def __sub__(self,other):
        if isinstance(other,Triangle):
            return self.v - other.v
