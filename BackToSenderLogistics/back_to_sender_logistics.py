class Logistics:

    def pay(self, number_of_parcels):
        if number_of_parcels > 100:
            return (100 * self.get_amount_of_parcels(100)) + 5000
        if number_of_parcels < 0:
            return 0
        return (number_of_parcels * self.get_amount_of_parcels(number_of_parcels)) + 5000

    def get_amount_of_parcels(self, percentage):
        if percentage < 0:
            return 0
        if percentage < 50:
            return 160
        elif percentage <= 59:
            return 200
        elif percentage <= 69:
            return 250
        else:
            return 500

    def calculate_percentage(self, number_of_parcels):
        return (number_of_parcels / 100) * 100