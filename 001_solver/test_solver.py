import pytest
from solver import Expression, Solver


class TestSolver:
    @pytest.mark.parametrize(
        "sequence, expected_res",
        [
            ([1, "plus", 2], 3),
            ([1, Solver.PLUS, 2], 3),
            ([3, "minus", 2], 1),
            ([3, Solver.MINUS, 2], 1),
            ([5, "times", 7], 35),
            ([5, Solver.TIMES, 7], 35),
            ([42, "divide", 2], 21),
            ([42, Solver.DIVIDE, 2], 21),
        ],
    )
    def test_solves_sequence(self, sequence, expected_res):
        res = Solver.solve(sequence)
        assert res == expected_res

    @pytest.mark.parametrize(
        "expression, expected_res",
        [
            (Expression(1, "plus", 2), 3),
            (Expression(1, Solver.PLUS, 2), 3),
            (Expression(3, "minus", 2), 1),
            (Expression(3, Solver.MINUS, 2), 1),
            (Expression(5, "times", 7), 35),
            (Expression(5, Solver.TIMES, 7), 35),
            (Expression(42, "divide", 2), 21),
            (Expression(42, Solver.DIVIDE, 2), 21),
        ],
    )
    def test_solves_expression(self, expression, expected_res):
        res = Solver.solve(expression)
        assert res == expected_res

    @pytest.mark.parametrize(
        "exp, expected_res",
        [
            ([1, "plus", [5, "minus", 2]], 4),
            ([5, "times", [12, "divide", [1, "plus", 2]]], 20),
            (
                Expression(
                    16,
                    Solver.DIVIDE,
                    [2, "times", 4]
                ),
                2,
            ),
            (
                Expression(
                    40,
                    Solver.MINUS,
                    Expression(
                        10,
                        "plus",
                        Expression(
                            3,
                            Solver.TIMES,
                            2,
                        ),
                    ),
                ),
                24,
            ),
        ],
    )
    def test_solves_nested(self, exp, expected_res):
        """
        :param exp:
        :param expected_res:
        :return:
        """
        res = Solver.solve(exp)
        assert res == expected_res
