from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
import MenuWindow
from Service import StudentService, UndoService
from Repositories import StudentRepo
from Entity.Student import Student,StudentValidator


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    studentRepo = StudentRepo.StudentRepo()
    studentValidator = StudentValidator()
    undo = UndoService.UndoService()

    serviceStudent = StudentService.Student_Service(studentRepo,studentValidator,undo)
    mainWin = MenuWindow.MenuWindow(serviceStudent)
    mainWin.show()
    app.exec_()