from Repositories.StudentAssignRepo import *
from Entity.Student_Assignment import *
import pickle

class BinaryStudentAssignRepo(StudentAssignRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def give_assignment(self, id_assignment, id_student):
        super().give_assignment(id_assignment, id_student)
        self._save()

    def remove_assignment(self, id_assignment):
        super().remove_assignment(id_assignment)
        self._save()

    def delete_single_assignment(self, id_assignment, id_student):
        super().delete_single_assignment(id_assignment, id_student)
        self._save()

    def remove_assignment_student(self, id_student):
        super().remove_assignment_student(id_student)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wb')
        for assignment in self._student_assignments:
           pickle.dump(assignment, f)
        f.close()

    def _load(self):
        f = open(self._file_name, 'rb')
        i = 0
        while i >=0:
            try:
                assignment = pickle.load(f)
                if not super().exists(assignment.get_assignment_id(),assignment.get_student_id()):
                    super().give_assignment(assignment.get_assignment_id(),assignment.get_student_id())
            except EOFError as e:
                break
            i+=1
        f.close()

