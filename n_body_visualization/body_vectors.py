#Define body and vector classes
from math import sqrt


class Vector:
    """ Vector class defining mathematical vector
    
    === Attributes ===
    x: x-component of vector
    y: y-component of vector
    """
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return str(f'{self.x}, {self.y}')

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __rsub__(self, other):
        if isinstance(other, Vector):
            return Vector(other.x - self.x, other.y - self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def norm(self) -> float:
        return sqrt(self.x**2 + self.y**2)


class Body:
    """ A body in an n-body system
    
    === Attributes ===
    
    mass: body's mass
    position: body's position vector
    velocity: body's velocity vector
    accelertion: body's acceleration vector
    """

    mass: float
    position: Vector
    velocity: Vector
    acceleration: Vector

    def __init__(self, mass: float, position: Vector) -> None:
        self.mass = mass
        self.position = position
        self.velocity = Vector(0, 0)
        self.acceleration = Vector(0, 0)
