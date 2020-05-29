import operator
from dataclasses import dataclass
from typing import Union, Tuple, Sequence

from exceptions import InvalidExpression, InvalidOperator

AcceptedExpressionType = Union[
    "Expression",
    Tuple["OperandType", str, "OperandType"],
    Sequence,
]
OperandType = Union[int, float, AcceptedExpressionType]


@dataclass
class Expression:
    operand1: OperandType
    operator: str
    operand2: OperandType


class Solver:
    PLUS = operator.add
    MINUS = operator.sub
    TIMES = operator.mul
    DIVIDE = operator.truediv

    OPERATORS = {
        "plus": operator.add,
        "minus": operator.sub,
        "times": operator.mul,
        "divide": operator.truediv,
    }

    @classmethod
    def get_operator(cls, exp: Expression):
        """
        Gets callable operator from expression
        :param exp:
        :return:
        """
        if callable(exp.operator):
            return exp.operator

        if isinstance(exp.operator, str):
            try:
                return cls.OPERATORS[exp.operator.lower()]
            except KeyError:
                raise InvalidOperator(f"No such operator {exp.operator!r}!")

        raise InvalidOperator(
            f"Please provide a valid operator or callable, not {exp.operator!r}!"
        )

    @classmethod
    def ensure_expression(cls, exp_or_sequence: AcceptedExpressionType):
        """
        :param exp_or_sequence:
        :return:
        """
        if not isinstance(exp_or_sequence, Expression):
            try:
                operand1, operator, operand2 = exp_or_sequence
            except ValueError:
                raise InvalidExpression(
                    "Expression has to be of type Expression or an iterable of exactly 3 items!"
                )
            return Expression(operand1, operator, operand2)
        return exp_or_sequence

    @classmethod
    def ensure_operand(cls, value: Union[OperandType, AcceptedExpressionType]):
        """
        :param value:
        :return:
        """
        if isinstance(value, (int, float)):
            return value
        return cls.solve(value)

    @classmethod
    def solve_expression(cls, exp: Expression):
        """
        Solves expressions
        :param exp:
        :return:
        """
        op = cls.get_operator(exp)
        return op(
            exp.operand1,
            cls.ensure_operand(exp.operand2),
        )

    @classmethod
    def solve(cls, expression: AcceptedExpressionType):
        """
        Optionally converts iterable to expression
        and then solves expression

        >>> assert Solver.solve([1, "plus", 2]) == 3

        :param expression:
        :return:
        """
        exp = cls.ensure_expression(expression)
        return cls.solve_expression(exp)
