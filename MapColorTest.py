from MapColorCSP import MapColorCSP
from backtrackingSearch import BacktrackingSearch


# parameters for Normal AUS Map with RGB colors + MapColorCSP for these parameters
variables = [0, 1, 2, 3, 4, 5, 6]      # WA : 0, NT: 1, SA: 2, Q: 3, NSW: 4, V: 5, T:6
domain = [0, 1, 2]                     # r, g, b
adj_list = {0: [1, 2], 1: [0, 2, 3], 2: [0, 1, 3, 4, 5], 3: [1, 2, 4], 4: [2, 3, 5], 5: [2, 4], 6: []}


# test 1: Normal Map (AUS) -- No Heuristics + No AC3
test_map_CSP_1 = MapColorCSP(variables, domain, adj_list)
test_BT_1 = BacktrackingSearch()
assignment_1 = test_BT_1.backtracking_search(test_map_CSP_1, mrv=False, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST1: MapColorCSP w/ no Heuristics + no AC3-------------"
      "----------------------------------------")
print((str(test_map_CSP_1.display_assignment(assignment_1)) + "\nint form: " + str(assignment_1) + "\nNodes visited: "
       + str(test_BT_1.nodes_visited)))
print()


# test 2: Normal Map (AUS) -- Only MRV Heuristic + No AC3
test_map_CSP_2 = MapColorCSP(variables, domain, adj_list)
test_BT_2 = BacktrackingSearch()
assignment_2 = test_BT_2.backtracking_search(test_map_CSP_2, mrv=True, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST2: MapColorCSP w/ only MRV Heuristic + no AC3----------"
      "--------------------------------------")
print((str(test_map_CSP_2.display_assignment(assignment_2)) + "\nint form: " + str(assignment_2) + "\nNodes visited: "
       + str(test_BT_2.nodes_visited)))
print()


# test 3: Normal Map (AUS) -- Only Degree Heuristic + No AC3
test_map_CSP_3 = MapColorCSP(variables, domain, adj_list)
test_BT_3 = BacktrackingSearch()
assignment_3 = test_BT_3.backtracking_search(test_map_CSP_3, mrv=False, degree=True, lcv=False, ac3=False)
print("-----------------------------------------------------TEST3: MapColorCSP w/ only Degree Heuristic + no AC3-------"
      "--------------------------------------")
print((str(test_map_CSP_3.display_assignment(assignment_3)) + "\nint form: " + str(assignment_3) + "\nNodes visited: "
       + str(test_BT_3.nodes_visited)))
print()


# test 4: Normal Map (AUS) -- Only LCV Heuristic + No AC3
test_map_CSP_4 = MapColorCSP(variables, domain, adj_list)
test_BT_4 = BacktrackingSearch()
assignment_4 = test_BT_4.backtracking_search(test_map_CSP_4, mrv=False, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST4: MapColorCSP w/ only LCV Heuristic + no AC3----------"
      "--------------------------------------")
print((str(test_map_CSP_4.display_assignment(assignment_4)) + "\nint form: " + str(assignment_4) + "\nNodes visited: "
       + str(test_BT_4.nodes_visited)))
print()


# test 5: Normal Map (AUS) -- MRV and LCV Heuristics + No AC3
test_map_CSP_5 = MapColorCSP(variables, domain, adj_list)
test_BT_5 = BacktrackingSearch()
assignment_5 = test_BT_5.backtracking_search(test_map_CSP_5, mrv=True, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST5: MapColorCSP w/ MRV and LCV Heuristics + no AC3------"
      "--------------------------------------")
print((str(test_map_CSP_5.display_assignment(assignment_5)) + "\nint form: " + str(assignment_5) + "\nNodes visited: "
       + str(test_BT_5.nodes_visited)))
print()


# test 6: Normal Map (AUS) -- MRV + Degree and LCV Heuristics + No AC3
test_map_CSP_6 = MapColorCSP(variables, domain, adj_list)
test_BT_6 = BacktrackingSearch()
assignment_6 = test_BT_6.backtracking_search(test_map_CSP_6, mrv=True, degree=True, lcv=True, ac3=False)
print("--------------------------------------------------TEST6: MapColorCSP w/ MRV + Degree and LCV Heuristics + no AC3"
      "-----------------------------------------")
print((str(test_map_CSP_6.display_assignment(assignment_6)) + "\nint form: " + str(assignment_6) + "\nNodes visited: "
       + str(test_BT_6.nodes_visited)))
print()


# test 7: Normal Map (AUS) -- No Heuristics but w/ AC3
test_map_CSP_7 = MapColorCSP(variables, domain, adj_list)
test_BT_7 = BacktrackingSearch()
assignment_7 = test_BT_7.backtracking_search(test_map_CSP_7, mrv=False, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST7: MapColorCSP No Heuristics but w/ AC3----------------"
      "--------------------------------------")
print((str(test_map_CSP_7.display_assignment(assignment_7)) + "\nint form: " + str(assignment_7) + "\nNodes visited: "
       + str(test_BT_7.nodes_visited)))
