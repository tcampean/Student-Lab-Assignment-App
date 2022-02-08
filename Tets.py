from Entity.Student import *
from Entity.Assignment import *
from Repositories.StudentRepo import *
from Repositories.AssignmentRepo import *
from Service.StudentService import  *
from Service.AssignmentService import *

class Tests:

    def __run_domain_tests(self):
        student_id = 30
        student_name = "Yes Name"
        group = "3"
        student = Student(student_id, student_name, group)
        assert (student.get_student_id() == 30)
        assert (student.get_name() == "Yes Name")
        assert (student.get_group() == "3")
        student2 = Student(student_id, student_name, 'fsf')
        # assert (student==student2)
        assignment_id = 30
        description = "Yes"
        deadline = "3/3/2020"
        assignment = Assignment(assignment_id, description, deadline)
        assert (assignment.get_assignment_id() == '30')
        assert (assignment.get_description() == "Yes")
        assert (assignment.get_deadline() == "3/3/2020")
        assignment2 = Assignment(assignment_id,description,"fadsgfh")
        # assert(assignment == assignment2)

    def __run_validation_tests(self):
        student = Student(23, "EFEF", "ffsf")
        validator_student = StudentValidator()
        try:
            validator_student.validate(student)
            assert True
        except StudException as se:
            assert False
        student2 = Student(85934990394, "Yes 2", "23")
        validator_student.validate(student2)
        assignment = Assignment(2323,"Edfdfa", '3/3/2020')
        validator_assignment = AssignmentValidator()
        try:
            validator_assignment.validate(assignment)
            assert True
        except AssignException as ae:
            assert False

    def __run_RepoTests(self):
        student = Student('34', "No", "3")
        student_repo = StudentRepo()
        assert (student_repo.__len__() == 0)
        student_repo.add_stud(student)
        assert (student_repo.__len__() == 1)
        student2 = Student('34', None, None)
        result_student = student_repo.find_id(student2)
        assert student.get_name() == result_student.get_name()
        assert student.get_group() == result_student.get_group()
        another_student = Student('1351', "Maria ger", "33")
        try:
            student_repo.add_stud(another_student)
            assert True
        except StudException:
            assert False
        try:
            student_repo.update_student(34,'Yes','')
            assert True
        except AssignRepoException:
            assert False
        result_student = student_repo.find_id(student2)
        assert student.get_name() == result_student.get_name()
        assert student.get_group() == result_student.get_group()
        assert (student_repo.__len__() == 2)
        student_repo.remove(34)
        assert (student_repo.__len__() == 1)
        assignment = Assignment(34, "Nowe", "3/3/2020")
        assignment_repo = AssignRepo()
        assert (assignment_repo.__len__() == 0)
        assignment_repo.add(assignment)
        assert (assignment_repo.__len__() == 1)
        assignment2 = Assignment(34, None, None)
        result_assignment = assignment_repo.find_id(assignment2)
        assert assignment.get_description() == result_assignment.get_description()
        assert assignment.get_deadline() == result_assignment.get_deadline()
        another_assignment = Assignment(13, "yes and no", "3/3/2020")
        try:
            assignment_repo.add(another_assignment)
            assert True
        except AssignException:
            assert False
        assignment_repo.update_assignment(34, 'Yes', '')
        result_assignment = assignment_repo.find_id(assignment2)
        assert assignment.get_description() == result_assignment.get_description()
        assert assignment.get_deadline() == result_assignment.get_deadline()
        assert (assignment_repo.__len__() == 2)
        assignment_repo.remove('34')
        assert assignment_repo.__len__() == 1



    def run_service_tests(self):
        student_repo = StudentRepo()
        validations = StudentValidator()
        student_service = Student_Service(student_repo, validations)
        student_id = '43431341'
        name = 'dgdsg'
        group = '33b'
        assert student_service.get_number_students() == 0
        student_service.add_student(student_id, name, group)
        assert student_service.get_number_students() == 1
        assignment_repo = AssignRepo()
        another_validation = AssignmentValidator()
        assignment_service = Assignment_Service(assignment_repo, another_validation)
        assignment_id = '43431341'
        description = 'dgdsg'
        deadline = '3/3/2020'
        assert assignment_service.get_number_assignments() == 0
        assignment_service.add_assignment(assignment_id, description, deadline)
        assert assignment_service.get_number_assignments() == 1

    def run_all_tests(self):
        self.__run_domain_tests()
        self.__run_validation_tests()
        self.__run_RepoTests()
        self.run_service_tests()


tests = Tests()
#tests.run_all_tests()