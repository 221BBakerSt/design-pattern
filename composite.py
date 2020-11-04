"""
Composite pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Graph(metaclass=ABCMeta):
    @abstractmethod
    def __str__(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Point(Graph):
    """Leaf"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"point({self.x}, {self.y})"


class Line(Graph):
    """Leaf"""

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __str__(self):
        return f"line({self.p1}, {self.p2})"


class Plane(Graph):
    """Composite"""

    def __init__(self, *args):
        self.children = []
        for stuff in args:
            self.children.append(stuff)

    def __str__(self):
        return str([stuff.__str__() for stuff in self.children])


if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(1, 1)
    line1 = Line(point1, point2)
    print(line1)
    plane1 = Plane(point1, point2, line1)
    print(plane1)
