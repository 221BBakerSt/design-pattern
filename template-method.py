"""
Template method pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Person(metaclass=ABCMeta):
    @abstractmethod
    def chew(self):
        raise NotImplementedError()

    def swallow(self):
        print("swallow")

    def eat(self):
        self.chew()
        self.swallow()


class Man(Person):
    def chew(self):
        print("chew fast")


class Woman(Person):
    def chew(self):
        print("chew slowly")


if __name__ == "__main__":
    """client"""
    person1 = Man()
    person1.eat()

    person2 = Woman()
    person2.eat()
