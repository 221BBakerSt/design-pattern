"""
Bridge pattern example.
"""
from abc import ABCMeta, abstractmethod


NOT_IMPLEMENTED = "You should implement this."


# Abstraction
class Shape(metaclass=ABCMeta):
    # low-level
    @abstractmethod
    def draw(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    # high-level
    @abstractmethod
    def resizeByPercentage(self, pct):
        raise NotImplementedError(NOT_IMPLEMENTED)


# Refined Abstraction
class Circle(Shape):
    def __init__(self, x, y, radius, pen):
        self.__x = x
        self.__y = y
        self.__radius = radius
        self.__pen = pen

    # low-level i.e. Implementation specific
    def draw(self):
        self.__pen.drawCircle(self.__x, self.__y, self.__radius)

    # high-level i.e. Abstraction specific
    def resizeByPercentage(self, pct):
        self.__radius *= pct


# Implementor
class Pen(metaclass=ABCMeta):
    @abstractmethod
    def drawCircle(self, x, y, radius):
        raise NotImplementedError(NOT_IMPLEMENTED)


# Concrete Implementor 1/2
class Pencil(Pen):
    def drawCircle(self, x, y, radius):
        print(f"circle1 at {x}:{y} radius {radius}")


# Concrete Implementor 2/2
class Ballpen(Pen):
    def drawCircle(self, x, y, radius):
        print(f"circle2 at {x}:{y} radius {radius}")


# client
def main():
    shapes = [Circle(1, 2, 3, Pencil()), Circle(5, 7, 11, Ballpen())]

    for shape in shapes:
        shape.resizeByPercentage(2.5)
        shape.draw()


if __name__ == "__main__":
    main()
