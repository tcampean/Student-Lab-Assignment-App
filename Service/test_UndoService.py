from unittest import TestCase
from Service.UndoService import *
from Repositories.AssignmentRepo import *
from Repositories.StudentRepo import *
from Service.AssignmentService import *
from Service.StudentService import *
from Entity.Student import *


class TestUndoService(TestCase):

    def test_undo(self):
        undo_service = UndoService()
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        student_service = Student_Service(student_repo,student_validator,undo_service)
        assert undo_service.undo() == False
        student_service.add_student('30',"Yes","gr")
        undo_service.undo()
        student_service.add_student('30', "Yes", "gr")
        student_service.add_student('31', "Yes", "gr")
        assignment = Assignment(5,"yes",'3/3/2020')
        student_service.give_assignment_group("gr",assignment)
        undo_service.undo()


    def test_redo(self):
        undo_service = UndoService()
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('30', "Yes", "gr")
        assert undo_service.redo() == False
        undo_service.undo()
        undo_service.redo()

    def test_set_index(self):
        undo_service = UndoService()
        undo_service.set_index()
        assert undo_service._index == -1

    def test_set_history(self):
        undo_service = UndoService()
        undo_service.set_history()
        assert undo_service._history == []

    def run_all(self):
        self.test_redo()
        self.test_undo()
        self.test_set_history()
        self.test_set_index()


