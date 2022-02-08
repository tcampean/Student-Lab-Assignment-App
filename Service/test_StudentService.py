from unittest import TestCase
from Repositories.StudentRepo import *
from Service.StudentService import *
from Entity.Student import *
from Entity.Assignment import *
from Entity.Grade import *
from Service.UndoService import *

class TestStudent_Service(TestCase):
    def test_get_number_students(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo,student_validator,undo_service)
        assert student_service.get_number_students() == 0


    def test_add_student(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        assert student_service.get_number_students() == 0
        student_service.add_student(20,"yes","56")
        assert student_service.get_number_students() == 1
        string = ''
        try:
            student_service.add_student(20, "yes", "56")
        except StudRepoException as sre:
            string = str(sre)
        assert string == "The student already exists!"


    def test_remove_student(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        assert student_service.get_number_students() == 0
        student_service.add_student('20', "yes", "56")
        assert student_service.get_number_students() == 1
        student_service.remove_student(20)
        assert student_service.get_number_students() == 0
        try:
            student_service.remove_student(19)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "Student with the given id does not exist! No changes have been made"


    def test_modify_student(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        assert student_service.get_number_students() == 0
        student_service.add_student('20', "yes", "56")
        students = student_service.get_students()
        student_service.modify_student('20', 'Yes', '3')
        for student in students:
            if student.get_student_id() == '20':
                assert student.get_name() == 'Yes'
                assert student.get_group() == '3'



    def test_give_assignment_student(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5,'ye','3/3/2020')
        student_service.give_assignment_student(20,assignment)
        string = ''
        try:
            student_service.give_assignment_student(20,assignment)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "The student already has this assignment!"


    def test_give_assignment_group(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        student_service.give_assignment_group('56', assignment)
        string = ''
        try:
            student_service.give_assignment_group('3',assignment)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "There is no such group!"


    def test_list_student_assignments(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        string = ''
        try:
            student_service.list_student_assignments('20')
        except StudRepoException as se:
            string = str(se)
        assert string == "No assignments!"


    def test_list_student_grades(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        string = ''
        try:
            student_service.list_student_grades('20')
        except StudRepoException as se:
            string = str(se)
        assert string == "No grades!"

    def test_remove_assignment(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        student_service.give_assignment_student(20,assignment)
        students = student_service.get_students()
        student_service.remove_assignment(5)
        for student in students:
            if int(student.get_student_id()) == 20:
                assert student.get_len_assignments() == 0

    def test_modify_assignment(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        student_service.give_assignment_student(20, assignment)
        students = student_service.get_students()
        student_service.modify_assignment(5,'no','5/5/2020')
        for student in students:
            if int(student.get_student_id()) == 20:
                assignments = student.get_assignments()
                for assignment in assignments:
                    assert assignment.get_description() == 'no'
                    assert assignment.get_deadline() == '5/5/2020'


    def test_give_grade(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        grade = Grade(20, 5, 4)
        string = ''
        try:
            student_service.give_grade(grade)
        except StudRepoException as sre:
            string = str(sre)
        assert string == "The student doesn't have this assignment!"

    def test_remove_grade_a(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        assignment2 = Assignment(6,'adfaf','3/3/2020')
        student_service.give_assignment_student(20,assignment)
        student_service.give_assignment_student(20,assignment2)
        grade = Grade(20,5,7)
        grade2= Grade(20,6,10)
        student_service.give_grade(grade)
        student_service.give_grade(grade2)
        students = student_service.get_students()
        student_service.remove_grade_a(5)
        for student in students:
            if int(student.get_student_id()) == 20:
                assert student.get_len_grades() == 1

    def test_get_students(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        assert student_service.get_students() == []

    def test_order_by_grade_assignment(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        student_service.give_assignment_student(20,assignment)
        grade = Grade(20, 5, 7)
        student_service.give_grade(grade)
        result = StudentGrade('20',7.0)
        result2 = student_service.order_by_grade_assignment(5)
        for entry in result2:
            assert str(result) == str(entry)

    def test_order_by_grade_total(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        assignment = Assignment(5, 'ye', '3/3/2020')
        student_service.give_assignment_student(20, assignment)
        grade = Grade(20, 5, 7)
        student_service.give_grade(grade)
        result = StudentGrade('20', 7.0)
        result2 = student_service.order_by_grade_total()
        for entry in result2:
            assert str(result) == str(entry)

    def test_late_assign(self):
        student_repo = StudentRepo()
        student_validator = StudentValidator()
        undo_service = UndoService()
        student_service = Student_Service(student_repo, student_validator, undo_service)
        student_service.add_student('20', "yes", "56")
        deadline = datetime.today() - timedelta(1)
        assignment = Assignment(5, 'ye', deadline)
        student_service.give_assignment_student(20, assignment)
        result = LateStudent(20)
        result2 = student_service.late_assign()

        for entry in result2:
            assert str(result) == "Student ID: "+str(entry)

    def run_all(self):
        self.test_give_grade()
        self.test_add_student()
        self.test_get_students()
        self.test_late_assign()
        self.test_modify_assignment()
        self.test_get_number_students()
        self.test_give_assignment_group()
        self.test_give_assignment_student()
        self.test_modify_student()
        self.test_list_student_assignments()
        self.test_list_student_grades()
        self.test_get_students()
        self.test_order_by_grade_assignment()
        self.test_order_by_grade_total()
        self.test_remove_assignment()
        self.test_remove_grade_a()
        self.test_remove_student()
