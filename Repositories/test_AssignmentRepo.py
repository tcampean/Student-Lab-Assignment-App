from unittest import TestCase
from Entity.Assignment import *
from Repositories.AssignmentRepo import *


class TestAssignRepo(TestCase):

    def test_list_assignment_list(self):
        assignment_list = AssignRepo()
        assert assignment_list.list_assignment_list() == []

    def test_add(self):
        assignment_list = AssignRepo()
        assignment = Assignment(20,'Yes','2/2/2020')
        assert assignment_list.__len__() == 0
        assignment_list.add(assignment)
        assert  assignment_list.__len__() == 1

    def test_find_id(self):
        assignment_list = AssignRepo()
        assignment = Assignment(20, 'Yes', '2/2/2020')
        assignment2 = Assignment(20,'Yes','2/2/2020')
        assignment_list.add(assignment)
        assert assignment_list.find_id(assignment2.get_assignment_id()) == assignment



    def test_update_assignment(self):
        assignment_list = AssignRepo()
        assignment = Assignment(20, 'Yes', '2/2/2020')
        assignment_list.add(assignment)
        assignment_list.update_assignment(20,"Nono",'3/3/2020')
        assert assignment.get_deadline() == '3/3/2020'
        assert assignment.get_description() == "Nono"
        string = ''
        try:
            assignment_list.update_assignment(21,"Nono",'3/3/2020')
        except AssignRepoException as are:
            string = str(are)
        assert string == "Assignment with the given id does not exist!"

    def test_remove(self):
        assignment_list = AssignRepo()
        assignment = Assignment(20, 'Yes', '2/2/2020')
        assignment_list.add(assignment)
        assert assignment_list.__len__() == 1
        string = ''
        try:
            assignment_list.remove(21)
        except AssignRepoException as are:
            string = str(are)
        assert string == "Assignment with the given id does not exist! No changes have been made"
        assignment_list.remove('20')
        assert assignment_list.__len__() == 0

    def test_get_all(self):
        assignment_list = AssignRepo()
        assignment = Assignment(20, 'Yes', '2/2/2020')
        assignment_list.add(assignment)
        result= []
        result.append(assignment)
        assert assignment_list.get_all() == result

    def run_all(self):
        self.test_add()
        self.test_find_id()
        self.test_get_all()
        self.test_remove()
        self.test_list_assignment_list()
        self.test_update_assignment()
