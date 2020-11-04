"""
Adapter pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."


class Payment(metaclass=ABCMeta):
    """
    An interface is a set of various abstract classes but hides internal implementation.
    Payment is an interface.
    """

    @abstractmethod
    def pay(self, money):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Alipay(Payment):
    """Alipay implements Payment interface"""

    # must override the abstract method in parent class, otherwise can't instantiate
    def pay(self, money):
        print(f"Alipay: ¥{money}")


class Wechatpay(object):
    """Suppose it's from another system"""

    def cost(self, money):
        print(f"Wechatpay: ¥{money}")

############### class adapter ################
class NewWechatpay(Payment, Wechatpay):
    """class adapter: multi-inheritance"""

    def pay(self, money):
        # must override pay method, because inherit from Payment
        self.cost(money)
        # instantiate Wechatpay and call its cost method
        # Wechatpay().cost(money)


p = Alipay()
p.pay(100)
p = NewWechatpay()
p.pay(100)


############### object adapter ################
class PaymentAdapter(Payment):
    """object adapter"""

    def __init__(self, payment):
        # 接收adaptee创建的对象
        self.payment = payment

    def pay(self, money):
        # 调用adaptee里面的对应方法，然后封装在与新接口匹配的方法里
        self.payment.cost(money)


p = Alipay()
p.pay(100)
p = PaymentAdapter(Wechatpay())
p.pay(100)
print("----------------------------\n")


# """
# Adapter pattern example.
# """
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

RECHARGE = ["Recharge started.", "Recharge finished."]

POWER_ADAPTERS = {"Android": "TypeC", "iPhone": "Lightning"}

CONNECTED = "{} connected."
CONNECT_FIRST = "Connect {} first."


class RechargeTemplate:
    __metaclass__ = ABCMeta

    @abstractmethod
    def recharge(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatIPhone(RechargeTemplate):
    @abstractmethod
    def use_lightning(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatAndroid(RechargeTemplate):
    @abstractmethod
    def use_type_c(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class IPhone(FormatIPhone):
    __name__ = "iPhone"

    def __init__(self):
        self.connector = False

    def use_lightning(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class Android(FormatAndroid):
    __name__ = "Android"

    def __init__(self):
        self.connector = False

    def use_type_c(self):
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self):
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class IPhoneAdapter(FormatAndroid):
    def __init__(self, mobile):
        self.mobile = mobile

    def recharge(self):
        self.mobile.recharge()

    def use_type_c(self):
        print(CONNECTED.format(POWER_ADAPTERS["Android"]))
        self.mobile.use_lightning()


class AndroidRecharger(object):
    def __init__(self):
        self.phone = Android()
        self.phone.use_type_c()
        self.phone.recharge()


class IPhoneTypeCRecharger(object):
    def __init__(self):
        self.phone = IPhone()
        self.phone_adapter = IPhoneAdapter(self.phone)
        self.phone_adapter.use_type_c()
        self.phone_adapter.recharge()


class IPhoneRecharger(object):
    def __init__(self):
        self.phone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()


print("Recharging Android with TypeC recharger.")
AndroidRecharger()
print()

print("Recharging iPhone with TypeC using adapter pattern.")
IPhoneTypeCRecharger()
print()

print("Recharging iPhone with Lightning recharger.")
IPhoneRecharger()
