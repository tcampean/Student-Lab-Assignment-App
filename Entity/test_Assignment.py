from unittest import TestCase
from Entity.Assignment import *


class TestAssignment(TestCase):
    def test_get_assignment_id(self):
        assignment = Assignment(20,"Yes","3/3/2020")
        assert assignment.get_assignment_id() == '20'

    def test_get_description(self):
        assignment = Assignment(20, "Yes", "3/3/2020")
        assert assignment.get_description() == 'Yes'

    def test_get_deadline(self):
        assignment = Assignment(20, "Yes", "3/3/2020")
        assert assignment.get_deadline() == '3/3/2020'

    def test_set_description(self):
        description = "No"
        assignment = Assignment(20, "Yes", "3/3/2020")
        assignment.set_description(description)
        assert assignment.get_description() == description

    def test_set_deadline(self):
        deadline = "4/3/2020"
        assignment = Assignment(20, "Yes", "3/3/2020")
        assignment.set_deadline(deadline)
        assert assignment.get_deadline() == deadline

    def test_str(self):
        assignment = Assignment(20, "Yes", "3/3/2020")
        string = ('Assignment ID: ' + str(20)).rjust(5) + (
                '  Description: ' + str("Yes")).rjust(10) + (
                '    Deadline: ' + str("3/3/2020")).rjust(20)
        assert assignment.__str__() == string

    def test_eq(self):
        assignment1 = Assignment(20, "Yes", "3/3/2020")
        assignment2 = Assignment(20, "Yes", "3/3/2020")
        assert assignment1.__eq__(assignment2)

    def test_validate(self):
        validator = AssignmentValidator()
        errors = ""
        assignment = Assignment(23, "EFEF", "ffsf")
        try:
            validator.validate(assignment)
        except AssignException as ae:
            errors += str(ae)
        assert errors == ""
        assignment2 = Assignment(-1, "Yes 2", "23")
        try:
            validator.validate(assignment2)
        except AssignException as ae:
            errors += str(ae)
        assert errors == "Assignment's ID must be positive!\n"
        errors = ""
        assignment3 = Assignment('23d', "Yes 2", "3/3/2020")
        try:
            validator.validate(assignment3)
        except AssignException as ae:
            errors += str(ae)
        assert errors == "Assignment's ID must be an integer!\n"
        assignment4 = Assignment(23,"eh","3/3/2020")
        errors = ""
        try:
            validator.validate(assignment4)
        except AssignException as ae:
            errors += str(ae)
        assert errors == "Assignment's description must be longer!\n"

    def run_all(self):
        self.test_eq()
        self.test_str()
        self.test_get_assignment_id()
        self.test_validate()
        self.test_get_deadline()
        self.test_get_description()
        self.test_set_deadline()
        self.test_set_description()