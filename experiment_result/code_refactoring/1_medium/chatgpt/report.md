STRENGTH:
Solves the problem, albeit naively.

WEAKNESS:
It solves the problem by toggling between 'print' and a logger function
using a single boolean flag passed in the argument of the class constructor.
This is not an efficient solution. Decoupling with dependency-injection
is a much better approach, but GPT-4o model fails to identify that as a
better way to refactor the code.
