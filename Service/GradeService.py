from Service.UndoService import *


class Grade_Service:

    def __init__(self, grade_list, undo_service):
        """""
        :param self
        :param grade_list Dependency Injection;
        """
        self.__grade_list = grade_list
        self.__undo_service = undo_service

    def add_grade(self, grade):
        """""
        Adds a grade to the grade lists
        Also record the operations for undo/redo
        """
        self.__grade_list.add_grade(grade)
        undo_fun = FunctionCall(self.__grade_list.delete_single_grade, grade)
        redo_fun = FunctionCall(self.__grade_list.add_grade, grade)
        self.__undo_service.record(Operation(undo_fun, redo_fun))

    def delete_single_grade(self, grade):
        """""
        Deletes a specific grade for the assignments
        """
        self.__grade_list.delete_single_grade(grade)

    def delete_grade(self, id_assign):
        """""
        Deletes all grades related to an assignments
        """
        i = 0
        list = []
        grades = self.__grade_list.get_grades()
        while i <= len(grades) - 1:
            if int(grades[i].get_assignment_id()) == int(id_assign):
                list.append(grades[i])
            i += 1
        self.__grade_list.delete_grade(id_assign)
        operations = []
        for elem in list:
            undo_fun = FunctionCall(self.__grade_list.add_grade, elem)
            redo_fun = FunctionCall(self.__grade_list.delete_grade, elem.get_assignment_id())
            operations.append(Operation(undo_fun, redo_fun))
        return operations

    def delete_grade_student(self, id_student):
        """""
        Deletes all grades related to a student
        """
        i = 0
        list = []
        grades = self.__grade_list.get_grades()
        while i <= len(grades)-1:
            if int(grades[i].get_student_id()) == int(id_student):
                list.append(grades[i])
            i +=1
        self.__grade_list.delete_student_grade(id_student)
        operations = []
        for elem in list:
            undo_fun = FunctionCall(self.__grade_list.add_grade, elem)
            redo_fun = FunctionCall(self.__grade_list.delete_student_grade, elem.get_student_id())
            operations.append(Operation(undo_fun, redo_fun))
        return operations

    def get_grades(self):
        return self.__grade_list.get_grades()

    def get_len_grades_student(self, id_student):
        """""
        Returns the number of grades in the list
        """
        return self.__grade_list.get_len_grades_student(id_student)

    def exists(self, id_assignment, id_student):
        """""
        Checks whether or not the the grade exists in the grade list
        """
        return self.__grade_list.exists(id_assignment, id_student)

    def average_grade(self, id_assignment):
        """""
        Returns a list containing students who have a given assignment graded
        """
        grades = self.__grade_list.get_grades()
        result = []
        grade_dict = {}
        for grade in grades:
            if int(grade.get_assignment_id()) == int(id_assignment):
                if grade.get_student_id() not in grade_dict:
                    grade_dict[grade.get_student_id()] = 0
                grade_dict[grade.get_student_id()] = float(grade.get_grade_value())
        for entry in grade_dict:
            result.append(StudentGrade(entry, grade_dict[entry]))
        result.sort(key=lambda x: x.grade)
        return result

    def total_grade(self, id_student):
        """""
        Returns a decreasing-by-grade list of students who have all the assignments graded
        """
        sum = 0
        grades = self.__grade_list.get_grades()
        for grade in grades:
            if int(grade.get_student_id()) == int(id_student):
                sum += float(grade.get_grade_value())
        return float(sum / self.get_len_grades_student(id_student))

    def is_graded(self, id_assignment, id_student):
        """""
        Checks whether or not a given assignment of a given student is graded
        """""
        grades = self.__grade_list.get_grades()
        for grade in grades:
            if int(grade.get_student_id()) == int(id_student) and int(grade.get_assignment_id()) == int(id_assignment):
                return True
        return False


class StudentGrade:

    def __init__(self, student_id, grade):
        self._student_id = student_id
        self._grade = grade

    @property
    def student_id(self):
        return self._student_id

    @property
    def grade(self):
        return self._grade

    def __str__(self):
        return 'Student ID: ' + str(self._student_id) + ' ' + 'Grade: ' + str(self._grade)
