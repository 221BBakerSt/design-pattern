from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Repas(object):
    """product"""

    def __init__(self):
        self.aperitif = None
        self.entree = None
        self.main_course = None
        self.dessert = None

    def __str__(self):
        info = f"Aperitif: {self.aperitif}, Entree: {self.entree}, Main course: {self.main_course}, Dessert: {self.dessert}"
        return info.replace(", ", "\n")


class Chef(metaclass=ABCMeta):
    """abstract builder"""

    @abstractmethod
    def make_aperitif(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def make_entree(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def make_main_course(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def make_dessert(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Chef1(Chef):
    """concrete builder 1"""

    def __init__(self):
        self.repas = Repas()

    def make_aperitif(self):
        self.repas.aperitif = "aperitif 1"

    def make_entree(self):
        self.repas.entree = "entree 1"

    def make_main_course(self):
        self.repas.main_course = "main_course 1"

    def make_dessert(self):
        self.repas.dessert = "dessert 1"


class Chef2(Chef):
    """concrete builder 2"""

    def __init__(self):
        self.repas = Repas()

    def make_aperitif(self):
        self.repas.aperitif = "aperitif 2"

    def make_entree(self):
        self.repas.entree = "entree 2"

    def make_main_course(self):
        self.repas.main_course = "main_course 2"

    def make_dessert(self):
        self.repas.dessert = "dessert 2"


class Waitor(object):
    """director: control the order of building"""

    def __init__(self, chef):
        self.chef = chef

    def prepare(self):
        self.chef.make_aperitif()
        self.chef.make_entree()
        self.chef.make_main_course()
        self.chef.make_dessert()
        return self.chef.repas


if __name__ == "__main__":
    # client 1:
    chef1 = Chef1()
    waitor1 = Waitor(chef1)
    print(waitor1.prepare())

    # client 2:
    chef2 = Chef2()
    waitor2 = Waitor(chef2)
    print(waitor2.prepare())
