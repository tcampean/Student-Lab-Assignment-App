class AssignRepoException(Exception):
    pass


class AssignRepo:
    def __init__(self):
        self._assignment_list = []

    def list_assignment_list(self):
        """""
        :param self
        :return the list of all assignments
        """
        return self._assignment_list

    def add_assignment(self, assignment):
        """""
        :param self
        :param assignment the assignment provided by the user
        Appends in the assignment list a new assignment
        """
        if assignment in self._assignment_list:
            raise AssignRepoException("The assignment already exists!")
        self._assignment_list.append(assignment)

    def find_id(self, id_assign):
        """""
        Looks for the given ID in the assignment list
        """
        for assignment in self._assignment_list:
            if int(assignment.get_assignment_id()) == int(id_assign):
                return assignment
        raise AssignRepoException("There no such assignment!")

    def update_assignment(self, id_assignment, description, deadline):
        """""
        Checks for the id of the wanted assignment
        Sets the values given pe the users
        """
        done = False
        for assignment in self._assignment_list:
            if assignment.get_assignment_id() == str(id_assignment):
                if description != '':
                    assignment.set_description(description)
                if deadline != '':
                    assignment.set_deadline(deadline)
                done = True
        if not done:
            raise AssignRepoException("Assignment with the given id does not exist!")

    def remove_assignment(self, id_assignment):
        """""
        Checks for the given id in the assignment list
        Deletes the assignment with the given id from the list
        """
        for assignment in self._assignment_list:
            if assignment.get_assignment_id() == id_assignment:
                assign = assignment
                self._assignment_list.remove(assignment)
                return assign
        raise AssignRepoException("Assignment with the given id does not exist! No changes have been made")

    def __len__(self):
        return len(self._assignment_list)

    def get_all(self):
        """""
        Returns the list of all assignments
        """
        return self._assignment_list
