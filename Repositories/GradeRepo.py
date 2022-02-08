class GradeRepoException(Exception):
    pass


class GradeRepo:
    def __init__(self):
        self._grade_list = []

    def exists(self, id_assignment, id_student):
        """""
        :param id_assignment
        :param id_student
        Checks whether or not a grade exists in the grade list
        :returns True if it exists or False otherwise
        """""
        for elem in self._grade_list:
            if int(elem.get_student_id()) == int(id_student) and int(elem.get_assignment_id()) == int(id_assignment):
                return True
        return False

    def add_grade(self, grade):
        """""
        :param grade
        Grades the assignments if it's not already graded
        """
        if self.exists(grade.get_assignment_id(), grade.get_student_id()):
            raise GradeRepoException("The assignment is already graded!")
        self._grade_list.append(grade)

    def delete_single_grade(self, grade):
        """""
        :param
        Removes a single grade from the grade list
        """""
        self._grade_list.remove(grade)

    def delete_grade(self, id_assignment):
        """""
        :param id_assignment
        Removes all the grades related to an assignment
        """
        i = 0
        operations = []
        while i <= len(self._grade_list) - 1:
            if int(self._grade_list[i].get_assignment_id()) == int(id_assignment):
                operations.append(self._grade_list[i])
                self._grade_list.pop(i)
            else:
                i += 1
        return operations

    def delete_student_grade(self, id_student):
        """""
        :param id_student
        Removes all grades related to a student
        """
        i = 0
        operations = []
        while i <= len(self._grade_list) - 1:
            if int(self._grade_list[i].get_student_id()) == int(id_student):
                operations.append(self._grade_list[i])
                self._grade_list.pop(i)
            else:
                i += 1
        return operations

    def get_grades(self):
        return self._grade_list

    def get_len_grades_student(self, id_student):
        """""
        :param id_student
        Returns the number of grades in the repo
        """
        c = 0
        for grade in self._grade_list:
            if int(grade.get_student_id()) == int(id_student):
                c += 1
        return c
