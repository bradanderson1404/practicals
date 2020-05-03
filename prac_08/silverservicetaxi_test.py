from prac_08.silverservicetaxi import SilverServiceTaxi

def main():
    ss_taxi = SilverServiceTaxi("Hummer", 100, 2)
    ss_taxi.drive(18)
    fare = ss_taxi.get_fare()
    print(fare)
    print(ss_taxi)

main()
