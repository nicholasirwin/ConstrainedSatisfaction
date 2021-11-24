# Author: Nick Irwin
# Course: COSC76 (21F)
# Purpose: MapColorCSP class. Takes in map variables (states), values (colors), and adj_list of bordering states.
#          Builds a binary constraint map of variables and their assignments.


class MapColorCSP:

    def __init__(self, variables, domain, adj_list):
        self.variables = variables  # [0, 1, 2, 3, 4, 5, 6]  ----  WA: 0, NT: 1, SA: 2, Q: 3, NSW: 4, V: 5, T:6
        self.domain = domain  # [0, 1, 2]  ----  [r, g, b]
        self.adj_list = adj_list  # {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3, 4, 5], ..., 6: []}

        # make a set of pairs of values for constraint map
        self.color_pairs = set()
        self.make_pairs()

        # we need an edge list dictionary for binary constraints: {"WA" : ["NT", "SA"], "NT" : ["WA", "SA", "Q"] ...}
        self.constraints = {}  # { (WA, SA) : {(r, g), (r, b), (g, r), ...}  }
        self.make_constraints()

        # build a dictionary mapping variables to their domain
        self.var_domains = {}
        for variable in self.variables:
            self.var_domains[variable] = list(self.domain)

    # generate a pairs tuple for all possible two state color combos { (r, g), (r, b), (g, r), ... }
    def make_pairs(self):
        for color1 in self.domain:
            for color2 in self.domain:
                if color1 != color2:
                    self.color_pairs.add((color1, color2))

    # build constraint map for neighboring variables
    def make_constraints(self):
        # for each variable
        for variable in self.adj_list:
            # for each neighbor of this variable
            for neighbor in self.adj_list[variable]:
                # add binary constraint
                if (variable, neighbor) and (neighbor, variable) not in self.constraints:
                    self.constraints[(variable, neighbor)] = self.color_pairs.copy()

    # output actual state names + colors. only for the Australia specific map with R G B
    def display_assignment(self, assignment):
        territories = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
        colors = ["r", "g", "b"]
        res = {}
        for i in range(len(assignment)):
            res[territories[i]] = colors[self.domain[assignment[i]]]
        return res


# test_map_CSP = MapColorCSP()
# print(test_map_CSP.constraints)

# variables1 = ["WA", "NT", "SA", "Q", "NSW", "V", "T"]
# domain1 = ["r", "g", "b"]
# adj_list = {"WA" : ["NT", "SA"], "NT" : ["WA", "SA", "Q"], "SA" : ["WA", "NT", "Q", "NSW", "V"],
# "Q" : ["NT", "SA", "NSW"], "NSW" : ["SA", "Q", "V"], "V" : ["SA", "NSW"], "T" : []}
# test_map_CSP = MapColorCSP(variables1, domain1, adj_list)
# print(test_map_CSP.constraints)
