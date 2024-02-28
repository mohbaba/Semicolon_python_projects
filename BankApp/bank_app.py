import sys

from BankApp.exceptions.InvalidPinException import InvalidPinException
from BankApp.Bank import *

bank = Bank("Bank Moh")


def main_menu():
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

        case 6: (input("Enter Amount you'd like to withdraw: "))
    account_number = int(input("Enter your account number: "))
    pin = input("Enter 4 character pin")

    try:
        bank.withdraw(amount, account_number, pin)
        print(f"*****{amount} withdrawn Successfully!*****")
    except Exception as e:
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
    except Exception as e:
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
    except Exception as message:
        print(message);
    finally:
        main_menu();


main_menu()
