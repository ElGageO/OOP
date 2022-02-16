import random

class Insect:

    def __init__(self):
        self.wings = 2
        self.legs = 4

    def flight_length(self):
        self.length = random.randint(1, 10)

    def get_flight_length(self):
            return self.length

    def get_wings(self):
            return self.wings
    
    def get_legs(self):
            return self.legs
