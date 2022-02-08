
from UI.Console import ui
from Service.GradeService import *
from Service.StudentAssignmentService import *
from Service.test_UndoService import *
from Repositories.TextStudentRepo import *
from Repositories.TextGradeRepo import *
from Repositories.TextAssignmentRepo import *
from Repositories.TextStudentAssignRepo import *
from jproperties import Properties
from os import path
import os.path
from Repositories.BinaryStudentRepo import *
from Repositories.BinaryAssignmentRepo import *
from Repositories.BinaryGradeRepo import *
from Repositories.BinaryStudentAssignRepo import *


if __name__ == '__main__':
    configs = Properties()
    with open('settings.properties','rb') as config_file:
        configs.load(config_file)
    if configs.get("repository").data == 'inmemory':
        student_repo = StudentRepo()
        assignment_repo = AssignRepo()
        grade_repo = GradeRepo()
        student_assign_repo = StudentAssignRepo()
        student_validator = StudentValidator()
        assignment_validator = AssignmentValidator()
        undo_service = UndoService()

        student_service = Student_Service(student_repo, student_validator, undo_service)
        assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
        student_assign_service = StudentAssignmentService(student_assign_repo, undo_service)
        grade_service = Grade_Service(grade_repo, undo_service)
        console = ui(student_service, assignment_service, student_assign_service, grade_service, undo_service)
        console.run()

    elif configs.get("repository").data == 'binaryfiles':
        string1 = str(configs.get("students").data)
        string1 = string1[1:len(string1)-1]
        ok = 1
        if path.exists(string1) == False:
            print("The student file does not exist or is not a file!")
            ok = 0
        string2 = str(configs.get("assignments").data)
        string2 = string2[1:len(string2) - 1]
        if path.exists(string2) == False:
            print("The assignment file does not exist or is not a file!")
            ok = 0
        string3 = str(configs.get("grades").data)
        string3 = string3[1:len(string3) - 1]
        if path.exists(string3) == False:
            print("The grade file does not exist or is not a file!")
            ok = 0
        string4 = str(configs.get("student_assignments").data)
        string4 = string4[1:len(string4) - 1]
        if path.exists(string4) == False:
            print("The student assignment file does not exist or is not a file")
            ok = 0
        if ok == 1:
            student_repo = BinaryStudentRepo(string1)
            assignment_repo = BinaryAssignmentRepo(string2)
            grade_repo = BinaryGradeRepo(string3)
            student_assign_repo = BinaryStudentAssignRepo(string4)
            student_validator = StudentValidator()
            assignment_validator = AssignmentValidator()
            undo_service = UndoService()

            student_service = Student_Service(student_repo, student_validator, undo_service)
            assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
            student_assign_service = StudentAssignmentService(student_assign_repo, undo_service)
            grade_service = Grade_Service(grade_repo, undo_service)
            console = ui(student_service, assignment_service, student_assign_service, grade_service, undo_service)
            console.run()

    elif configs.get("repository").data == 'textfiles':
        string1 = str(configs.get("students").data)
        string1 = string1[1:len(string1)-1]
        ok = 1
        if path.exists(string1) == False:
            print("The student file does not exist or is not a file!")
            ok = 0
        string2 = str(configs.get("assignments").data)
        string2 = string2[1:len(string2) - 1]
        if path.exists(string2) == False:
            print("The assignment file does not exist or is not a file!")
            ok = 0
        string3 = str(configs.get("grades").data)
        string3 = string3[1:len(string3) - 1]
        if path.exists(string3) == False:
            print("The grade file does not exist or is not a file!")
            ok = 0
        string4 = str(configs.get("student_assignments").data)
        string4 = string4[1:len(string4) - 1]
        if path.exists(string4) == False:
            print("The student assignment file does not exist or is not a file")
            ok = 0
        if ok == 1:
            student_repo = TextStudentRepo(string1)
            assignment_repo = TextAssignmentRepo(string2)
            grade_repo = TextGradeRepo(string3)
            student_assign_repo = TextStudentAssignRepo(string4)

            student_validator = StudentValidator()
            assignment_validator = AssignmentValidator()
            undo_service = UndoService()

            student_service = Student_Service(student_repo, student_validator, undo_service)
            assignment_service = Assignment_Service(assignment_repo, assignment_validator, undo_service)
            student_assign_service = StudentAssignmentService(student_assign_repo, undo_service)
            grade_service = Grade_Service(grade_repo, undo_service)
            console = ui(student_service, assignment_service, student_assign_service, grade_service, undo_service)
            console.run()

    else:
        print("Invalid repository status!")
