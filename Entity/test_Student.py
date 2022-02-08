from unittest import TestCase
from Entity.Student import *
from Entity.Assignment import Assignment
from Entity.Grade import Grade


class TestStudent(TestCase):

    def test_get_student_id(self):
        student_id = 30
        student_name = "Yes Name"
        group = "3"
        student = Student(student_id, student_name, group)
        assert (student.get_student_id() == 30)

    def test_get_name(self):
        student_id = 30
        student_name = "Yes Name"
        group = "3"
        student = Student(student_id, student_name, group)
        assert (student.get_name() == "Yes Name")

    def test_get_group(self):
        student_id = 30
        student_name = "Yes Name"
        group = "3"
        student = Student(student_id, student_name, group)
        assert (student.get_group() == "3")

    def test_get_assignments(self):
        student = Student(20, "aef", "weg")
        assignments = []
        assignment = Assignment(30,"Yes","3/3/2020")
        assignments.append(assignment)
        student.append_assign(assignment)
        assert student.get_assignments() == assignments

    def test_get_grades(self):
        grades = []
        student = Student(20, "aef", "weg")
        grade = Grade(30,20,5)
        student.append_grade(grade)
        grades.append(grade)
        assert student.get_grades() == grades

    def test_set_student_id(self):
        student_id = 30
        student = Student(20,"aef","weg")
        student.set_student_id(student_id)
        assert student.get_student_id() == student_id

    def test_set_name(self):
        student = Student(20, "aef", "weg")
        student.set_name("Andrei")
        assert student.get_name() == "Andrei"

    def test_set_group(self):
        student = Student(20, "aef", "weg")
        student.set_group("3")
        assert student.get_group() == "3"

    def test_get_len_assignments(self):
        student = Student(20, "aef", "weg")
        assert student.get_len_assignments() == 0

    def test_get_len_grades(self):
        student = Student(20, "aef", "weg")
        assert student.get_len_grades() == 0

    def test_eq(self):
        student1 = Student(20,"aef","weg")
        student2 = Student(20,"aef","weg")
        assert student1.__eq__(student2) == True

    def test_str(self):
        student = Student(20,"aef","weg")

        string = ('Student ID: ' + str(20)).rjust(5) + ('  Name: ' + str("aef")).rjust(10) + (
                    '    Group: ' + str("weg")).rjust(15)
        assert string == student.__str__()

    def test_validator(self):
        errors=""
        student = Student(23, "EFEF", "ffsf")
        validator_student = StudentValidator()
        try:
            validator_student.validate(student)
        except StudException as se:
            errors+= str(se)
        assert errors == ""
        student2 = Student(-1, "Yes 2", "23")
        try:
            validator_student.validate(student2)
        except StudException as se:
            errors += str(se)
        assert errors == "Student's ID must be positive"
        errors = ""
        student3 = Student('23d', "Yes 2", "23")
        try:
            validator_student.validate(student3)
        except StudException as se:
            errors += str(se)
        assert errors == "Student's ID must contain only numbers!\n"

    def run_all(self):
        self.test_get_assignments()
        self.test_get_name()
        self.test_get_grades()
        self.test_eq()
        self.test_get_assignments()
        self.test_str()
        self.test_get_group()
        self.test_get_len_assignments()
        self.test_get_len_grades()
        self.test_get_student_id()
        self.test_validator()
        self.test_set_group()
        self.test_set_student_id()
        self.test_set_name()




