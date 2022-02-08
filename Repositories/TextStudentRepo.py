from Repositories.StudentRepo import *
from Entity.Student import *
class TextStudentRepo(StudentRepo):

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
        f = open(self._file_name, 'wt')
        for student in self._student_list:
            line = str(student.get_student_id()) + ';' +str(student.get_name()) + ';' + str(student.get_group())
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        f = open(self._file_name, 'rt')  # read text
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            ok = 1
            if len(line) !=3:
                ok = 0
            if ok == 1:
                student=Student(int(line[0]),line[1],line[2])
                validator = StudentValidator()
                try:
                    validator.validate(student)
                except StudException:
                    ok = 0
                try:
                    super().find_id(int(line[0]))
                    ok = 0
                except StudRepoException:
                    ok = 1
            if ok == 1:
                super().add_stud(Student(int(line[0]), line[1], line[2]))