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

    def __rmul__(self, value):
        return Point(
            x=value * self.x,
            y=value * self.y,
            z=value * self.z
        )

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


if __name__ == '__main__':
    p1 = Point(1, 2, 3)
    p2 = Point(1, 2, 3)
    print(3 * p2)
