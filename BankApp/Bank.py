from BankApp.Account1 import Account
from BankApp.exceptions.NoAccountFoundException import NoAccountFoundException


class Bank:
    accounts = []

    def __init__(self, name):
        self.name = name

    def deposit(self, amount, account_number):
        account = self.find_account(account_number)
        account.deposit(amount)

    def find_account(self,account_number):
        for account in self.accounts:
            if account.get_account_number == account_number:
                return account
        raise NoAccountFoundException("Account cannot be found")

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.check_balance(pin)
