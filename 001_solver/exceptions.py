class SolverException(Exception):
    """
    Exception base
    """


class InvalidExpression(SolverException):
    """
    For invalid expressions
    """


class InvalidOperator(SolverException):
    """
    For invalid operators
    """
