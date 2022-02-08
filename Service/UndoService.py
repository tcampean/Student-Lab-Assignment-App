class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def record(self, operation):
        self._history = self._history[0:self._index + 1]

        self._history.append(operation)
        self._index += 1

    def undo(self):
        if self._index == -1:
            return False

        self._history[self._index].undo()
        self._index -= 1

    def redo(self):
        if self._index == len(self._history) - 1:
            return False

        self._index += 1
        self._history[self._index].redo()

    def set_index(self):
        self._index = -1

    def set_history(self):
        self._history = []


class CascadedOperation:
    """
    Represents a cascaded operation (where 1 user operation corresponds to more than 1 program op)
    """

    def __init__(self, operations):
        self._operations = operations

    def undo(self):
        for oper in self._operations:
            oper.undo()

    def redo(self):
        for oper in self._operations:
            oper.redo()


class Operation:
    """
    How to undo/redo a program operation
    """

    def __init__(self, fun_call_undo, fun_call_redo):
        self._fun_call_undo = fun_call_undo
        self._fun_call_redo = fun_call_redo

    def undo(self):
        self._fun_call_undo()

    def redo(self):
        self._fun_call_redo()


class FunctionCall:
    '''
    A function call with parameters
    '''

    def __init__(self, function_ref, *function_params):
        self._function_ref = function_ref
        self._function_params = function_params

    def call(self):
        return self._function_ref(*self._function_params)

    def __call__(self):
        return self.call()


