### 001

Python -​ Write a Solver class/object in Python that would accept parameter in the form of: `[3​ , “Plus”, 1]` ​, `[6​ , “Times”, 2]`... ​ or an object with properties “operand1”, “operator” and “operand2”, the option that you prefer, and returns the result of the arithmetic.
Note:​ element representing the operator is the name of a function or a reference to that function – implement them as well (Plus, Minus, Times and Divide).
Note:​ in the future there may be a need to support another operations without changing the existing code or changing it as little as possible.

### 001(a)
Python -​ make your implementation that it handles inner operations, (so you can pass other operations instead of any or both operators, something like: ​ `[3​ , “Plus”, [6, “Times”, 2]]` ​ ), that would be equivalent to `3 + (6 * 2)`.
