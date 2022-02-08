from Repositories.AssignmentRepo import *
from Entity.Assignment import *
import pickle

class BinaryAssignmentRepo(AssignRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_assignment(self, assignment):
        super().add_assignment(assignment)
        self._save()

    def remove_assignment(self, id_assignment):
        super().remove_assignment(id_assignment)
        self._save()

    def update_assignment(self, id_assignment, description, deadline):
        super().update_assignment(id_assignment,description,deadline)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wb')
        for assignment in self._assignment_list:
           pickle.dump(assignment, f)
        f.close()

    def _load(self):
        f = open(self._file_name, 'rb')
        i = 0
        while i >=0:
            try:
                assignment = pickle.load(f)
                validator = AssignmentValidator()
                ok = 1
                try:
                    validator.validate(assignment)
                except AssignException:
                    ok = 0
                try:
                    super().find_id(assignment.get_assignment_id())
                    ok = 0
                except AssignRepoException:
                    ok = 1
                if ok == 1:
                    super().add_assignment(assignment)
            except EOFError as e:
                break
            i+=1
        f.close()

