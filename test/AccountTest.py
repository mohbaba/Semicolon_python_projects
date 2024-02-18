import unittest
from decimal import Decimal

from Account.Account import Account


class MyTestCase(unittest.TestCase):
    def test_Account_creation(self):
        account:Account = Account("Mohbaba",Decimal(0.00))



if __name__ == '__main__':
    unittest.main()
