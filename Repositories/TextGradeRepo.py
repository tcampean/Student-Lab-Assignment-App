from Repositories.GradeRepo import *
from Entity.Grade import *
class TextGradeRepo(GradeRepo):

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
        f = open(self._file_name, 'wt')
        for grade in self._grade_list:
            line = str(grade.get_student_id()) + ';' +str(grade.get_assignment_id()) + ';' + str(grade.get_grade_value())
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
            grade = Grade(int(line[0]), int(line[1]), float(line[2]))
            if not super().exists(grade.get_assignment_id(),grade.get_student_id()):
                super().add_grade(Grade(int(line[0]), int(line[1]), float(line[2])))

