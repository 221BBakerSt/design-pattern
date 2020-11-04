from abc import ABCMeta, abstractmethod

"""
Factory Method Pattern:
allows interfaces for creating objects, but allow subclasses to determine which class to instantiate.
"""
NOT_IMPLEMENTED = "You should implement this."


class KFC(metaclass=ABCMeta):
    """role: abstract product"""

    @abstractmethod
    def __init__(self, qty: int, price: float):
        self.qty = qty
        self.price = price

    @abstractmethod
    def pay(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Burger(KFC):
    """role: concrete product"""

    def __init__(self, qty, price=5.5):
        KFC.__init__(self, qty, price)

    def pay(self):
        return f"Burger price: {self.price * self.qty}"


class Chips(KFC):
    """role: concrete product"""

    def __init__(self, qty, price=3.0):
        KFC.__init__(self, qty, price)

    def pay(self):
        return f"Chips price: {self.price * self.qty}"


class Coke(KFC):
    """role: concrete product"""

    def __init__(self, qty, price=2.0):
        KFC.__init__(self, qty, price)

    def pay(self):
        return f"Coke price: {self.price * self.qty}"


class Order(metaclass=ABCMeta):
    """role: abstract creator"""

    @abstractmethod
    def buy(self, qty):
        raise NotImplementedError(NOT_IMPLEMENTED)


class OrderBurger(Order):
    """role: concrete creator"""

    def buy(self, qty):
        return Burger(qty)


class OrderChips(Order):
    """role: concrete creator"""

    def buy(self, qty):
        return Chips(qty)


class OrderCoke(Order):
    """role: concrete creator"""

    def buy(self, qty):
        return Coke(qty)


if __name__ == "__main__":
    order_burger = OrderBurger()
    order1 = order_burger.buy(3)
    print(order1.pay())

    order_coke = OrderCoke()
    order2 = order_coke.buy(2)
    print(order2.pay())
