from prac_08.taxi import Taxi

def main():
    my_taxi = Taxi("Prius1", 100, 1.23)

    my_taxi.drive(40)
    print(my_taxi)

main()