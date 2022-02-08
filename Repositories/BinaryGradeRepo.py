from Repositories.GradeRepo import *
from Entity.Grade import *
import pickle
class BinaryGradeRepo(GradeRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_grade(self, grade):
        super().add_grade(grade)
        self._save()

    def delete_grade(self, id_assignment):
        super().delete_grade(id_assignment)
        self._save()

    def delete_single_grade(self, grade):
        super().delete_single_grade(grade)
        self._save()

    def delete_student_grade(self, id_student):
        super().delete_student_grade(id_student)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wb')
        for grade in self._grade_list:
            pickle.dump(grade, f)
        f.close()

    def _load(self):
        f = open(self._file_name, 'rb')
        i = 0
        while i >= 0:
            try:
                grade = pickle.load(f)
                if not super().exists(grade.get_assignment_id(),grade.get_student_id()):
                    super().add_grade(grade)
            except EOFError as e:
                break
            i += 1
        f.close()