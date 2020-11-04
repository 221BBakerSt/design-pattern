# Method 1:
class Married(object):
    # this class attribute is to judge if any instance has been created,
    # and also to store the reference of the instance object if there is one
    __class_attribute = False
    __instance_attribute = False

    def __new__(cls, *args, **kwargs):
        """check if the class has been initialised"""
        if not cls.__class_attribute:
            cls.__class_attribute = super().__new__(cls)
            # super() can be replaced with object:
            # cls.__class_attribute = object.__new__(cls)
        # no matter it had this class attribute or not, return the reference of this instance object,
        # so every time it creates the same instance
        return cls.__class_attribute

    def __init__(self, name):
        """check if the instance has been initialised"""
        if not self.__instance_attribute:
            self.__instance_attribute = True
            self.name = name
        else:
            print(f"Sorry {name}, I have {self.name}")

    def show_my_wife(self):
        print(f"My wife is {self.name}")


girl1 = Married("Ann")
girl1.show_my_wife()
girl2 = Married("Amy")
girl2.show_my_wife()
# it means they both point to the same block of memory,
print(girl2 is girl1)
# and it failed to create instance girl2
print(girl2 == girl1)

print("---------use hasattr:----------")

# Method 2:
class Singleton(object):
    def __new__(cls, *args):
        # if there is no class attribute cls_attr
        if not hasattr(cls, "cls_attr"):
            # call __new__ method from superclass to create this class attribute.
            # this class attribute cls_attr stores the reference of this instance object
            cls.cls_attr = super().__new__(cls)
        # no matter it had this class attribute or not, return the reference of this instance object,
        # so every time it creates the same instance
        return cls.cls_attr

    def __init__(self, name):
        #if there is no instance attribute instance_attr
        if not hasattr(self, "instance_attr"):
            self.name = name
        # set instance_attr to True so next time a new name won't be accepted
        self.instance_attr = True

    def __str__(self):
        return f"My wife is {self.name}"

girl1 = Singleton("Ann")
print(girl1)

girl2 = Singleton("Amy")
print(girl2)

# it proves they are the same instance stored in the same block of memory
print(girl1 is girl2)

print("--------use decorator:---------")

# Method 3:
def singletonDecorator(cls, *args, **kwargs):
    # this is a closure
    
    instance = {}

    def wrap_singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrap_singleton

@singletonDecorator
class Married(object):
    def __init__(self, girl):
        self.__name = girl

    def __str__(self):
        return f"My wife is {self.__name}"


girl1 = Married("Ann")
print(girl1)
girl2 = Married("Amy")
print(girl2)
print(girl1 is girl2)


# result:
# My wife is Ann
# Sorry Amy, I have Ann
# My wife is Ann
# True
# True
# ---------use hasattr:----------
# My wife is Ann
# My wife is Ann
# True
# --------use decorator:---------
# My wife is Ann
# My wife is Ann
# True