print()


# test 8: Normal Map (AUS) -- MRV Heuristic w/ AC3
test_map_CSP_8 = MapColorCSP(variables, domain, adj_list)
test_BT_8 = BacktrackingSearch()
assignment_8 = test_BT_8.backtracking_search(test_map_CSP_8, mrv=True, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST8: MapColorCSP MRV Heuristic w/ AC3--------------------"
      "--------------------------------------")
print((str(test_map_CSP_8.display_assignment(assignment_8)) + "\nint form: " + str(assignment_8) + "\nNodes visited: "
       + str(test_BT_8.nodes_visited)))
print()


# test 9: Normal Map (AUS) -- Degree Heuristic w/ AC3
test_map_CSP_9 = MapColorCSP(variables, domain, adj_list)
test_BT_9 = BacktrackingSearch()
assignment_9 = test_BT_9.backtracking_search(test_map_CSP_9, mrv=False, degree=True, lcv=False, ac3=True)
print("-----------------------------------------------------TEST9: MapColorCSP Degree Heuristic w/ AC3-----------------"
      "--------------------------------------")
print((str(test_map_CSP_9.display_assignment(assignment_9)) + "\nint form: " + str(assignment_9) + "\nNodes visited: "
       + str(test_BT_9.nodes_visited)))
print()


# test 10: Normal Map (AUS) -- LCV Heuristic w/ AC3
test_map_CSP_10 = MapColorCSP(variables, domain, adj_list)
test_BT_10 = BacktrackingSearch()
assignment_10 = test_BT_10.backtracking_search(test_map_CSP_10, mrv=False, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST10: MapColorCSP LCV Heuristic w/ AC3-------------------"
      "--------------------------------------")
print((str(test_map_CSP_10.display_assignment(assignment_10)) + "\nint form: " + str(assignment_10) +
       "\nNodes visited: " + str(test_BT_10.nodes_visited)))
print()


# test 11: Normal Map (AUS) -- MRV + LCV Heuristics w/ AC3
test_map_CSP_11 = MapColorCSP(variables, domain, adj_list)
test_BT_11 = BacktrackingSearch()
assignment_11 = test_BT_11.backtracking_search(test_map_CSP_11, mrv=True, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST11: MapColorCSP MRV + LCV Heuristics w/ AC3------------"
      "--------------------------------------")
print((str(test_map_CSP_11.display_assignment(assignment_11)) + "\nint form: " + str(assignment_11) +
       "\nNodes visited: " + str(test_BT_11.nodes_visited)))
print()


# test 12: Normal Map (AUS) -- MRV + Degree + LCV Heuristics w/ AC3
test_map_CSP_12 = MapColorCSP(variables, domain, adj_list)
test_BT_12 = BacktrackingSearch()
assignment_12 = test_BT_12.backtracking_search(test_map_CSP_12, mrv=True, degree=True, lcv=True, ac3=True)
print("-----------------------------------------------------TEST12: MapColorCSP MRV + Degree + LCV Heuristics w/ AC3---"
      "--------------------------------------")
print((str(test_map_CSP_12.display_assignment(assignment_12)) + "\nint form: " + str(assignment_12) +
       "\nNodes visited: " + str(test_BT_12.nodes_visited)))
print()


# new parameters for Map of US with four colors (R G B Y) + MapColorCSP
adj_list_2 = {
    0: [],
    1: [25, 42, 10, 9],
    2: [24, 42, 25, 18, 43, 36],
    3: [4, 33, 44, 5, 32],
    4: [37, 33, 3],
    5: [50, 29, 16, 36, 32, 3, 44],
    6: [34, 19, 39],
    7: [20, 45],
    8: [20, 38, 31],
    9: [1, 10],
    10: [9, 1, 42, 27, 40],
    11: [],
    12: [23, 48, 14, 24, 29, 41],
    13: [26, 50, 44, 33, 37, 47],
    14: [15, 17, 24, 12, 48],
    15: [22, 35, 17, 14],
    16: [29, 24, 36, 5],
    17: [15, 35, 49, 45, 42, 24, 14],
    18: [43, 2, 25],
    19: [39, 6, 34, 30, 46],
    20: [45, 49, 38, 7, 8],
    21: [30],
    22: [48, 15, 35],
    23: [48, 12, 41, 28],
    24: [12, 14, 17, 42, 2, 36, 16, 29],
    25: [18, 2, 42, 1],
    26: [28, 41, 50, 13],
    27: [45, 42, 10, 40],
    28: [23, 41, 26],
    29: [41, 12, 24, 16, 5, 50],
    30: [46, 21, 19],
    31: [8, 38, 34],
    32: [3, 44, 5, 36, 43],
    33: [13, 44, 3, 4, 37],
    34: [31, 38, 46, 19, 6],
    35: [38, 49, 17, 15, 22],
    36: [16, 24, 2, 43, 32, 5],
    37: [4, 33, 13, 47],
    38: [34, 31, 8, 20, 49, 35],
    39: [6, 19],
    40: [10, 27],
    41: [28, 23, 12, 29, 50, 26],
    42: [17, 45, 27, 10, 1, 25, 2, 24],
    43: [32, 36, 2, 18],
    44: [13, 50, 5, 32, 3, 33],
    45: [27, 42, 17, 49, 20, 7],
    46: [34, 30, 19],
    47: [13, 37],
    48: [22, 23, 12, 14],
    49: [35, 38, 20, 45, 17],
    50: [26, 41, 29, 5, 44, 13],
}
variables_2 = list(adj_list_2.keys())
domain_2 = [0, 1, 2, 3]


