from prac_08.taxi import Taxi
from prac_08.silverservicetaxi import SilverServiceTaxi

TAXI_MENU = """Please select a Taxi to ride in:
 1. Prius
 2. Limo
 3. Hummer
...   """
VALID_SELECTIONS = ["PRIUS", "LIMO", "HUMMER"]


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 100, 4)]


main()