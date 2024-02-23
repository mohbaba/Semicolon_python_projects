from Account.exceptions.InvalidAmountException import InvalidAmountException
from Account.exceptions.InvalidPinException import InvalidPinException


class Account:
    def __init__(self ,name, pin, accountNumber):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.accountNumber = accountNumber

    def validate_pin(self, pin):
        if self.pin != pin:
            raise InvalidPinException

    def check_balance(self, pin):
        self.validate_pin(pin)
        return self.balance

    def deposit(self, amount):
        if amount < 0:
            raise InvalidAmountException("Cannot deposit negative amount")
        self.balance += amount


