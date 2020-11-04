from abc import ABCMeta, abstractmethod

"""
Simple Factory Pattern:
allows interfaces to create objects without exposing the object creation logic to the client.
"""
NOT_IMPLEMENTED = "You should implement this."


class FastFood(metaclass=ABCMeta):
    """role: abstract product"""

    @abstractmethod
    def __init__(self, qty: int, price: float):
        self.qty = qty
        self.price = price

    @abstractmethod
    def pay(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Burger(FastFood):
    """role: concrete product"""

    def __init__(self, qty, price=5.5):
        super().__init__(qty, price)

    def pay(self):
        return f"Burger price: {self.price * self.qty}"


class Chips(FastFood):
    """role: concrete product"""

    def __init__(self, qty, price=3.0):
        super().__init__(qty, price)

    def pay(self):
        return f"Chips price: {self.price * self.qty}"


class Coke(FastFood):
    """role: concrete product"""

    def __init__(self, qty, price=2.0):
        super().__init__(qty, price)

    def pay(self):
        return f"Coke price: {self.price * self.qty}"


class Order(object):
    """role: creator"""

    def buy(self, food, qty):
        if food == "burger":
            return Burger(qty)
        elif food == "chips":
            return Chips(qty)
        elif food == "coke":
            return Coke(qty)
        else:
            raise TypeError("No such category currently")


if __name__ == "__main__":
    order = Order()

    order1 = order.buy("burger", 3)
    print(order1.pay())

    order2 = order.buy("coke", 2)
    print(order2.pay())
