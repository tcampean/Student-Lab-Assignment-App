class StudException(Exception):
    pass

class StudentValidator:

    def validate(self, student):
        errors = ""
        ok = 1
        try:
            a = int(student.get_student_id())
        except ValueError:
            errors += "Student's ID must contain only numbers!\n"
            ok = 0
        if ok == 1:
            a = int(student.get_student_id())
            if a < 0:
                errors += "Student's ID must be positive"
        if len(student.get_name()) < 3:
            errors += "Student's name must be longer!\n"
        if student.get_group() == '':
            errors += "Invalid group!\n"
        if len(errors) > 0:
            raise StudException(errors)


class Student:

    def __init__(self, student_id, name, group):
        self.__student_id = student_id
        self.__name = str(name)
        self.__group = str(group)

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def set_name(self, name):
        self.__name = name

    def set_group(self, group):
        self.__group = group

    def __str__(self):
        return ('Student ID: ' + str(self.__student_id)).rjust(5) + ('  Name: ' + str(self.__name)).rjust(10) + (
                    '    Group: ' + str(self.__group)).rjust(15)

    def __eq__(self, other):
        return self.__student_id == other.__student_id
