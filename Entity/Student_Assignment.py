class Student_Assignment:
    def __init__(self, assignment_id, student_id):
        self.__assignment_id = assignment_id
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def get_assignment_id(self):
        return self.__assignment_id

    def __str__(self):
        return ('Assignment ID: ' + str(self.__assignment_id)).rjust(5) + (
                    '  Student ID: ' + str(self.__student_id)).rjust(10)
