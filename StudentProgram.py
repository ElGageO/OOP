import StudentClass as s

def main():
    my_student = s.Student('892542742', 'Gage Reynolds', '7/11/2001', 'Jr')
    
    classification = my_student.get_class()
    my_student.calc_registration_dates(classification)

    dob = my_student.get_dob()
    my_student.calc_age(dob)

    student_reg_dates, student_age = my_student.get_student_info()
    print('\nStudent age:', student_age)
    print('Registration dates:', student_reg_dates)
    print()

main()
