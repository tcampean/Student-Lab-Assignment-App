from Entity.Assignment import Assignment


class StudRepoException(Exception):
    pass


class StudentRepo:
    def __init__(self):
        self._student_list = []

    def list_student_list(self):
        """""
        Returns the list of all students
        """
        return self._student_list

    def add_stud(self, student):
        """""
        Checks if a student with the same id is already in the list
        Appends the student formed by the user input
        """
        for stud in self._student_list:
            if int(student.get_student_id()) == int(stud.get_student_id()):
                raise StudRepoException("The student already exists!")

        self._student_list.append(student)
        return student

    def update_student(self, id_student, name, group):
        """""
        Updates the student with the given parameters
        Raises an error if the student is not found
        """
        done = False
        for student in self._student_list:
            if student.get_student_id() == str(id_student):
                if name != '':
                    student.set_name(name)
                if group != '':
                    student.set_group(group)
                done = True
        if not done:
            raise StudRepoException("Student with the given id does not exist!")

    def remove_stud(self, id_student):
        """""
        Removes a student from the list
        Raises an error if the student hasn't been found
        """
        for student in self._student_list:
            if int(student.get_student_id()) == int(id_student):
                stud = student
                self._student_list.remove(student)
                return stud
        raise StudRepoException("Student with the given id does not exist! No changes have been made")


    def find_id(self, id_stud):
        """""
        Checks if the student with the given id exists and returns it
        """

        for student in self._student_list:
            if student.get_student_id() == id_stud:
                return student
        raise StudRepoException("There is no such student!")

    def remove(self, id_student):
        """""
        Removes a student from the list
        Raises an error if the student hasn't been found
        """
        for student in self._student_list:
            if student.get_student_id() == str(id_student):
                stud = student
                self._student_list.remove(student)
                return stud
        raise StudRepoException("Student with the given id does not exist! No changes have been made")

    def get_all(self):
        """""
        Returns the list of all students
        """
        return self._student_list


    def __len__(self):
        return len(self._student_list)
