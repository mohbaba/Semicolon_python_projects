import unittest

from BankApp.Bank import Bank
from BankApp.exceptions.InsufficientFundsException import InsufficientFundsException
from BankApp.exceptions.InvalidAmountException import InvalidAmountException
from BankApp.exceptions.InvalidPinException import InvalidPinException
from BankApp.exceptions.NoAccountFoundException import NoAccountFoundException


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("mohBank")

    def tearDown(self):
        self.bank.accounts.clear()

    def testBankCanDepositIntoCustomersAccount(self):
        account = self.bank.register_customer("Moh", "baba", "1234")
        self.bank.deposit(2_000, 1000)
        self.assertEqual(2_000, self.bank.check_balance(1000, "1234"))

    def testBankCanWithdrawFromCustomersAccount(self):
        self.bank.register_customer("Moh","baba","1234")

        self.bank.deposit(10_000,1000)
        self.bank.withdraw(5000,1000,"1234")
        self.assertEqual(5000,self.bank.check_balance(1000,"1234"))

    def testDepositNegativeAmount_ThrowExceptionTest(self):
        self.bank.register_customer("Moh","baba","1234")
        with self.assertRaises(InvalidAmountException):
            self.bank.deposit(-2000,1000)

    def testWithdrawNegativeAmount_ThrowExceptionTest(self):
        self.bank.register_customer("Moh","baba","1234")
        with self.assertRaises(InsufficientFundsException):
            self.bank.withdraw(-2000,1000,"1234")

    def testWithdrawAmountWithIncorrectPin_ThrowExceptionTest(self):
        self.bank.register_customer("Moh","baba","1234")
        with self.assertRaises(InvalidPinException):
            self.bank.withdraw(-2000,1000,"1274")

    def testTransferMoneyFromAccountToAccount(self):
        self.bank.register_customer("Moh","baba","1234")
        self.bank.deposit(5000,1000)
        self.bank.register_customer("First","last","5678")
        self.bank.transfer(1000,1001,2000,"1234")
        self.assertEqual(2000,self.bank.check_balance(1001,"5678"))

    def testTransferNegativeMoneyFromAccountToAccount(self):
        self.bank.register_customer("Moh", "baba", "1234")
        self.bank.deposit(5000, 1000)
        self.bank.register_customer("First", "last", "5678")
        with self.assertRaises(InsufficientFundsException):
            self.bank.transfer(1000, 1001, -2000, "1234")

    def testRemoveAccountFromListOfAccountsTest(self):
        self.bank.register_customer("Moh", "baba", "1234")
        self.bank.register_customer("First", "last", "5678")
        self.bank.remove(1000,"1234")
        self.assertEqual(1,self.bank.number_of_customers())

    def testFindAccountReturnsAccount(self):
        self.bank.register_customer("First", "last", "5678")
        self.assertIsNotNone(self.bank.find_account(1000))

    def testFindUnexistingAccount_RaiseException(self):
        self.bank.register_customer("First", "last", "5678")
        with self.assertRaises(NoAccountFoundException):
            self.bank.find_account(32232)

    def testDepositIntoAnAccountThatDoesntExist_ThrowsAccountNotFoundError(self):
        self.bank.register_customer("First", "last", "5678")
        with self.assertRaises(NoAccountFoundException):
            self.bank.deposit(29292,32232)

    def testWithdrawFromAnAccountThatDoesntExist_ThrowsAccountNotFoundError(self):
        with self.assertRaises(NoAccountFoundException):
            self.bank.withdraw(29292,32232,"1234")

    def testRemoveAccount_TestIfAccountStillExistsAfterRemoving(self):
        self.bank.register_customer("Moh", "baba", "1234")
        self.bank.register_customer("First", "last", "5678")
        self.bank.remove(1001,"5678")
        with self.assertRaises(NoAccountFoundException):
            self.bank.withdraw(29292,1001,"5678")













if __name__ == '__main__':
    unittest.main()
