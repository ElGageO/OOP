import InsectClass as insect

def main():
    housefly = insect.Insect(2,4)
    mosquito = insect.Insect(4,6)

    housefly.flight_length()
    print('\nThere is a housefly with', housefly.get_wings(), 'wings and', housefly.get_legs(), 'legs.')
    print('The housefly can fly', housefly.get_flight_length(), 'mile(s).')

    mosquito.flight_length()
    print('\nThere is a mosquito with', mosquito.get_wings(), 'wings and', mosquito.get_legs(), 'legs.')
    print('The mosquito can fly', mosquito.get_flight_length(), 'mile(s).\n')

main()
