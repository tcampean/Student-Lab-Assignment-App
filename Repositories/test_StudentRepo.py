from unittest import TestCase
from Entity.Assignment import *
from Entity.Grade import *
from Entity.Student import *
from Repositories.StudentRepo import *


class TestStudentRepo(TestCase):
    def test_list_student_list(self):
        student = Student(20,"Yes","534")
        student_list = StudentRepo()
        stud_list = []
        student_list.add_stud(student)
        stud_list.append(student)
        assert stud_list == student_list.list_student_list()

    def test_add_stud(self):
        student = Student(20,"Yes","534")
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        assert student_list.__len__() == 0
        student_list.add_stud(student)
        assert student_list.__len__() == 1

    def test_add_assign_student(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(20,"Yes","3/3/2020")
        string = ''
        try:
            student_list.add_assign_student(4,assignment)
        except StudRepoException as sre:
            string +=str(sre)
        assert string == "Student with the given id does not exist! No changes have been made"
        string = ''
        try:
            student_list.add_assign_student(20,assignment)
        except StudRepoException as sre:
            string +=str(sre)
        assert string == "Assigned successfully!"

    def test_remove_assign(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(20, "Yes", "3/3/2020")
        string = ''
        try:
            student_list.add_assign_student(20, assignment)
        except StudRepoException as sre:
            string += str(sre)
        assert student.get_len_assignments() == 1
        student_list.remove_assign(20)
        assert student.get_len_assignments() == 0

    def test_modify_assign(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(5,"Yes","3/3/2020")
        string = ''
        try:
            student_list.add_assign_student(20, assignment)
        except StudRepoException as sre:
            string += str(sre)
        student_list.modify_assign(5,"No",'5/5/2020')
        for student in student_list.list_student_list():
            for assignment in student.get_assignments():
                if int(assignment.get_assignment_id()) == 5:
                    assert assignment.get_description() == "No"
                    assert assignment.get_deadline() == "5/5/2020"


    def test_find_id(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        student2 = Student(15,"Yes",'2323')
        string = ''
        try:
            student_list.find_id(student2.get_student_id())
        except StudRepoException as sre:
            string += str(sre)
        assert string == "There is no such student!"
        assert student == student_list.find_id(student.get_student_id())

    def test_update_student(self):
        student = Student('20', "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        student2 = Student(15, "Yes", '2323')
        string = ''
        try:
            student_list.update_student(15,"No",'24')
        except StudRepoException as sre:
            string += str(sre)
        assert string == "Student with the given id does not exist!"
        student_list.update_student(20,"No",'24')
        assert student.get_name() == "No"
        assert student.get_group() == '24'

    def test_remove(self):
        student = Student('20', "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assert student_list.__len__() == 1
        student2 = Student(15, "Yes", '2323')
        string = ''
        try:
            student_list.remove(15)
        except StudRepoException as sre:
            string += str(sre)
        assert string == "Student with the given id does not exist! No changes have been made"
        student_list.remove('20')
        assert student_list.__len__() == 0

    def test_assign(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(20, "Yes", "3/3/2020")
        string = ''
        try:
            student_list.assign(4, assignment)
        except StudRepoException as sre:
            string += str(sre)
        assert string == "There is no student with such ID!"
        student_list.assign('20', assignment)


    def test_assign2(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(20, "Yes", "3/3/2020")
        string = ''
        try:
            student_list.assign2('5', assignment)
        except StudRepoException as sre:
            string += str(sre)
        assert string == "There is no such group!"
        string = ''
        student_list.assign2("534", assignment)


    def test_get_all(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        result = []
        result.append(student)
        assert result == student_list.get_all()

    def test_list_assignments(self):
        student = Student('20', "Yes", "534")
        student2 = Student(21,"Yes", "35")
        student_list = StudentRepo()
        student_list.add_stud(student)
        student_list.add_stud(student2)
        assignment = Assignment(5,"Yes","3/3/2020")
        student.append_assign(assignment)
        string = ''
        student_list.list_assignments(20)
        try:
            student_list.list_assignments(21)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "No assignments!"
        try:
            student_list.list_assignments(41)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "There is no student with such ID!"

    def test_list_grades(self):
        student = Student('20', "Yes", "534")
        student2 = Student('21', "Yes", "35")
        student_list = StudentRepo()
        student_list.add_stud(student)
        student_list.add_stud(student2)
        assignment = Assignment(5, "Yes", "3/3/2020")
        student.append_assign(assignment)
        grade = Grade(20,5,10)
        string = ''
        assert student.get_len_grades() == 0
        student_list.grade(grade)
        assert student.get_len_grades() == 1

        grade2 = Grade(20,6,7)
        try:
            student_list.list_grades(20)
        except StudRepoException as sre:
            string = str(sre)
        assert string == ""
        try:
            student_list.list_grades(21)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "No grades!"
        try:
            student_list.list_grades(25)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "There is no student with such ID!"


    def test_grade(self):
        student = Student('20', "Yes", "534")
        student2 = Student('21', "Yes", "35")
        student_list = StudentRepo()
        student_list.add_stud(student)
        student_list.add_stud(student2)
        assignment = Assignment(5, "Yes", "3/3/2020")
        student.append_assign(assignment)
        grade = Grade(20, 5, 10)
        string = ''
        assert student.get_len_grades() == 0
        student_list.grade(grade)
        assert student.get_len_grades() == 1
        grade2 = Grade(20,6 , 7)
        try:
            student_list.grade(grade2)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "The student doesn't have this assignment!"
        try:
            student_list.grade(grade)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "The assignment is already graded!"

    def test_remove_grade(self):
        student = Student('20', "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(5, "Yes", "3/3/2020")
        assignment2 = Assignment(6,"No","3/3/2020")
        student.append_assign(assignment2)
        student.append_assign(assignment)
        grade = Grade(20, 5, 10)
        grade2 = Grade(20,6,5)
        assert student.get_len_grades() == 0
        student_list.grade(grade)
        student_list.grade(grade2)
        assert student.get_len_grades() == 2
        student_list.remove_grade(5)
        assert student.get_len_grades() == 1

    def test_remove_grade_student(self):
        student = Student('20', "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(5, "Yes", "3/3/2020")
        assignment2 = Assignment(6,"Yes", "3/3/2020")
        student.append_assign(assignment)
        student.append_assign(assignment2)
        grade = Grade(20, 5, 10)
        student_list.grade(grade)
        grade2 = Grade(20,6,10)
        student_list.grade(grade2)
        assert student.get_len_grades() == 2
        student_list.remove_grade_student(grade)
        assert student.get_len_grades() == 1

    def test_modify_assign_student(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(5,"Yes","3/3/2020")
        assignment2 = Assignment(6,"Ye","5/5/2020")
        string = ''
        try:
            student_list.add_assign_student(20, assignment)
            student_list.add_assign_student(20,assignment)
        except StudRepoException as sre:
            string += str(sre)
        try:
            student_list.add_assign_student(20, assignment2)
        except StudRepoException as sre:
            string += str(sre)
        student_list.modify_assign_student(20,5,"No",'5/5/2020')
        for student in student_list.list_student_list():
            if student.get_student_id() == 20:
                for assignment in student.get_assignments():
                    if int(assignment.get_assignment_id()) == 5:
                        assert assignment.get_description() == "No"
                        assert assignment.get_deadline() == "5/5/2020"

    def test_remove_assign_student(self):
        student = Student(20, "Yes", "534")
        student_list = StudentRepo()
        student_list.add_stud(student)
        assignment = Assignment(20, "Yes", "3/3/2020")
        string = ''
        try:
            student_list.add_assign_student(20, assignment)
        except StudRepoException as sre:
            string += str(sre)
        assert student.get_len_assignments() == 1
        student_list.remove_assign_student(20,assignment)
        assert student.get_len_assignments() == 0

    def run_all(self):
        self.test_remove()
        self.test_get_all()
        self.test_find_id()
        self.test_grade()
        self.test_add_stud()
        self.test_add_assign_student()
        self.test_assign()
        self.test_assign2()
        self.test_list_assignments()
        self.test_list_grades()
        self.test_list_student_list()
        self.test_modify_assign()
        self.test_modify_assign_student()
        self.test_remove_assign()
        self.test_remove_assign_student()
        self.test_remove_grade()
        self.test_remove_grade_student()
        self.test_update_student()