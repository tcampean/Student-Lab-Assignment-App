from Repositories.AssignmentRepo import *
from Entity.Assignment import *
class TextAssignmentRepo(AssignRepo):

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
        f = open(self._file_name, 'wt')
        for assignment in self._assignment_list:
            line = str(assignment.get_assignment_id()) + ';' +str(assignment.get_description()) + ';' + str(assignment.get_deadline())
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        """
        Load data from file
        We assume file-saved data is valid
        """
        f = open(self._file_name, 'rt')  # read text
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            ok = 1
            if len(line) !=3:
                ok = 0
            if ok == 1:
                assignment = Assignment(int(line[0]), line[1], line[2])
                validator = AssignmentValidator()
                try:
                    validator.validate(assignment)
                except AssignException:
                    ok = 0
                try:
                    super().find_id(int(line[0]))
                    ok = 0
                except AssignRepoException:
                    ok = 1

            if ok == 1:
                super().add_assignment(Assignment(int(line[0]), line[1], line[2]))