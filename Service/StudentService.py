from Entity.Student import Student
from datetime import *
from Repositories.StudentRepo import StudRepoException
from Service.UndoService import Operation, FunctionCall, CascadedOperation


class Student_Service:

    def __init__(self, student_list, valid_student, undo_service):
        """""
        :param self
        :param student_list Dependency Injection;
        """
        self.__student_list = student_list
        self.__valid_student = valid_student
        self.__undo_service = undo_service

    def get_number_students(self):
        """""
        :param self
        return the number of elements in the book list
        """
        return len(self.__student_list)

    def add_student(self, student_id, name, group):
        """""
        :param self
        :param student_id ; given by the user
        :param name ; given by the user
        :param group ; given by the user
        Creates a Student class type variable and passes it to the add function
        """
        student = Student(student_id, name, group)
        self.__valid_student.validate(student)
        try:
            stud = self.__student_list.add_stud(student)
            undo_fun = FunctionCall(self.__student_list.remove_stud, student.get_student_id())
            redo_fun = FunctionCall(self.__student_list.add_stud, student)
            self.__undo_service.record(Operation(undo_fun, redo_fun))
        except StudRepoException:
            raise StudRepoException("The student already exists!")

    def remove_student(self, id_student):
        """""
        :param self
        :param id_student ; given by the user in the ui function
        Passes the parameter to the remove function
        """
        stud = 0
        students = self.__student_list.get_all()
        for student in students:
            if int(student.get_student_id()) == int(id_student):
                stud = student
        try:
            self.__student_list.remove_stud(id_student)
            undo_fun = FunctionCall(self.__student_list.add_stud, stud)
            redo_fun = FunctionCall(self.__student_list.remove, id_student)
            return Operation(undo_fun, redo_fun)

        except StudRepoException:
            raise StudRepoException("Student with the given id does not exist! No changes have been made")

    def modify_student(self, id_student, name, group):
        """""
        :param self
        :param id_student ; given by the user in the ui function
        :param name; given by the user in the ui function
        :param group; given by the user in the ui function
        """""
        try:
            student = self.__student_list.find_id(id_student)
        except StudRepoException:
            raise StudRepoException("There is no such student!")
        id_student2 = student.get_student_id()
        name2 = student.get_name()
        group2 = student.get_group()
        self.__student_list.update_student(id_student, name, group)
        undo_fun = FunctionCall(self.__student_list.update_student, id_student2, name2, group2)
        redo_fun = FunctionCall(self.__student_list.update_student, id_student, name, group)
        self.__undo_service.record(Operation(undo_fun, redo_fun))

    def give_assignment_student(self, id_student, assignment):
        """""
        Passes the given parameters to the Repo
        """
        try:
            self.__student_list.assign(id_student, assignment)
            undo_fun = FunctionCall(self.__student_list.remove_assign_student, id_student, assignment)
            redo_fun = FunctionCall(self.__student_list.assign, id_student, assignment)
            self.__undo_service.record(Operation(undo_fun, redo_fun))
        except StudRepoException as sre:
            raise StudRepoException(str(sre))

    def give_assignment_group(self, group, assignment):
        """""
        Passes the given parameters to the Repo
        """
        try:
            self.__student_list.assign2(group, assignment)
        except StudRepoException as sre:
            raise StudRepoException(str(sre))
        operations = []
        students = self.__student_list.get_all()
        for student in students:
            if student.get_group() == group:
                undo_fun = FunctionCall(self.__student_list.remove_assign_student, student.get_student_id(), assignment)
                redo_fun = FunctionCall(self.__student_list.assign, student.get_student_id(), assignment)
                operations.append(Operation(undo_fun, redo_fun))
        self.__undo_service.record(CascadedOperation(operations))

    def list_student_assignments(self, id_student):
        """""
        Passes the given parameters to the Repo
        """
        return self.__student_list.list_assignments(id_student)

    def list_student_grades(self, id_student):
        return self.__student_list.list_grades(id_student)

    def remove_assignment(self, id_assignment):
        """""
        Passes the given parameters to the Repo
        Will help in removing a non existing assignment from student's assignment list
        """
        operations = []
        assignments = self.__student_list.remove_assign(id_assignment)
        i = 0
        while i <= len(assignments) - 1:
            undo_fun = FunctionCall(self.__student_list.assign, assignments[i], assignments[i + 1])
            redo_fun = FunctionCall(self.__student_list.remove_assign_student, assignments[i], assignments[i + 1])
            operations.append(Operation(undo_fun, redo_fun))
            i = i + 2
        return operations

    def modify_assignment(self, id_assignment, description, deadline):
        """""
        Passes the given parameters to the Repo
        Will help in modifying the assignments from the student's assignment list accordingly
        """
        operations = []
        assignments = self.__student_list.modify_assign(id_assignment, description, deadline)
        i = 0
        while i + 3 <= len(assignments) - 1:
            undo_fun = FunctionCall(self.__student_list.modify_assign_student, assignments[i], assignments[i + 1],
                                    assignments[i + 2], assignments[i + 3])
            redo_fun = FunctionCall(self.__student_list.modify_assign, id_assignment, description, deadline)
            operations.append(Operation(undo_fun, redo_fun))
            i += 4
        return operations

    def give_grade(self, grade):
        """""
        Passes the newly formed Grade type variable to the Repo
        Will help in giving grades
        """
        try:
            self.__student_list.grade(grade)
            undo_fun = FunctionCall(self.__student_list.remove_grade_student, grade)
            redo_fun = FunctionCall(self.__student_list.grade, grade)
            self.__undo_service.record(Operation(undo_fun, redo_fun))
        except StudRepoException as sre:
            raise StudRepoException(str(sre))

    def remove_grade_a(self, id_assignment):
        """""
        Only called if the user removes an assignment
        Will pass the given parameter to the repo
        Will help in deleting the grades from deleted assignments
        """
        grade_list = self.__student_list.remove_grade(id_assignment)
        operations = []
        i = 0
        while i <= len(grade_list) - 1:
            undo_fun = FunctionCall(self.__student_list.grade, grade_list[i])
            redo_fun = FunctionCall(self.__student_list.remove_grade, grade_list[i].get_assignment_id())
            operations.append(Operation(undo_fun, redo_fun))
            i += 1
        return operations

    def get_students(self):
        """""
        :param self
        :return a list containing all the books
        """
        return self.__student_list.get_all()

    def order_by_grade_assignment(self, id_assignment):
        """""
        Orders students who have a given assignment by their grade
        Computes the value which is transformed in a StudentGrade type variable
        The result is put in the result list which is then sorted
        """
        result = []
        grade_dict = {}
        students = self.__student_list.get_all()
        for student in students:
            grades = student.get_grades()
            for grade in grades:
                if int(grade.get_assignment_id()) == int(id_assignment):
                    if student.get_student_id() not in grade_dict:
                        grade_dict[student.get_student_id()] = 0
                    grade_dict[student.get_student_id()] += float(grade.get_grade_value())
        for entry in grade_dict:
            result.append(StudentGrade(entry, grade_dict[entry]))
        result.sort(key=lambda x: x.grade)
        return result

    def order_by_grade_total(self):
        """""
        Orders students who have all assignments graded by their average grade on all assignments
        Computes the value which is transformed in a StudentGrade type variable
        The result is put in the result list which is then sorted
        """
        result = []
        grade_dict = {}
        students = self.__student_list.get_all()
        for student in students:
            if student.get_len_assignments() == student.get_len_grades() and student.get_len_assignments() > 0:
                grades = student.get_grades()
                assign_grade = 0
                for grade in grades:
                    assign_grade += float(grade.get_grade_value())
                if student.get_student_id() not in grade_dict:
                    grade_dict[student.get_student_id()] = 0
                grade_dict[student.get_student_id()] = assign_grade / (student.get_len_grades())
        for entry in grade_dict:
            result.append(StudentGrade(entry, grade_dict[entry]))
        result.sort(key=lambda x: x.grade, reverse=True)
        return result

    def late_assign(self):
        """""
        Orders students who have at least one late assignment
        Computes the value which is transformed in a LateStudent type variable
        The result is put in the result list which is then sorted
        """
        result = []
        student_dict = {}
        today = date.today()
        students = self.__student_list.get_all()
        for student in students:
            if int(student.get_len_assignments()) != int(student.get_len_grades()):
                assignments = student.get_assignments()
                grades = student.get_grades()
                for assignment in assignments:
                    if datetime.date(assignment.get_deadline()) < today:
                        graded = False
                        for grade in grades:
                            if int(assignment.get_assignment_id()) == int(grade.get_assignment_id()):
                                graded = True
                        if not graded:
                            result.append(student.get_student_id())
        for entry in student_dict:
            result.append(LateStudent(student_dict[entry]))
        result.sort()
        return result


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


class LateStudent:

    def __init__(self, student_id):
        self._student_id = student_id

    @property
    def student_id(self):
        return self.student_id

    def __str__(self):
        return 'Student ID: ' + str(self._student_id)
