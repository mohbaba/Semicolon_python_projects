from decimal import Decimal


class Account:
    def __init__(self, name, balance: Decimal):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self,balance):
        if balance < Decimal(0.0) :
            raise ValueError("Invalid amount")
        self._balance = balance

    def __str__(self):
        return f"Account Name: {self.name} "
