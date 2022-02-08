
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *
from StudentMenu import StudentMenuWindow
from Entity.Student import Student,StudentValidator
import sys

class MenuWindow(QMainWindow):
    def __init__(self,serviceStudent):
        QMainWindow.__init__(self)
        self.setWindowTitle("Main Menu")
        self.setMinimumSize(400,300)
        self.studentService = serviceStudent
        panel = QHBoxLayout()
        studButton = QPushButton('Student Menu')
        assignButton = QPushButton('Assignment Menu')
        gradesButton = QPushButton('Grade Menu')

        studButton.clicked.connect(self.displayStudentMenu)

        panel.addWidget(studButton)
        panel.addWidget(assignButton)
        panel.addWidget(gradesButton)
        widget = QWidget()
        widget.setLayout(panel)
        self.setCentralWidget(widget)

    def displayStudentMenu(self):
        global sm
        sm = StudentMenuWindow(self.studentService)
        sm.show()







