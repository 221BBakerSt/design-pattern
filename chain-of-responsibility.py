"""
Chain of Responsibility pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


# Abstract handler
class Handler(metaclass=ABCMeta):
    @abstractmethod
    def handle_leave(self, day):
        raise NotImplementedError(NOT_IMPLEMENTED)


# Concrete handler
class ProjectManager(Handler):
    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day <= 3:
            print(f"The project manager permits the {day}-day leave.")
        else:
            print("The project manager have no such authority!")
            self.next.handle_leave(day)


# Concrete handler
class DepartmentManager(Handler):
    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day <= 7:
            print(f"The department manager permits the {day}-day leave.")
        else:
            print("The department manager have no such authority!")
            self.next.handle_leave(day)


# Concrete handler
class GeneralManager(Handler):
    def handle_leave(self, day):
        if day <= 30:
            print(f"The general manager permits the {day}-day leave.")
        else:
            print("The general manager rejects this application of leave!")


if __name__ == "__main__":
    # client
    p = ProjectManager()
    p.handle_leave(3)
    print("-" * 50)
    p.handle_leave(20)
    print("-" * 50)
    p.handle_leave(40)
