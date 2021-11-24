# Author: Nick Irwin
# Course: COSC76 (21F)
# Purpose: CircuitBoardCSP class. Takes in board variables (components dict mapping each component to its size),
#          and the dimensions of the actual board itself.
#          Builds a binary constraint map of variables and their assignments.


class CircuitBoardCSP:

    def __init__(self, components_dict, board_width, board_height):
        # initialize board data
        self.components_dict = components_dict      # given components_dict as width and height for each component
        self.board_width = board_width              # -- components_dict = { 0: (w0, h0), 1: (w1, h1), ... }
        self.board_height = board_height

        # create list of variables which is just a list of each component number starting w/ zero: [0, 1, 2, ...]
        self.variables = []
        for component in components_dict:
            self.variables.append(component)

        # create domain which is just all the positions on the board
        self.domain = set()                         # { (0, 0), (0, 1), ..., (w-2, h-2), (w-1, h-1) }
        for x in range(board_width):
            for y in range(board_height):
                self.domain.add((x, y))

        # build var_domains which is a dict that holds a set of legal bottom left positions for each component
        # { 0 : [(x1, y1), (x2, y2), ...]
        self.var_domains = {}
        self.build_var_domains()

        # build adjacency list dict. In this case, each component is neighbors with every other component
        self.adj_list = {}
        self.build_adj_list()

        # build constraint map
        self.constraints = {}                       # constraints = { (0, 1): [((x0, y0), (x1, y1)), ] ..., }
        self.make_constraints()

    # build domain for each variable
    def build_var_domains(self):
        # for each component
        for var in self.variables:
            self.var_domains[var] = set()
            # for each spot (x, y) in domain,
            for spot in self.domain:
                x_c = spot[0]
                y_c = spot[1]
                # if component fits on board (does not exceed right edge or top edge), add spot to component's domain
                if (x_c + self.components_dict[var][0] <= self.board_width) \
                        and (y_c + self.components_dict[var][1] <= self.board_height):
                    self.var_domains[var].add((x_c, y_c))

    # build simple adj list dict
    def build_adj_list(self):
        # for each variable
        for var in self.variables:
            # variable's adjacency list is list of all other variables
            temp_list = list(self.variables)
            temp_list.remove(var)
            self.adj_list[var] = temp_list

    # build constraints dict which maps a variable and a neighbor to all their allowed positions
    # key: tuple (var, neigh)
    # value: list of tuple of tuples [ ((x_v0, y_v0), (x_n0, y_n0)), ((x_v1, y_v1), (x_n1, y_n1)), ... ]
    # constraints = { (0, 1): [ ((x0, y0), (x1, y1)), ...] ...}
    def make_constraints(self):
        # for every variable and each of its neighbors
        for variable in self.adj_list:
            for neighbor in self.adj_list[variable]:
                # create empty set of constraints and fill with a tuples of tuples ((var_x, var_y), (nei_x, nei_y))
                self.constraints[(variable, neighbor)] = set()

                # for each location in variable's domain,
                for v_loc in self.var_domains[variable]:
                    # for each location in neighbor's domain,
                    for n_loc in self.var_domains[neighbor]:

                        # we know these two locations have to be on the board because we created var_domains earlier
                        # if variable and neighbor at these locations do not overlap,
                        if self.no_overlap(variable, neighbor, v_loc, n_loc):           # helper function for overlap
                            # add (v_loc, n_loc) to my constraints for (variable, neighbor)
                            self.constraints[(variable, neighbor)].add((v_loc, n_loc))

    # given two variables and location assignments,
    # check that the components do not overlap
    def no_overlap(self, variable, neighbor, v_loc, n_loc):
        x_n = n_loc[0]      # bottom left x coordinate of neighbor
        y_n = n_loc[1]      # bottom left y coordinate of neighbor
        x_v = v_loc[0]      # bottom left x coordinate of variable
        y_v = v_loc[1]      # bottom left y coordinate of variable

        n_width = self.components_dict[neighbor][0]
        n_height = self.components_dict[neighbor][1]

        v_width = self.components_dict[variable][0]
        v_height = self.components_dict[variable][1]

        # if neighbor is left of var, neighbor is right of var, neighbor is below var, or neighbor is above var
        if x_n + n_width <= x_v or x_n >= x_v + v_width or y_n + n_height <= y_v or y_n >= y_v + v_height:
            return True

        # otherwise, components must overlap
        return False

    # assignment = [ (x0, y0), (x1, y1), ..., (xn, yn) ]
    # given an assignment, animate the populated board starting with var 0= 'a', 1= 'b', ...
    def animate_board(self, assignment):

        # map coordinates (x, y) to variable assignment
        coordinates = {}

        # for each component + assigned location
        for i in range(len(assignment)):

            # for every spot (x, y) that component covers,
            for x in range(assignment[i][0], assignment[i][0] + self.components_dict[i][0]):

                for y in range(assignment[i][1], assignment[i][1] + self.components_dict[i][1]):

                    coordinates[(x, y)] = chr(ord('a') + i)

        s = "board result: \n"
        # go through every (x, y) coordinate in board
        # (0, 0) bottom left so reverse y order
        for y in range(self.board_height-1, -1, -1):
            for x in range(self.board_width):
                # append the variable assignment at that point, if unassigned, just put "."
                s += str(coordinates.get((x, y), "."))

            # newline
            s += "\n"

        return s


test_cb_CSP = CircuitBoardCSP({0: (3, 2), 1: (5, 2), 2: (2, 3), 3: (7, 1)}, 10, 3)
# print(test_cb_CSP.var_domains)
# print(test_cb_CSP.adj_list)
print(test_cb_CSP.constraints)
