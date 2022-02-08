from Repositories.StudentRepo import *
from Entity.Student import *
import pickle

class BinaryStudentRepo(StudentRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def add_stud(self, item):
        super().add_stud(item)
        self._save()

    def remove_stud(self, id_student):
        super().remove_stud(id_student)
        self._save()

    def update_student(self,id_student,name,group):
        super().update_student(id_student,name,group)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wb')
        for student in self._student_list:
           pickle.dump(student, f)
        f.close()

    def _load(self):
        f = open(self._file_name, 'rb')
        i = 0
        while i >=0:
            try:
                student = pickle.load(f)
                validator = StudentValidator()
                ok = 1
                try:
                    validator.validate(student)
                except StudException:
                    ok = 0
                try:
                    super().find_id(student.get_student_id())
                    ok = 0
                except StudRepoException:
                    ok = 1
                if ok == 1:
                    super().add_stud(student)
            except EOFError as e:
                break
            i+=1
        f.close()

