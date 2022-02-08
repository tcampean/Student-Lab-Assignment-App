from Service.UndoService import *


class StudentAssignmentService:

    def __init__(self, student_assign_list, undo_service):
        """""
        :param self
        :param student_assign_list Dependency Injection;
        """
        self.__student_assign_list = student_assign_list
        self.__undo_service = undo_service

    def give_assignment(self, id_assignment, id_student):
        """""
        Gives an assignment to a given student
        Records the operation for undo/redo
        """
        self.__student_assign_list.give_assignment(id_assignment, id_student)
        undo_fun = FunctionCall(self.__student_assign_list.delete_single_assignment, id_assignment, id_student)
        redo_fun = FunctionCall(self.__student_assign_list.give_assignment, id_assignment, id_student)
        self.__undo_service.record(Operation(undo_fun, redo_fun))

    def give_assignment_group(self, id_assignment, id_student):
        """""
        Gives an assignment to a whole group of students
        """
        self.__student_assign_list.give_assignment(id_assignment, id_student)
        undo_fun = FunctionCall(self.__student_assign_list.delete_single_assignment, id_assignment, id_student)
        redo_fun = FunctionCall(self.__student_assign_list.give_assignment, id_assignment, id_student)
        return Operation(undo_fun, redo_fun)

    def delete_single_assignment(self, id_assignment, id_student):
        """""
        Deletes a specific assignment from the list
        """
        self.__student_assign_list.delete_single_assignment(id_assignment, id_student)

    def delete_assignment(self, id_assignment):
        """""
        Deletes all given assignments related to an assignments
        """
        list = []
        assignments = self.__student_assign_list.get_student_assignments()
        i = 0
        while i <= len(assignments) - 1:
            if int(assignments[i].get_assignment_id()) == int(id_assignment):
                list.append(assignments[i])
            i += 1
        self.__student_assign_list.remove_assignment(id_assignment)
        operations = []
        for elem in list:
            undo_fun = FunctionCall(self.__student_assign_list.give_assignment, elem.get_assignment_id(),
                                    elem.get_student_id())
            redo_fun = FunctionCall(self.__student_assign_list.remove_assignment, elem.get_assignment_id())
            operations.append(Operation(undo_fun, redo_fun))
        return operations

    def delete_student_assignment(self, id_student):
        """""
        Deletes all given assignments related to a student
        """
        list = []
        assignments = self.__student_assign_list.get_student_assignments()
        i = 0
        while i <= len(assignments) - 1:
            if int(assignments[i].get_student_id())== int(id_student):
                list.append(assignments[i])
            i +=1
        self.__student_assign_list.remove_assignment_student(id_student)
        operations = []
        for elem in list:
            undo_fun = FunctionCall(self.__student_assign_list.give_assignment, elem.get_assignment_id(),
                                    elem.get_student_id())
            redo_fun = FunctionCall(self.__student_assign_list.remove_assignment_student, elem.get_student_id())
            operations.append(Operation(undo_fun, redo_fun))
        return operations

    def get_student_assignment(self):
        return self.__student_assign_list.get_student_assignments()

    def exists(self, id_assignment, id_student):
        """""
        Checks if the given assignment is already in the list
        """
        return self.__student_assign_list.exists(id_assignment, id_student)

    def list_student_assignments(self, id_student):
        """""
        Returns the list of all given assignments
        """

        return self.__student_assign_list.list_student_assignments(id_student)

    def get_len_student_assignments(self, id_student):
        """""
        Returns the number of given assignments
        """
        return self.__student_assign_list.get_len_student_assignments(id_student)
