import InsectClass as insect

def main():
    my_insect = insect.Insect()

    my_insect.flight_length()
    print('There is an insect with', my_insect.get_wings(), 'wings and', my_insect.get_legs(), 'legs.')
    print('The insect can fly', my_insect.get_flight_length(), 'mile(s).')

main()
