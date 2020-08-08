import math


class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = value

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, value):
        # use radius instead of _radius to access public setter and ValueError
        self.radius = value / 2

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @area.setter
    def area(self, value):
        raise AttributeError('Cannot set value of area.')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.radius})"


if __name__ == '__main__':
    c = Circle(5)
    print(c.diameter)
    c.radius = -10


