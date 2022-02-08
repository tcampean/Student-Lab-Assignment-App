class Grade:

    def __init__(self, student_id, assignment_id, grade_value):
        self.__assignment_id = str(assignment_id)
        self.__student_id = str(student_id)
        self.__grade_value = float(grade_value)

    def get_assignment_id(self):
        return self.__assignment_id

    def get_student_id(self):
        return self.__student_id

    def get_grade_value(self):
        return self.__grade_value

    def __str__(self):
        return ('Student ID: '+str(self.__student_id)).rjust(5)+('  Assignment ID: ' +str(self.__assignment_id)).rjust(10)+('    Grade: '+ str(self.__grade_value)).rjust(20)

    def __eq__(self, other):
        return self.__student_id == other.__student_id and self.__assignment_id == other.__assignment_id