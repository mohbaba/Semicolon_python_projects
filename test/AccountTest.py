import unittest

from Account.Account1 import *
from Account.exceptions.InvalidAmountException import InvalidAmountException


class MyTestCase(unittest.TestCase):

    def test_newly_created_account_has_zero_balance(self):
        account = Account("abike", "1234", 0)
        self.assertEqual(0, account.check_balance("1234"))

    def testAccountPinThrowsException_whenInvalidPinIsInputWhenCreatingAccount(self):
        account = Account("abike", "1234", 0)
        with self.assertRaises(InvalidPinException):
            account.check_balance("12ergshr")

    def testDepositNegativeAmount_ThrowsException(self):
        account = Account("abike", "1234", 0)
        with self.assertRaises(InvalidAmountException):
            account.deposit(-5000)
            account.check_balance("1234")

    def testDepositAmount_BalanceIncreases(self):
        account = Account("abike", "1234", 0)
        account.deposit(10_000)
        self.assertEqual(10_000, account.check_balance("1234"))

    def test_withdrawNegativeAmount_ThrowsExceptionTest(self):
        account = Account("abike", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(-5000, "1234")

    def test_withdrawMoreThanAccountBalance_ThrowsException(self):
        account = Account("abike", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InsufficientFundsException):
            account.withdraw(15000, "1234")

    def test_enterIncorrectPinUponWithdrawal_ThrowException(self):
        account = Account("abike", "1234", 0)
        account.deposit(10_000)
        with self.assertRaises(InvalidPinException):
            account.withdraw(5000, "1i34")


if __name__ == '__main__':
    unittest.main()
