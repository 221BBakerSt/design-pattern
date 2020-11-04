"""
Strategy pattern example.
"""
from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

# abstract strategy
class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError(NOT_IMPLEMENTED)


# concrete strategy
class SendByEmail(Strategy):
    def execute(self, data):
        print(data, "sent by email.")


# concrete strategy
class SendBySMS(Strategy):
    def execute(self, data):
        print(data, "sent by SMS.")


# context
class Context:
    def __init__(self, strategy, data):
        self.data = data
        self.strategy = strategy

    def take_strategy(self):
        self.strategy.execute(self.data)


data = "Hello"

email_method = SendByEmail()
context = Context(email_method, data)
context.take_strategy()

sms_method = SendBySMS()
context = Context(sms_method, data)
context.take_strategy()
