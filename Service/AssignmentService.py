from Entity.Assignment import Assignment
from Repositories.AssignmentRepo import AssignRepoException
from Service.UndoService import UndoService,FunctionCall,CascadedOperation, Operation


class Assignment_Service:
    """""
    Book_Service class containing program's functionalities
    It is bound to the BookList class
    """

    def __init__(self, assignment_list, valid_assignment, undo_service):
        '''''
        :param self
        :param assignment_list Dependency Injection;
        '''
        self.__assignment_list = assignment_list
        self.__valid_assignment = valid_assignment
        self.__undo_service = undo_service

    def get_number_assignments(self):
        """""
        :param self
        return the number of elements in the assignments list
        """
        return len(self.__assignment_list)

    def add_assignment(self, assignment_id, description, deadline):
        """""
        :param self
        :param assignment_id ; given by the user
        :param description ; given by the user
        :param deadline ; given by the user
        Creates a Student class type variable and passes it to the add function
        """
        assignment = Assignment(assignment_id, description, deadline)
        self.__valid_assignment.validate(assignment)
        try:
            self.__assignment_list.add_assignment(assignment)
            undo_fun = FunctionCall(self.__assignment_list.remove_assignment, assignment.get_assignment_id())
            redo_fun = FunctionCall(self.__assignment_list.add_assignment, assignment)
            self.__undo_service.record(Operation(undo_fun, redo_fun))
        except AssignRepoException as are:
            raise AssignRepoException(str(are))

    def remove_assignment(self, id_assignment):
        """""
        :param self
        :param id_assignment ; given by the user in the ui function
        Passes the parameter to the remove function
        """
        assign = 0
        assignments = self.__assignment_list.get_all()
        for assignment in assignments:
            if int(assignment.get_assignment_id()) == int(id_assignment):
                assign = assignment
        try:
            self.__assignment_list.remove_assignment(id_assignment)
            undo_fun = FunctionCall(self.__assignment_list.add_assignment, assign)
            redo_fun = FunctionCall(self.__assignment_list.remove_assignment, assign.get_assignment_id())
        except AssignRepoException as are:
            raise AssignRepoException(str(are))
        return Operation(undo_fun,redo_fun)



    def modify_assignment(self, id_assignment, description, deadline):
        """""
        :param self
        :param id_assignment ; given by the user in the ui function
        :param description; given by the user in the ui function
        :param deadline; given by the user in the ui function
        """""
        try:
            assignment = self.__assignment_list.find_id(id_assignment)
        except AssignRepoException as are:
            raise AssignRepoException(str(are))
        id_assignment2 = assignment.get_assignment_id()
        description2 = assignment.get_description()
        deadline2 = assignment.get_deadline()
        self.__assignment_list.update_assignment(id_assignment, description, deadline)
        undo_fun = FunctionCall(self.__assignment_list.update_assignment, id_assignment2, description2, deadline2)
        redo_fun = FunctionCall(self.__assignment_list.update_assignment, id_assignment, description, deadline)
        return Operation(undo_fun,redo_fun)

    def get_assignments(self):
        """""
        :param self
        :return a list containing all the books
        """
        return self.__assignment_list.get_all()
