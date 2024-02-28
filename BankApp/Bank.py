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
            if account.get_account_number() == account_number:
                return account
        raise NoAccountFoundException("Account cannot be found")

    def check_balance(self, account_number, pin):
        account = self.find_account(account_number)
        return account.check_balance(pin)

    def register_customer(self, first_name, last_name, pin):
        name = first_name +" "+ last_name
        account = Account(name,pin,self.generate_account_number())
        self.accounts.append(account)
        return account

    def generate_account_number(self):
        return len(self.accounts) + 1000

    def withdraw(self, amount, account_number, pin):
        account = self.find_account(account_number)
        account.withdraw(amount,pin)

    def transfer(self, sender_account_number, receiver_account_number, amount, pin):
        self.withdraw(amount,sender_account_number,pin)
        self.deposit(amount,receiver_account_number)

    def remove(self, account_number, pin):
        account = self.find_account(account_number)
        self.accounts.remove(account)

    def number_of_customers(self):
        return len(self.accounts)


