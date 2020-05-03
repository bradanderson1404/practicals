from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall_fee = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        return "{} plus flagall of ${:.2f}".format(super().__str__(), self.flagfall_fee)

    def get_fare(self):
        return self.flagfall_fee + super().get_fare()