# test 13: US Map -- MRV + LCV Heuristics + AC3
test_map_CSP_13 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_13 = BacktrackingSearch()
assignment_13 = test_BT_13.backtracking_search(test_map_CSP_13, mrv=True, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST13: US! MapColorCSP w/ MRV + LCV Heuristics + AC3------"
      "--------------------------------------")
print("int form: " + str(assignment_13) + "\nNodes visited: " + str(test_BT_13.nodes_visited))
print()


# test 14: US Map -- No Heuristics + AC3
test_map_CSP_14 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_14 = BacktrackingSearch()
assignment_14 = test_BT_14.backtracking_search(test_map_CSP_14, mrv=False, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST14: US! MapColorCSP w/ No Heuristics + AC3-------------"
      "--------------------------------------")
print("int form: " + str(assignment_14) + "\nNodes visited: " + str(test_BT_14.nodes_visited))
print()


# test 15: US Map -- MRV + LCV Heuristics + No AC3
test_map_CSP_15 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_15 = BacktrackingSearch()
assignment_15 = test_BT_15.backtracking_search(test_map_CSP_15, mrv=True, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST15: US! MapColorCSP w/ MRV + LCV Heuristics + No AC3---"
      "--------------------------------------")
print("int form: " + str(assignment_15) + "\nNodes visited: " + str(test_BT_15.nodes_visited))
print()


# test 16: US Map -- No Heuristics + No AC3
test_map_CSP_16 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_16 = BacktrackingSearch()
assignment_16 = test_BT_16.backtracking_search(test_map_CSP_16, mrv=False, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST16: US! MapColorCSP w/ No Heuristics + No AC3----------"
      "--------------------------------------")
print("int form: " + str(assignment_16) + "\nNodes visited: " + str(test_BT_16.nodes_visited))
print()


# test 17: US Map -- Only MRV Heuristic + AC3
test_map_CSP_17 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_17 = BacktrackingSearch()
assignment_17 = test_BT_17.backtracking_search(test_map_CSP_17, mrv=True, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST17: US! MapColorCSP w/ Only MRV Heuristic + No AC3-----"
      "--------------------------------------")
print("int form: " + str(assignment_17) + "\nNodes visited: " + str(test_BT_17.nodes_visited))
print()


# test 18: US Map -- Only Degree Heuristic + AC3
test_map_CSP_18 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_18 = BacktrackingSearch()
assignment_18 = test_BT_18.backtracking_search(test_map_CSP_18, mrv=False, degree=True, lcv=False, ac3=True)
print("-----------------------------------------------------TEST18: US! MapColorCSP w/ Only Degree Heuristic + AC3-----"
      "--------------------------------------")
print("int form: " + str(assignment_18) + "\nNodes visited: " + str(test_BT_18.nodes_visited))
print()


# test 19: US Map -- Only LCV Heuristic + AC3
test_map_CSP_19 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_19 = BacktrackingSearch()
assignment_19 = test_BT_19.backtracking_search(test_map_CSP_19, mrv=False, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST19: US! MapColorCSP w/ Only LCV Heuristic + AC3--------"
      "--------------------------------------")
print("int form: " + str(assignment_19) + "\nNodes visited: " + str(test_BT_19.nodes_visited))
print()


# test 20: US Map -- Degree + LCV Heuristics + AC3
test_map_CSP_20 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_20 = BacktrackingSearch()
assignment_20 = test_BT_20.backtracking_search(test_map_CSP_20, mrv=False, degree=True, lcv=True, ac3=True)
print("-----------------------------------------------------TEST20: US! MapColorCSP w/ Degree + LCV Heuristic + AC3----"
      "--------------------------------------")
print("int form: " + str(assignment_20) + "\nNodes visited: " + str(test_BT_20.nodes_visited))
print()


# test 21: US Map -- MRV + Degree + LCV Heuristics + AC3
test_map_CSP_21 = MapColorCSP(variables_2, domain_2, adj_list_2)
test_BT_21 = BacktrackingSearch()
assignment_21 = test_BT_21.backtracking_search(test_map_CSP_21, mrv=True, degree=True, lcv=True, ac3=True)
print("-----------------------------------------------TEST21: US! MapColorCSP w/ MRV + Degree + LCV Heuristics + AC3---"
      "--------------------------------------------")
print("int form: " + str(assignment_21) + "\nNodes visited: " + str(test_BT_21.nodes_visited))
print()
