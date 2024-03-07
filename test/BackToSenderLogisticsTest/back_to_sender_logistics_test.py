import unittest
from BackToSenderLogistics.back_to_sender_logistics import Logistics


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.logistics = Logistics()

    def testThatRiderWillBePaidAfter80SuccessfullyDeliveredPackages(self):
        numbers_of_delivered_parcels = 80
        self.assertEqual(45_000, self.logistics.pay(numbers_of_delivered_parcels))

    def testThatRiderWillBePaidAfter25SuccessfullyDeliveredPackages(self):
        self.assertEqual(9000,self.logistics.pay(25))

    def testThatRiderWillBePaidAfter55SuccessfullyDeliveredPackages(self):
        self.assertEqual(16_000,self.logistics.pay(55))

    def testThatRiderWillBePaidAfter65SuccessfullyDeliveredPackages(self):
        self.assertEqual(21_250, self.logistics.pay(65))

    def testThatFunctionReturnsZeroWhenNumberOfParcelsIsNegative(self):
        self.assertEqual(0, self.logistics.pay(-65))

    def testThatFunctionRaisesExceptionWhenNumberOfParcelsIsMoreThanRequiredAmount(self):
        with self.assertRaises(ValueError):
            self.logistics.pay(150)



if __name__ == '__main__':
    unittest.main()
