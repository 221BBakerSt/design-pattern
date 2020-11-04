"""
Composite pattern example.
"""

# sub-system
class CPU(object):
    def run(self):
        print("CPU starts...")

    def stop(self):
        print("CPU stops...")


# sub-system
class SolidStateDrive(object):
    def run(self):
        print("Disk starts...")

    def stop(self):
        print("Disk stops...")


# sub-system
class Memory(object):
    def run(self):
        print("Memory starts...")

    def stop(self):
        print("Memory stops...")


# facade
class Computer(object):
    def __init__(self):
        self.cpu = CPU()
        self.disk = SolidStateDrive()
        self.mem = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.mem.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.mem.stop()


if __name__ == "__main__":
    # client
    c = Computer()
    c.run()
    c.stop()
