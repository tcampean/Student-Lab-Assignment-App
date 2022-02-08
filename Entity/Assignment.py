class AssignException(Exception):
    pass


class AssignmentValidator:

    def validate(self, assignment):
        errors = ""
        ok = 1
        try:
            a = int(assignment.get_assignment_id())
        except ValueError:
            errors += "Assignment's ID must be an integer!\n"
            ok = 0
        if ok == 1:
            a = int(assignment.get_assignment_id())
            if a < 0:
                errors += "Assignment's ID must be positive!\n"

        if len(assignment.get_description()) < 3:
            errors += "Assignment's description must be longer!\n"
        if assignment.get_deadline() == '':
            errors += "Invalid deadline !\n"
        if len(errors) > 0:
            raise AssignException(errors)



class Assignment:

    def __init__(self, assignment_id, description, deadline):
        self.__assignment_id = str(assignment_id)
        self.__description = str(description)
        self.__deadline = deadline

    def get_assignment_id(self):
        return self.__assignment_id

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def set_description(self, description):
        self.__description = description

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def __str__(self):
        return ('Assignment ID: ' + str(self.__assignment_id)).rjust(5) + (
                    '  Description: ' + str(self.__description)).rjust(10) + (
                           '    Deadline: ' + str(self.__deadline)).rjust(20)

    def __eq__(self, other):
        return self.__assignment_id == other.__assignment_id
