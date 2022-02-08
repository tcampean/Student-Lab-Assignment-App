
from PyQt5.QtWidgets import *
from random import choice,randint
from Repositories.StudentRepo import StudRepoException
from Entity.Student import Student,StudentValidator
from PyQt5.QtCore import QModelIndex

class StudentMenuWindow(QWidget):
    def __init__(self,studentService):
        super().__init__()
        self.setWindowTitle("Student Menu")
        self.setMinimumSize(800,600)
        self.studentService = studentService
        panel = QHBoxLayout()

        addButton = QPushButton('Add Student')
        deleteButton = QPushButton('Delete Student')
        updateButton = QPushButton('Update Student')
        self.studentList = QListWidget()
        panel.addWidget(self.studentList)

        buttonPanel = QVBoxLayout()

        textPanel = QGridLayout()
        self.idField = QLineEdit()
        idLabel = QLabel('ID')
        idLabel.setBuddy(self.idField)

        self.nameField = QLineEdit()
        nameLabel = QLabel('Name')
        nameLabel.setBuddy(self.nameField)

        self.groupField = QLineEdit()
        groupLabel = QLabel('Group')
        groupLabel.setBuddy(self.groupField)

        textPanel.addWidget(idLabel,0,0)
        textPanel.addWidget(self.idField,0,1)
        textPanel.addWidget(nameLabel,1,0)
        textPanel.addWidget(self.nameField,1,1)
        textPanel.addWidget(groupLabel,2,0)
        textPanel.addWidget(self.groupField,2,1)

        textWidget = QWidget()
        textWidget.setLayout(textPanel)
        buttonPanel.addWidget(textWidget)

        addButton.clicked.connect(self.addStudent)
        deleteButton.clicked.connect(self.deleteStudent)
        updateButton.clicked.connect(self.updateStudent)

        buttonPanel.addWidget(addButton)
        buttonPanel.addWidget(deleteButton)
        buttonPanel.addWidget(updateButton)
        widget = QWidget()
        widget.setLayout(buttonPanel)
        panel.addWidget(widget)
        self.setLayout(panel)
        self.test_students()
        self.studentList.itemSelectionChanged.connect(self.updateFields)



        self.updateStudentList()
        self.studentList.setCurrentRow(0)

    def updateStudentList(self):
        students = self.studentService.get_students()
        self.studentList.clear()
        for student in students:
            item = QListWidgetItem(student.__str__())
            self.studentList.addItem(item)

    def test_students(self):
        first_name = ['Anca', 'Andrei', 'Alex', 'Daniel', 'Alexandra', 'Razvan', 'Raul', 'Elena', 'Andreea']
        last_name = ['Bucur', 'Petrescu', 'Turdean', 'Turturica', 'Pop', 'Popescu', 'Lazar', 'Uifelean']
        i = 1
        while i <= 10:
            done = False
            student_id = str(randint(1, 1000))
            name = choice(first_name) + ' ' + choice(last_name)
            group = randint(1, 3)
            try:
                self.studentService.add_student(student_id, name, group)
                done = True
            except StudRepoException:
                done = False
            if done:
                i += 1

    def addStudent(self):
        id = self.idField.text()
        name = self.nameField.text()
        group = self.groupField.text()
        if id == '' or name == '' or group == '':
            return
        try:
            self.studentService.add_student(id, name, int(group))
        except StudRepoException:
            global box
            box = QMessageBox()
            box.setText('Invalid student!')
            box.show()
        self.updateStudentList()

    def updateFields(self):
        if len(self.studentService.get_students()) == 0:
            self.idField.clear()
            self.nameField.clear()
            self.groupField.clear()
        else:
            i = self.studentList.currentIndex()
            s = self.studentService.get_students()[i.row()]
            self.idField.setText(str(s.get_student_id()))
            self.nameField.setText(str(s.get_name()))
            self.groupField.setText(str(s.get_group()))

    def deleteStudent(self):
        id = self.idField.text()
        if id == '':
            return

        self.studentService.remove_student(id)
        if len(self.studentService.get_students()) == 0:
            self.studentList.clear()
        else:
            self.updateStudentList()
        self.updateFields()
        self.studentList.setCurrentRow(0)

    def updateStudent(self):
        id = self.idField.text()
        name = self.nameField.text()
        group = self.groupField.text()
        if id == '' or name == '' or group == '':
            return
        self.studentService.modify_student(id,name,int(group))
        self.updateStudentList()
        self.updateFields()
        self.studentList.setCurrentRow(0)







