from Repositories.StudentAssignRepo import *
class TextStudentAssignRepo(StudentAssignRepo):

    def __init__(self, file_name):
        super().__init__()
        self._file_name = file_name
        self._load()

    def give_assignment(self,id_assignment,id_student):
        super().give_assignment(id_assignment,id_student)
        self._save()

    def remove_assignment(self,id_assignment):
        super().remove_assignment(id_assignment)
        self._save()

    def delete_single_assignment(self,id_assignment,id_student):
        super().delete_single_assignment(id_assignment,id_student)
        self._save()

    def remove_assignment_student(self,id_student):
        super().remove_assignment_student(id_student)
        self._save()

    def _save(self):
        f = open(self._file_name, 'wt')
        for assignment in self._student_assignments:
            line = str(assignment.get_assignment_id()) + ';' + str(assignment.get_student_id())
            f.write(line)
            f.write('\n')
        f.close()

    def _load(self):
        f = open(self._file_name, 'rt')  # read text
        lines = f.readlines()
        f.close()

        for line in lines:
            line = line.split(';')
            if not super().exists(int(line[0]), int(line[1])):
                super().give_assignment(int(line[0]), int(line[1]))