import unittest

from BankApp.Bank import Bank


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.bank = Bank("mohBank")

    def testBankCanDepositIntoCustomersAccount(self):
        self.bank.deposit(2_000, 0)
        self.assertEqual(2_000, self.bank.check_balance(0, "1234"))


if __name__ == '__main__':
    unittest.main()
