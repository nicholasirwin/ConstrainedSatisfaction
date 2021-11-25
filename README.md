CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Methods
 * Testing
 

INTRODUCTION
------------
In this project, I write a program for solving constraint satisfaction problems using backtracking search with different variable and value heuristic functions. First, I model the classic CSP of map coloring where neighboring regions cannot be the same color given a limited list of color options. Next, I model the CSP of placing every component of varying dimensions on a circuit board of certain dimensions. Lastly, I provide the functionality of visualization for a particular search on a particular CSP.

METHODS
------------
- `MapColorCSP`:
  - `make_pairs()`: Generate a length-2 tuple for all possible combinations of neighboring state colors
  - `make_constraints()`: Build constraint dictionary mapping each possible pair of neighboring states to all corresponding legal color assignments for these two states.
  - `make_assignment(assignment)`: Visualization function to display each state with the corresponding color assignment.
- `CircuitBoardCSP`:
  - `build_var_domains()`: Map each variable (component) to all legal locations (ie, locations for the bottom left hand corner of the component such that its dimensions do not exceed the dimensions of the circuit board).
  - `build_adj_list()`: Map each variable (component) to a list of all other components because in theory, any component can neighbor any other component in this CSP.
  - `make_constraints()`: Build constraint dictionary mapping each possible pair of neighboring variables (components) to all corresponding legal position assignments for these two components.
  - `no_overlap(variable, neighbor, v_loc, n_loc)`: Given two variables and potential location assignments for each variable, check that the components do not overlap.
  - `animate_board(assignment): Given a legal assignment for each component, display the newly populated circuit board by representing each unpopulated spot with '.' and each part of each component with a letter.
- `backtrackingSearch`:
  - `backtracking_search(csp, mrv, degree, lcv, ac3)`: Given a CSP and true values for each possible heuristic function, intialize each variable assignments to be -1 and call the recursive `backtracking()` function.
  - `backtracking(assignment, csp, mrv, degree, lcv, ac3)`: Given current variable assignments and switches for heuristic functions, first check if all variables are assigned. If not, select unassigned variable using MRV or degree heuristic. Then, assign value to variable using LCV heuristic and arc checking. Recursively update assignment and new variable.
  - `complete_test(assignment)`: Simply check if all variables have been assigned a value (not -1).
  - `select_unassigned_variable(csp, assignment, mrv, degree)`: Return an unassigned variable using heuristic functions. If no heuristic, return first unassigned variable.
  - `degree_heuristic(csp, assignment, vars)`: Heuristic function to return the unassigned variable associated with the most unassigned neighbors.
  - `MRV_heuristic(csp, assignment, degree)`: Heuristic function to return the unassigned variable with the fewest values in its current domain. If tie, use degree heuristic.
  - `check_consistent(csp, var, val, assignment)`: Check consistency (legality) of a potential new variable assignment by checking that the new assignment does not violate the constraint map as it relates to the current assigned variables.
  - `order_domain_values(var, lcv, csp, assignment)`: Heuristic function to return a reordered (or unchanged) domain of values for a given variable based on presence or absence of LCV heuristic function.
  - `update_domains(csp, var, val)`: Given a variable and a value, remove value from variables domain.
  - `AC_3(csp)`: Inference function. Build and update a queue of arcs (each arc is each possible neighboring states) and then look forward beyond current assignments and update each variable's domain if possible current and future assignments do not allow this value for this variable.
  - `revise(csp, arc)`: Helper function for AC3. Given a CSP and a particular arc, remove all values in the first variable's domain that will never be assigned (impossible).

TESTING
------------
For testing and visualizing solutions to either the map coloring or circuit board problems with all possible combinations of heuristic values, execute test script `MapColorTest.py` or `CircuitBoardTest.py`. You can also edit the various tests. For MapColoring, the map of Australian territories as well as a map of the states of the US are solved. For CircuitBoard, varying boards and components with differing complexities are solved too. See below for the output of two examples runs on each problem. Enjoy.

```
-----------------------------------------------------TEST16: US! MapColorCSP w/ No Heuristics + No AC3------------------------------------------------
int form: [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 0, 0, 0, 1, 0, 0, 2, 2, 1, 1, 0, 1, 2, 3, 3, 2, 0, 0, 2, 2, 1, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 2, 3, 0, 1, 3, 0, 3]
Nodes visited: 4088659

-----------------------------------------------------TEST19: US! MapColorCSP w/ Only LCV Heuristic + AC3----------------------------------------------
int form: [0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 2, 0, 0, 1, 1, 0, 0, 2, 2, 1, 2, 1, 1, 1, 3, 3, 2, 0, 0, 2, 0, 2, 3, 3, 3, 3, 2, 0, 1, 2, 1, 3, 1, 1, 2, 3, 2, 2, 2, 0, 0]
Nodes visited: 32
```

```
-----------------------------------------------------TEST17: CircuitBoardCSP Only MRV Heuristic and no AC3--------------------------------------------
board result: 
aaaaaaaccc.gg
fffffeeccc.gg
fffffeebbbbbb
fffffeebbbbbb
.ddddd.bbbbbb
.ddddd.bbbbbb
int form: [(0, 5), (7, 0), (7, 4), (1, 0), (5, 2), (0, 2), (11, 4)]
Nodes visited: 1717

-----------------------------------------------------TEST13: CircuitBoardCSP MRV + LCV Heuristics w/ AC3----------------------------------------------
board result: 
aaaaaaaddddd.
eefffffddddd.
eefffffbbbbbb
eefffffbbbbbb
.gg.cccbbbbbb
.gg.cccbbbbbb
int form: [(0, 5), (7, 0), (4, 0), (7, 4), (0, 2), (2, 2), (1, 0)]
Nodes visited: 969
```