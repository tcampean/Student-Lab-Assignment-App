from Entity.Student import *
from Entity.Assignment import *
from Entity.Grade import *
from Entity.Student_Assignment import *
from Repositories.StudentRepo import *
from Repositories.AssignmentRepo import *
from Repositories.GradeRepo import *
from Repositories.StudentAssignRepo import *
from datetime import datetime
from random import randint, choice
from Service.GradeService import StudentGrade
from Service.UndoService import UndoService, CascadedOperation
from datetime import *


class ui:

    def __init__(self, service_student, service_assignment, service_student_assignment, service_grade, undo_service):
        self.__student_list = service_student
        self.__assignments_list = service_assignment
        self.__student_assign_list = service_student_assignment
        self.__grade_list = service_grade
        self.__undo_service = undo_service
        self.__commands = {'1': self.student_menu_ui, '2': self.assignment_menu_ui, '3': self.grading_menu_ui,
                           '4': self.statistics,
                           '5': self.undo, '6': self.redo}

    def undo(self):
        if self.__undo_service.undo() == False:
            print("There is nothing to undo!")
        else:
            print("The previous operation was undone!")

    def redo(self):
        if self.__undo_service.redo() == False:
            print("There is nothing to redo!")
        else:
            print("The previous operation was redone!")

    def stat1(self):
        id_assignment = input("Enter ID : ")
        try:
            id_assignment = int(id_assignment)
        except ValueError:
            print("The ID must be an integer!")
            return
        done = False
        assignments = self.__assignments_list.get_assignments()
        for assignment in assignments:
            if int(assignment.get_assignment_id()) == int(id_assignment):
                done = True
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist!")
        result = self.__grade_list.average_grade(id_assignment)
        if result == []:
            print("No students!")
            return
        for entry in result:
            print(entry)

    def stat2(self):
        students = self.__student_list.get_students()
        result = []
        grade_dict = {}
        for student in students:
            if self.__grade_list.get_len_grades_student(
                    student.get_student_id()) == self.__student_assign_list.get_len_student_assignments(
                    student.get_student_id()) and self.__grade_list.get_len_grades_student(
                    student.get_student_id()) != 0:
                if student.get_student_id() not in grade_dict:
                    grade_dict[student.get_student_id()] = 0
                grade_dict[student.get_student_id()] = self.__grade_list.total_grade(student.get_student_id())
        for entry in grade_dict:
            result.append(StudentGrade(entry, grade_dict[entry]))
        result.sort(key=lambda x: x.grade, reverse=True)
        if result == []:
            print("No students!")
        else:
            for elem in result:
                print(elem)

    def stat3(self):
        students = self.__student_list.get_students()
        result = []
        grade_dict = {}
        today = date.today()

        for student in students:
            marked = False
            if self.__grade_list.get_len_grades_student(
                    student.get_student_id()) != self.__student_assign_list.get_len_student_assignments(
                    student.get_student_id()):
                student_assignments = self.__student_assign_list.get_student_assignment()
                for stud_assign in student_assignments:
                    if int(stud_assign.get_student_id()) == int(student.get_student_id()):
                        if not self.__grade_list.is_graded(stud_assign.get_assignment_id(),
                                                           stud_assign.get_student_id()):
                            assignments = self.__assignments_list.get_assignments()
                            for assignment in assignments:
                                if int(assignment.get_assignment_id()) == int(stud_assign.get_assignment_id()):
                                    if datetime.date(assignment.get_deadline()) < today:
                                        result.append(student.get_student_id())
                                        marked = True
                                        break
                    if marked:
                        break
        if result == []:
            print("No students!")
            return
        for entry in result:
            print("Student ID: " + str(entry))

    def print_menu(self):
        print('1: Student Menu')
        print('2: Assignment Menu')
        print('3: Grading Menu')
        print('4: Statistics')
        print('5: Undo')
        print('6: Redo')
        print('0: Exit')

    def student_menu_ui(self):
        print('     1: Add a Student')
        print('     2: List all Students')
        print('     3: Remove a student')
        print('     4: Modify a student')
        print("     5: List student's assignments")
        print('     6: Give assignments')
        command = input('Enter command: ')
        if command == '1':
            self.__add_student_ui()
        elif command == '2':
            self.list_students_ui()
        elif command == '3':
            self.remove_student_ui()
        elif command == '4':
            self.modify_student_ui()
        elif command == '5':
            self.list_student_assignments_ui()
        elif command == '6':
            self.give_assignments_ui()
        else:
            print('Invalid command!')

    def assignment_menu_ui(self):
        print('     1: Add an Assignment')
        print('     2: List all Assignments')
        print('     3: Remove an assignment')
        print('     4: Modify an assignment')
        command = input('Enter command: ')
        if command == '1':
            self.add_assignments_ui()
        elif command == '2':
            self.list_assignments_ui()
        elif command == '3':
            self.remove_assignment_ui()
        elif command == '4':
            self.modify_assignment_ui()
        else:
            print('Invalid command!')

    def grading_menu_ui(self):
        print('     1: Give a grade to a student')
        print('     2: List the grades of a student')
        command = input('Enter command: ')
        if command == '1':
            self.grade_assignment_ui()
        elif command == '2':
            self.list_student_grades_ui()
        else:
            print('Invalid command!')

    def statistics(self):
        print('     1: List students with a graded given assignment')
        print('     2: List students with the best school situation')
        print('     3: List students who are late with assignments')
        command = input('Enter command: ')
        if command == '1':
            self.stat1()
        elif command == '2':
            self.stat2()
        elif command == '3':
            self.stat3()
        else:
            print('Invalid command!')

    def __add_student_ui(self):
        """""
        :param self
        Takes the input from the user and checks it
        Passes the input to add_student function
        """
        student_id = input("Enter an ID: ")
        name = input("Enter student's name: ")
        group = input("Enter student's group: ")
        self.__student_list.add_student(student_id, name, group)

    def list_students_ui(self):
        """""
        :param self
        Takes all the students from the lists and prints them
        """
        students = self.__student_list.get_students()
        for student in students:
            print(student)

    def remove_student_ui(self):
        """""
        :param self
        Takes the word input from the user
        Passes it to remove_student function
        """
        student_id = input("Enter the student's id: ")
        try:
            student_id = int(student_id)
        except ValueError:
            print("Invalid ID!")
            return
        operations = []
        student_removed = self.__student_list.remove_student(student_id)
        student_assignments = self.__student_assign_list.delete_student_assignment(student_id)
        grades = self.__grade_list.delete_grade_student(student_id)
        operations.append(student_removed)
        for elem in student_assignments:
            operations.append(elem)
        for elem in grades:
            operations.append(elem)
        self.__undo_service.record(CascadedOperation(operations))

    def modify_student_ui(self):
        """""
        :param self
        Passes the parameters to Student Service through the modify_student function
        """
        student_id = input("Enter the student's id: ")
        print("Enter the new name and group for the student. Leaving them empty will not modify the value ")
        name = input("Enter a new name for the student: ")
        group = input("Enter a new group for the student: ")
        self.__student_list.modify_student(student_id, name, group)

    def modify_assignment_ui(self):
        """""
        :param self
        Passes the parameters to Assignment Service through modify_assignments
        Checks the validity of the input
        Calls the modify_assignment from the Student Service which
        modifies the modified assignment in the assignments list of all students
        """
        assignment_id = input("Enter the assignment's id: ")
        print(
            "Enter the new description and deadline for the assignment. Leaving them empty will not modify the value ")
        description = input("Enter a new description for the assignment: ")
        deadline = input("Enter a new deadline for the assignment: ")
        if deadline != '':
            try:
                deadline = datetime.strptime(deadline, '%d/%m/%Y')
            except ValueError:
                print("Invalid date format!")
                return
        done = False
        assignmnets = self.__assignments_list.get_assignments()
        for assignment in assignmnets:
            if assignment.get_assignment_id() == assignment_id:
                done = True
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist!")

        assignment_modify = self.__assignments_list.modify_assignment(assignment_id, description, deadline)
        operations = []
        operations.append(assignment_modify)
        self.__undo_service.record(CascadedOperation(operations))

    def give_assignment_group_ui(self):
        """""
        :param self
        Checks the input from the user
        If the input is valid then the function will call the give_assignment_group function
        from the Student Service and gives the assignment to the group of students
        """
        group = input("Enter a group name: ")
        id_assignment = input("Enter assignment's ID: ")
        try:
            id_assignment = int(id_assignment)
        except ValueError:
            print("The id must be an integer")
            return
        done = False
        operations = []
        assignments = self.__assignments_list.get_assignments()
        for assignment in assignments:
            if int(assignment.get_assignment_id()) == int(id_assignment):
                done = True
                students = self.__student_list.get_students()
                for student in students:
                    if group == student.get_group():
                        operation = self.__student_assign_list.give_assignment_group(assignment.get_assignment_id(),
                                                                                     student.get_student_id())
                        operations.append(operation)
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist! No changes have been made")
        self.__undo_service.record(CascadedOperation(operations))

    def give_assignment_student_ui(self):
        """""
        :param self
        Check the input from the user
        If the input is valid, the function calls the Student Service function
        to give the assignment to the given student
        """
        id_student = input("Enter student's ID: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("The id must be an integer")
            return
        id_assignment = input("Enter assignment's ID: ")
        try:
            id_assignment = int(id_assignment)
        except ValueError:
            print("The id must be an integer")
            return
        done = False
        assignments = self.__assignments_list.get_assignments()
        for assignment in assignments:
            if int(assignment.get_assignment_id()) == int(id_assignment):
                done = True
                self.__student_assign_list.give_assignment(id_assignment, id_student)
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist! No changes have been made")

    def give_assignments_ui(self):
        """""
        :param self
        Simple menu manager
        Gives the user the option to give assignments to one student or a group of students
        """
        print("     1: Give an Assignment to one student")
        print("     2: Give an Assignment to a group of students")
        yes = input("Enter command: ")
        if yes == '1':
            self.give_assignment_student_ui()
        elif yes == '2':
            self.give_assignment_group_ui()
        else:
            print("Invalid command!")

    def add_assignments_ui(self):
        """""
        :param self
        Takes the input from the user and checks it
        Passes the input to add_assignment function
        """
        assignment_id = input("Enter an ID: ")
        description = input("Enter the assignment's description: ")
        deadline = input("Enter the deadline for the assignment (day/month/year): ")
        try:
            deadline = datetime.strptime(deadline, '%d/%m/%Y')
        except ValueError:
            print("Invalid date format!")
            return
        self.__assignments_list.add_assignment(assignment_id, description, deadline)

    def list_assignments_ui(self):
        """""
        :param self
        Takes all the assignments from the lists and prints them
        """
        assignments = self.__assignments_list.get_assignments()
        for assignment in assignments:
            print(assignment)

    def list_student_assignments_ui(self):
        """""
        :param self
        Takes input from the user
        Checks if the input is correct
        Lists all the assignments of a student
        """
        id_student = input("Enter the student's ID: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("The ID must be an integer! ")
            return
        list_assignment = self.__student_assign_list.list_student_assignments(id_student)
        assignments = self.__assignments_list.get_assignments()
        printed = False
        for i in range(len(list_assignment)):
            for assignment in assignments:
                if int(list_assignment[i]) == int(assignment.get_assignment_id()):
                    print(assignment)
                    printed = True
        if not printed:
            print("No assignments!")

    def remove_assignment_ui(self):
        """""
        :param self
        Takes the id input from the user
        Passes it to remove_student function
        """
        assignment_id = input("Enter the assignment id: ")
        done = False
        assignments = self.__assignments_list.get_assignments()
        for assignment in assignments:
            if assignment.get_assignment_id() == assignment_id:
                done = True
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist!")
        try:
            student_removal = self.__student_assign_list.delete_assignment(assignment_id)
        except StudRepoException as sre:
            raise StudRepoException(str(sre))
        try:
            assignment_removal = self.__assignments_list.remove_assignment(assignment_id)
        except AssignRepoException as are:
            raise AssignRepoException(str(are))
        grade_removal = self.__grade_list.delete_grade(assignment_id)
        operations = []
        operations.append(assignment_removal)
        for elem in student_removal:
            operations.append(elem)
        print(assignment_removal)
        for elem in grade_removal:
            operations.append(elem)
        self.__undo_service.record(CascadedOperation(operations))

    def grade_assignment_ui(self):
        """""
        Function that allows grading of the assignments
        Takes the input and checks it
        Prints the ungraded assignments of a student
        Raises errors in case of invalid input
        """
        id_student = input("Enter student's ID: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("The ID must be an integer")
            return
        done = False
        students = self.__student_list.get_students()
        ungraded = []
        for student in students:
            if int(student.get_student_id()) == int(id_student):
                done = True
                assignments = self.__assignments_list.get_assignments()
                grades = self.__grade_list.get_grades()
                for assign in assignments:
                    if self.__student_assign_list.exists(assign.get_assignment_id(), student.get_student_id()):
                        graded = False
                        if self.__grade_list.exists(int(assign.get_assignment_id()), int(student.get_student_id())):
                            graded = True
                        if not graded:
                            print(assign)
                            ungraded.append(assign)
        if not done:
            raise StudRepoException("Student with the given ID does not exist!")
        if ungraded == []:
            raise StudRepoException("Student has no ungraded assignments! ")
        id_assignment = input("Enter assignment's ID: ")
        try:
            id_assignment = int(id_assignment)
        except ValueError:
            print("The ID must be an integer")
            return
        found = False
        for assignment in ungraded:
            if int(assignment.get_assignment_id()) == int(id_assignment):
                found = True
        if not found:
            print("The given assignment is already graded or hasn't been assigned to the student!")
            return

        grade_value = input("Enter student's grade: ")
        try:
            grade_value = float(grade_value)
        except ValueError:
            print("The grade must be an integer or a rational number!")
            return
        if grade_value < 1 or grade_value > 10:
            raise StudRepoException("The grade must be between 1 and 10!")
        grade = Grade(id_student, id_assignment, grade_value)
        self.__grade_list.add_grade(grade)

    def list_student_grades_ui(self):
        """""
        :param self
        Takes input from the user
        Checks if the input is correct
        Lists all the grades of a student
        """
        id_student = input("Enter the student's ID: ")
        try:
            id_student = int(id_student)
        except ValueError:
            print("The ID must be an integer! ")
            return
        printed = False
        list_grades = self.__grade_list.get_grades()
        for grade in list_grades:
            if int(grade.get_student_id()) == int(id_student):
                print(grade)
                printed = True
        if not printed:
            print("No grades!")

    def test_students(self):
        first_name = ['Anca', 'Andrei', 'Alex', 'Daniel', 'Alexandra', 'Razvan', 'Raul', 'Elena', 'Andreea']
        last_name = ['Bucur', 'Petrescu', 'Turdean', 'Turturica', 'Pop', 'Popescu', 'Lazar', 'Uifelean']
        i = 1
        while i <= 10:
            done = False
            student_id = str(randint(1, 1000))
            name = choice(first_name) + ' ' + choice(last_name)
            group = randint(1, 3)
            try:
                self.__student_list.add_student(student_id, name, group)
                done = True
            except StudRepoException:
                done = False
            if done:
                i += 1

    def test_assignments(self):
        descriptions = ['Game','Network Application','Console Application','Artificial Intelligence']
        i = 1
        while i <= 10:
            done = False
            assignment_id = str(randint(1, 1000))
            description = choice(descriptions)
            deadline = str(randint(1, 30)) + '/' + str(randint(1, 12)) + '/2020'
            deadline = datetime.strptime(deadline, '%d/%m/%Y')
            try:
                self.__assignments_list.add_assignment(assignment_id, description, deadline)
                done = True
            except AssignRepoException:
                done = False
            if done:
                i += 1

    def run(self):
        done = False
        self.test_students()
        self.test_assignments()
        self.__undo_service.set_index()
        self.__undo_service.set_history()
        while not done:
            ui.print_menu(self)
            command = input("Enter command: ")
            if command in self.__commands:
                try:
                    self.__commands[command]()
                except StudException as se:
                    print(se)
                except AssignException as ae:
                    print(ae)
                except AssignRepoException as are:
                    print(are)
                except GradeRepoException as gre:
                    print(gre)
                except StudentAssignRepoException as sare:
                    print(sare)
                except StudRepoException as sre:
                    print(sre)
            elif command == '0':
                print("The program will exit now...")
                done = True
            else:
                print("Invalid command!")
