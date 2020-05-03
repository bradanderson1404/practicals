from prac_08.unreliablecar import UnreliableCar

def main():

    dodgy_car = UnreliableCar("Commodore SV6", 150, 85)
    print(dodgy_car)
    dodgy_car.drive(30)
    print(dodgy_car)
    dodgy_car.drive(30)
    print(dodgy_car)
    dodgy_car.drive(30)
    print(dodgy_car)
    dodgy_car.drive(30)
    print(dodgy_car)

main()