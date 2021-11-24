from MapColorCSP import MapColorCSP
from CircuitBoardCSP import CircuitBoardCSP
import math
import copy
from collections import deque


class BacktrackingSearch:

    def __init__(self):
        self.nodes_visited = 0

    def backtracking_search(self, csp, mrv, degree, lcv, ac3):
        assignment = [-1] * len(csp.variables)
        return self.backtrack(assignment, csp, mrv, degree, lcv, ac3)

    def backtrack(self, assignment, csp, mrv, degree, lcv, ac3):
        self.nodes_visited += 1                     # for each recursive call, increment nodes visited
        if self.complete_test(assignment):          # if assignment is complete then return assignment
            return assignment

        # grab unassigned variable based on var heuristics
        var = self.select_unassigned_variable(csp, assignment, mrv, degree)
        # get var's domain values in order based on LCV heuristic
        for val in self.order_domain_values(var, lcv, csp, assignment):
            # if value is consistent with assignment:
            if self.check_consistent(csp, var, val, assignment):
                assignment[var] = val
                # store csp.var_domains copy in case of restoration
                var_domains_copy = copy.deepcopy(csp.var_domains)
                # remove value from domain values of neighbors
                self.update_domains(csp, var, val)

                # execute arc-checking inference if switched and assign var's with only 1 val in domain
                if ac3:
                    if self.AC_3(csp):
                        for variable in csp.var_domains:
                            if len(csp.var_domains[variable]) == 1 and assignment[variable] == -1:
                                assignment[variable] = csp.var_domains[variable][0]

                # recursive call
                result = self.backtrack(assignment, csp, mrv, degree, lcv, ac3)
                # if result is not a failure:
                if result is not None:
                    return result
                # remove {var = value} and inferences from assignments
                assignment[var] = -1
                csp.var_domains = var_domains_copy

        # return failure
        return None

    # check if all variables have been assigned a value (not -1)
    def complete_test(self, assignment):
        for num in assignment:
            if num == -1:
                return False
        return True

    # return an unassigned variable using heuristics
    def select_unassigned_variable(self, csp, assignment, mrv, degree):
        # if no heuristics return first unassigned variable
        if not (mrv or degree):
            for i in range(len(assignment)):
                if assignment[i] == -1:
                    return i
        # otherwise, if MRV,
        elif mrv:
            return self.MRV_heuristic(csp, assignment, degree)

        # otherwise, do just degree
        return self.degree_heuristic(csp, assignment, csp.adj_list)

    # heuristic to return variable with most unassigned neighbors
    def degree_heuristic(self, csp, assignment, vars):
        max_var = None
        max_var_deg = -math.inf

        for var in vars:
            # count unassigned neighbors
            unassigned_neighbors = 0
            for neighbor in csp.adj_list[var]:
                if assignment[neighbor] == -1:
                    unassigned_neighbors += 1
            # if variable unassigned and degree greater than current max degree
            if assignment[var] == -1 and unassigned_neighbors > max_var_deg:
                max_var_deg = unassigned_neighbors
                max_var = var

        return max_var

    # heuristic to return variable with fewest values in its domain
    def MRV_heuristic(self, csp, assignment, degree):
        min_var_len = math.inf
        min_var = None
        # for each variable in variable domain dict
        for var in csp.var_domains:
            # if var unassigned and domain has fewer variables than that of min_var
            if assignment[var] == -1 and len(csp.var_domains[var]) < min_var_len:
                min_var_len = len(csp.var_domains[var])
                min_var = var
            # degree tiebreaker: if same MRV, return min_var with larger degree
            elif len(csp.var_domains[var]) == min_var_len and degree and assignment[var] == -1:
                min_var = self.degree_heuristic(csp, assignment, [var, min_var])

        return min_var

    # check consistency of a variable assignment using constraint map
    def check_consistent(self, csp, var, val, assignment):
        # if var or value doesn't exist
        if (var not in csp.variables) or (val not in csp.domain):
            return False

        # for each binary constraint
        for variables in csp.constraints:
            is_consistent = False

            # if var isn't in this binary set, skip
            if var not in variables:
                continue

            # grab indices in tuple of var and it's binary partner
            var_idx = variables.index(var)
            comp_idx = abs(var_idx - 1)

            # if partner variable not assigned yet, continue
            if assignment[variables[comp_idx]] == -1:
                continue

            # otherwise store partner variable assignment
            comp_val = assignment[variables[comp_idx]]

            # for (val1, val2) in constraint list, return False if inconsistent
            for values in csp.constraints[variables]:

                # if partner assignment and new var assignment pair is in constraint map, we know its consistent
                if comp_val == values[comp_idx] and values[var_idx] == val:
                    is_consistent = True

            # if consistent assignment not found, return False
            if not is_consistent:
                return False

        return True

    # heuristic to return ordered (or unordered) variable domain based on LCV or no LCV
    def order_domain_values(self, var, lcv, csp, assignment):
        if not lcv:
            return set(csp.var_domains[var])

        # otherwise, we wanna return a reordered list of that domain's values
        # ordered by how many of var's neighbors' domains val limits

        # map each var's val to num imposed constraints
        val_constraints = {}

        for val in csp.var_domains[var]:
            num_constraints = 0                 # number of constraints this value will impose on neighbors
            for neighbor in csp.adj_list[var]:
                # if neighbor is unassigned and has this value in its domain, increment num_constraints
                if assignment[neighbor] == -1 and val in csp.var_domains[neighbor]:
                    num_constraints += 1

            val_constraints[val] = num_constraints

        # get var's domain as a list sorted in increasing order by value's imposed constraint's on neighbors
        sorted_constraints = sorted(val_constraints, key=val_constraints.get)
        return sorted_constraints

    # remove val from domain of all neighbors of var
    def update_domains(self, csp, var, val):
        for neighbor in csp.adj_list[var]:
            if val in csp.var_domains[neighbor]:
                val_list = csp.var_domains[neighbor]
                val_list.remove(val)
                csp.var_domains[neighbor] = val_list

    # AC-3 Inference!
    def AC_3(self, csp):
        q = deque()

        # build queue of arcs in both directions for each pair of neighbors
        for var in csp.adj_list:
            for neighbor in csp.adj_list[var]:
                q.append((var, neighbor))

        while q:
            arc = q.popleft()               # remove first arc from queue -- (Xi, Xj)
            if self.revise(csp, arc):       # if arc imposes constraints on domains
                # if domain of Xi is empty, no solution so return false
                if len(csp.var_domains[arc[0]]) == 0:
                    return False

                # for each neighbor of Xi, append new arc between Xi and neighbor in both directions
                for neighbor in csp.adj_list[arc[0]]:
                    if neighbor != arc[1]:
                        q.append((neighbor, arc[0]))
                        q.append((arc[0], neighbor))
        return True

    # domain revision helper for AC-3
    def revise(self, csp, arc):
        revised = False
        # keep list of values in Xi's domain that constrain neighbors
        x_list = []

        for x in csp.var_domains[arc[0]]:
            # if no y_val in csp.var_domains[arc[1]] satisfies the constraint btw Xi and Xj
            temp = True
            for y in csp.var_domains[arc[1]]:
                # check (x, y) AND (y, x) presence in constraints
                if (arc[0], arc[1]) in csp.constraints:
                    if (x, y) in csp.constraints[(arc[0], arc[1])]:
                        temp = False
                elif (arc[1], arc[0]) in csp.constraints:
                    if (y, x) in csp.constraints[(arc[1], arc[0])]:
                        temp = False

            # if no y value satisfies the arc constraint, add x to be removed from Xi's domain
            if temp:
                x_list.append(x)
                revised = True

        # remove all x's in to-be-removed list from Xi's domain
        for x in x_list:
            csp.var_domains[arc[0]].remove(x)
        return revised
