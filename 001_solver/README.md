### 001

Python -​ Write a Solver class/object in Python that would accept parameter in the form of: `[3​ , “Plus”, 1]` ​, `[6​ , “Times”, 2]`... ​ or an object with properties “operand1”, “operator” and “operand2”, the option that you prefer, and returns the result of the arithmetic.
Note:​ element representing the operator is the name of a function or a reference to that function – implement them as well (Plus, Minus, Times and Divide).
Note:​ in the future there may be a need to support another operations without changing the existing code or changing it as little as possible.

### 001(a)
Python -​ make your implementation that it handles inner operations, (so you can pass other operations instead of any or both operators, something like: ​ `[3​ , “Plus”, [6, “Times”, 2]]` ​ ), that would be equivalent to `3 + (6 * 2)`.


#### Example

```python
from solver import Solver, Expression

assert Solver.solve([1, "plus", 2]) == 3
assert Solver.solve(Expression(1, Solver.PLUS, 2)) == 3

assert Solver.solve([5, "times", [12, "divide", [1, "plus", 2]]]) == 20

assert Solver.solve(
    Expression(
        40, Solver.MINUS, Expression(
            10, "plus", Expression(
                3, Solver.TIMES, 2,
            ),
        ),
    ),
) == 24
```
