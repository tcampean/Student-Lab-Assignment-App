from Entity.Student_Assignment import Student_Assignment
from copy import *
class StudentAssignRepoException(Exception):
    pass

class StudentAssignRepo:
    def __init__(self):
        self._student_assignments = []

    def exists(self,id_assignment,id_student):
        """""
        :param id_student
        :param id_assignment
        Checks if an assignments was already assigned to a given student
        Returns True if yes or False otherwise
        """
        for elem in self._student_assignments:
            if int(id_assignment) == int(elem.get_assignment_id()) and int(id_student) == int(elem.get_student_id()):
                return True
        return False

    def find(self,id_assignment,id_student):
        """""
        Returns a given assignment if it exists
        """
        for elem in self._student_assignments:
            if int(id_assignment) == int(elem.get_assignment_id()) and int(id_student) == int(elem.get_student_id()):
                return elem

    def give_assignment(self,id_assignment,id_student):
        """""
        Assigns an assignment to a student if it wasn't assigned yet
        """
        if not self.exists(id_assignment,id_student):
            self._student_assignments.append(Student_Assignment(id_assignment,id_student))

    def delete_single_assignment(self,id_assignment,id_student):
        """""
        Deletes a specific assignment from the given assignments list
        """
        assignment = self.find(id_assignment,id_student)
        self._student_assignments.remove(assignment)

    def remove_assignment(self,id_assignment):
        """""
        Removes all given assignments related to a specific assignments
        """
        operations = []
        i = 0
        while i <= len(self._student_assignments)-1:
            if int(self._student_assignments[i].get_assignment_id()) == int(id_assignment):
                operations.append(self._student_assignments[i])
                self._student_assignments.pop(i)
            else:
                i += 1
        return operations

    def remove_assignment_student(self,id_student):
        """""
        Removes all given assignments related to a student
        """
        i = 0
        operations = []
        while i <= len(self._student_assignments) - 1:
            if int(self._student_assignments[i].get_student_id())== int(id_student):
                operations.append(self._student_assignments[i])
                self._student_assignments.pop(i)
            else:
                i += 1

        return operations

    def get_student_assignments(self):
        return self._student_assignments

    def get_len_student_assignments(self,id_student):
        """""
        Returns the number of given assignments
        """
        c = 0
        for assignment in self._student_assignments:
            if int(assignment.get_student_id()) == int(id_student):
                c += 1
        return c

    def list_student_assignments(self,id_student):
        """""
        Returns a list of all the existing given assignments
        """
        assignments = []
        for assignment in self._student_assignments:
            if int(assignment.get_student_id()) == int(id_student):
                assignments.append(assignment.get_assignment_id())
        return assignments
