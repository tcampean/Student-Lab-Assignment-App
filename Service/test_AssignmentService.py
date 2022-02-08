from unittest import TestCase
from Entity.Assignment import *
from Repositories.AssignmentRepo import *
from Service.AssignmentService import *


class TestAssignment_Service(TestCase):
    def test_get_number_assignments(self):
        assignment_repo = AssignRepo()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()
        assignment_service = Assignment_Service(assignment_repo,assignment_validator,undo_service)
        assert assignment_service.get_number_assignments() == 0


    def test_add_assignment(self):
        assignment_repo = AssignRepo()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()
        assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
        assert assignment_service.get_number_assignments() == 0
        assignment_service.add_assignment(20,'Yes','3/3/2020')
        assert assignment_service.get_number_assignments() == 1
        string = ''
        try:
            assignment_service.add_assignment(20, 'Yes', '3/3/2020')
        except AssignRepoException as are:
            string = str(are)
        assert string == "The assignment already exists!"

    def test_remove_assignment(self):
        assignment_repo = AssignRepo()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()
        assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
        assignment_service.add_assignment(20, 'Yes', '3/3/2020')
        assert assignment_service.get_number_assignments() == 1
        assignment_service.remove_assignment('20')
        assert assignment_service.get_number_assignments() == 0

    def test_modify_assignment(self):
        assignment_repo = AssignRepo()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()
        assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
        assignment_service.add_assignment(20, 'Yes', '3/3/2020')
        assignment_service.modify_assignment(20,"No","5/2/2020")
        assignments = assignment_service.get_assignments()
        for assignment in assignments:
            if assignment.get_assignment_id() == '20':
                assert assignment.get_description() == "No"
                assert assignment.get_deadline() == "5/2/2020"
        string = ''
        try:
            assignment_service.modify_assignment(5,'yes','no')
        except AssignRepoException as are:
            string = str(are)
        assert string == "There no such assignment!"


    def test_get_assignments(self):
        assignment_repo = AssignRepo()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()
        assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
        assignment_service.add_assignment(20, 'Yes', '3/3/2020')
        assignment = Assignment(20,'Yes','3/3/2020')
        result = []
        result.append(assignment)
        assert assignment_service.get_assignments() == result

    def run_all(self):
        self.test_remove_assignment()
        self.test_add_assignment()
        self.test_get_number_assignments()
        self.test_get_assignments()
        self.test_modify_assignment()

