from unittest import TestCase
from Entity.Grade import Grade


class TestGrade(TestCase):
    def test_get_assignment_id(self):
        grade = Grade(20,20,5)
        assert grade.get_assignment_id()== '20'

    def test_get_student_id(self):
        grade = Grade(20,20,5)
        assert grade.get_student_id() == '20'

    def test_get_grade_value(self):
        grade = Grade(20,20,5)
        assert grade.get_grade_value() == 5.0

    def test_str(self):
        grade = Grade(20,20,5)
        string = ('Student ID: '+str(20)).rjust(5)+('  Assignment ID: ' +str(20)).rjust(10)+('    Grade: '+ str(5.0)).rjust(20)
        assert grade.__str__() == string

    def test_eq(self):
        grade1 = Grade(20,20,5)
        grade2 = Grade(20,20,5)
        assert grade1.__eq__(grade2)

    def run_all(self):
        self.test_eq()
        self.test_str()
        self.test_get_student_id()
        self.test_get_assignment_id()
        self.test_get_grade_value()

