import sys

from BankApp.exceptions.InsufficientFundsException import InsufficientFundsException
from BankApp.exceptions.InvalidPinException import InvalidPinException
from BankApp.Bank import *

bank = Bank("Bank Moh")


def main_menu():
    try:
        print(f"""
                           Welcome To {bank.name}!
                           1-> Register Account
                           2-> Deposit
                           3-> Withdraw
                           4-> Transfer
                           5-> Check Balance
                           6-> Exit App
                           """);

        user_input = int(input("Select an option: "))
        match user_input:
            case 1:
                register_account()

            case 2:
                deposit()

            case 3:
                withdraw()

            case 4:
                transfer()

            case 5:
                check_balance()

            case 6:
                print(f"Thank you for banking with us at {bank.name}")
                sys.exit()

            case _:
                main_menu()
    except ValueError as e:
        print("You are mad")
        main_menu()





def register_account():
    try:
        first_name = input("Please enter your firstname: ")
        last_name = input("Please enter your lastname: ")
        pin = input("Please enter 4 character pin: ")
        account = bank.register_customer(first_name, last_name, pin)
        print("\n")
        print("*****Account Registered Successfully*****\n")
        print(f"Hello {first_name} {last_name} your account number is {account.get_account_number()}")
    except InvalidPinException as e:
        print(e)
    finally:
        main_menu()


def deposit():
    print("DEPOSIT MONEY\n")
    account_number = int(input("Enter Account Number to deposit into: "))
    amount = int(input("Enter amount you will like to deposit: "))
    try:
        bank.deposit(amount, account_number)
        print("***Amount deposited Successfully***\n")
    except InsufficientFundsException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except Exception as e:
        print(e)
    except NoAccountFoundException as e:
        print(e)
    finally:
        print("\n")
        main_menu()


def withdraw():
    print("WITHDRAW MONEY")
    amount = int(input("Enter Amount you'd like to withdraw: "))
    account_number = int(input("Enter your account number: "))
    pin = input("Enter 4 character pin: ")

    try:
        bank.withdraw(amount, account_number, pin)
        print(f"*****{amount} withdrawn Successfully!*****")
    except InsufficientFundsException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except NoAccountFoundException as e:
        print(e)
    finally:
        print("\n")
        main_menu()


def transfer():
    sender = int(input("Enter Account number of the sender: "))
    receiver = int(input("Enter Account number of receiver: "))
    amount = int(input("Enter amount to transfer: "))
    pin = input("Enter your pin: ")

    try:
        bank.transfer(sender, receiver, amount, pin)
        print(f"*****{amount} transferred successfully from {sender} to {receiver}*****")
    except InsufficientFundsException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except Exception as e:
        print(e)
    except NoAccountFoundException as e:
        print(e)
    finally:
        main_menu()


def check_balance():
    print("BALANCE")
    account_number = int(input("Enter Account Number: "))
    pin = input("Enter pin: ")

    try:
        balance = bank.check_balance(account_number, pin);
        print(f"Your Account balance is {balance}")
    except InsufficientFundsException as e:
        print(e)
    except InvalidPinException as e:
        print(e)
    except Exception as e:
        print(e)
    except NoAccountFoundException as e:
        print(e)
    finally:
        main_menu();


main_menu()
