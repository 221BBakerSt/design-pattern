"""
Observer pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


# abstract subject: it can be an interface so doesn't have to be a metaclass
class Observable(object):
    def __init__(self):
        pass

    def register(self, sub):
        pass

    def deactivate(self, sub):
        pass

    def notify(self):
        pass


# abstract observer
class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, notice):
        raise NotImplementedError(NOT_IMPLEMENTED)


# concrete subject
class Publisher(Observable):
    def __init__(self):
        self._subscribers = []

    def register(self, sub):
        self._subscribers.append(sub)

    def deactivate(self, sub):
        self._subscribers.remove(sub)

    def notify(self, notice):
        for sub in self._subscribers:
            sub.update(notice)


# concrete observer
class Subscriber(Observer):
    def __init__(self, pub):
        self.msg = []
        pub.register(self)

    def update(self, notice):
        self.msg.append(notice)

    def msg_box(self):
        return self.msg


if __name__ == "__main__":
    """client"""

    youtuber = Publisher()
    follower1 = Subscriber(youtuber)
    follower2 = Subscriber(youtuber)

    # the youtuber post a notice and the followers check their message boxes
    youtuber.notify("Welcome to my Youtube channel!")
    print(follower1.msg_box())
    print(follower2.msg_box())

    # the youtuber deactivates the follower 2 and posts another notice
    youtuber.deactivate(follower2)
    youtuber.notify("I posted my first video!")
    print(follower1.msg_box())
    # the follower 2 doesn't receive new notice anymore
    print(follower2.msg_box())
