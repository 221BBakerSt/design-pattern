"""
Proxy pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def get_content(self):
        raise NotImplementedError(NOT_IMPLEMENTED)

    @abstractmethod
    def set_content(self, content):
        raise NotImplementedError(NOT_IMPLEMENTED)


class RealSubject(Subject):
    def __init__(self, filename):
        self.filename = filename

    def get_content(self):
        with open(self.filename, "r", encoding="utf-8") as f:
            self.content = f.read()
        return self.content

    def set_content(self, content):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(content)


class VirtualProxy(Subject):
    def __init__(self, filename):
        self.filename = filename
        self.proxyStateOn = True

    def get_content(self):
        if self.proxyStateOn:
            virtualSubject = RealSubject(self.filename)
            return virtualSubject.get_content()
        return "Please turn proxy on!"

    def set_content(self, content):
        if self.proxyStateOn:
            virtualSubject = RealSubject(self.filename)
            return virtualSubject.set_content(content)
        return "Please turn proxy on!"


class ProtectedSubject(Subject):
    def __init__(self, filename):
        self.virtualSubject = RealSubject(filename)

    def get_content(self):
        return self.virtualSubject.get_content()

    def set_content(self, content):
        raise PermissionError("No write permission!")


subj = RealSubject("/Users/admin/Desktop/test.txt")
print(subj.get_content())

subj = VirtualProxy("/Users/admin/Desktop/test.txt")
print(subj.get_content())
subj.set_content("abc")
print(subj.get_content())

subj = ProtectedSubject("/Users/admin/Desktop/test.txt")
print(subj.get_content())
# subj.set_content('abc')
