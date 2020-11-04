"""
Abstract Factory Pattern:
an interface to create related objects without specifying/exposing their classes / 
provides an object of another factory that is responsible for creating required objects.
"""

from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Burger(metaclass=ABCMeta):
    """abstract product"""

    @abstractmethod
    def show_burger(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Chips(metaclass=ABCMeta):
    """abstract product"""

    @abstractmethod
    def show_chips(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Coke(metaclass=ABCMeta):
    """abstract product"""

    @abstractmethod
    def show_coke(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Restaurant(metaclass=ABCMeta):
    """abstract creator"""

    @abstractmethod
    def make_burger(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def make_chips(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def make_coke(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class CheeseBurger(Burger):
    """concrete product"""

    def show_burger(self):
        return "Here is a cheese burger"


class HamBurger(Burger):
    """concrete product"""

    def show_burger(self):
        return "Here is a ham burger"


class SmallChips(Chips):
    """concrete product"""

    def show_chips(self):
        return "Here are small chips"


class BigChips(Chips):
    """concrete product"""

    def show_chips(self):
        return "Here are big chips"


class Cocacola(Coke):
    """concrete product"""

    def show_coke(self):
        return "Here is a Cocacola"


class Pepsi(Coke):
    """concrete product"""

    def show_coke(self):
        return "Here is a Pepsi"


class KFC(Restaurant):
    """concrete creator"""

    def make_burger(self):
        return CheeseBurger()

    def make_chips(self):
        return SmallChips()

    def make_coke(self):
        return Pepsi()


class McDonalds(Restaurant):
    """concrete creator"""

    def make_burger(self):
        return HamBurger()

    def make_chips(self):
        return BigChips()

    def make_coke(self):
        return Cocacola()


class Order(object):
    """client"""

    def __init__(self, burger, chips, coke):
        self.burger = burger
        self.chips = chips
        self.coke = coke

    def show_info(self):
        print("Order info:")
        print(self.burger.show_burger())
        print(self.chips.show_chips())
        print(self.coke.show_coke())


def make_order(restaurant):
    """client"""

    burger = restaurant.make_burger()
    chips = restaurant.make_chips()
    coke = restaurant.make_coke()
    return Order(burger, chips, coke)


if __name__ == "__main__":

    m1 = make_order(KFC())
    m1.show_info()

    m2 = make_order(McDonalds())
    m2.show_info()
