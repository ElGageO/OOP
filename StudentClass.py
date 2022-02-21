import datetime

class Student:

    def __init__(self, student_id, name, dob, classification):
        self.__student_id = student_id
        self.__name = name
        self.__dob = dob
        self.__class = classification

    def calc_age(self, dob):
        self.__birth_year = int(dob[-4:])
        self.__age = 2022 - self.__birth_year
    
    def get_dob(self):
        return self.__dob

    def calc_registration_dates(self, classification):
        if classification == 'F':
            self.__reg_dates = '4/10 - 4/12'
        elif classification == 'S':
            self.__reg_dates = '4/7 - 4/9'
        elif classification == 'Jr':
            self.__reg_dates = '4/4 - 4/6'
        elif classification == 'Sr':
            self.__reg_dates = '4/1 - 4/3'
        else:
            self.__reg_dates = 'Error: Invalid classification'


    def get_class(self):
        return self.__class

    def get_student_info(self):
        return self.__reg_dates, self.__age
