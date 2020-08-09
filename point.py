from dataclasses import dataclass, astuple


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y}, z={self.z})"

    def __eq__(self, other):
        return (self.x, self.y, self.z) == (other.x, other.y, other.z)

    def __add__(self, other):
        return Point(
            x=self.x + other.x,
            y=self.y + other.y,
            z=self.z + other.z
        )

    def __sub__(self, other):
        return Point(
            x=self.x - other.x,
            y=self.y - other.y,
            z=self.z - other.z
        )

    def __mul__(self, value):
        return Point(
            x=self.x * value,
            y=self.y * value,
            z=self.z * value
        )

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


@dataclass
class Point:

    """Three-dimensional point."""

    x: float
    y: float
    z: float

    def __add__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1+x2, y1+y2, z1+z2)

    def __sub__(self, other):
        """Return copy of our point, shifted by other."""
        x1, y1, z1 = self
        x2, y2, z2 = other
        return Point(x1-x2, y1-y2, z1-z2)

    def __mul__(self, scalar):
        """Return new copy of our point, scaled by given value."""
        x, y, z = self
        return Point(scalar*x, scalar*y, scalar*z)

    __rmul__ = __mul__

    def __iter__(self):
        yield from astuple(self)


if __name__ == '__main__':
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    print(3 * p2)
