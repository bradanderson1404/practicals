from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}".format(super().__str__())

    def drive(self, distance):
        reliability_check = random.randint(0-100)
        if reliability_check >= self.reliability:
            distance_driven = 0
        else:
            distance_driven = super().drive(distance)
        return distance_driven
