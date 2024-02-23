from Account.exceptions.InsufficientFundsException import InsufficientFundsException
from Account.exceptions.InvalidAmountException import InvalidAmountException
from Account.exceptions.InvalidPinException import InvalidPinException


class Account:
    def __init__(self, name, pin, account_number):
        self.name = name
        self.pin = pin
        self.balance = 0
        self.accountNumber = account_number

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

    def withdraw(self, amount, pin):
        self.validate_pin(pin)
        if amount < 0 or amount > self.balance:
            raise InsufficientFundsException("Insufficient Funds")
        self.balance -= amount


