from CircuitBoardCSP import CircuitBoardCSP
from backtrackingSearch import BacktrackingSearch

# parameters for basic circuit board (assignment ex)
comp_dict = {0: (7, 1), 1: (3, 2), 2: (5, 2), 3: (2, 3)}
width = 10
height = 3


# test 1: Given circuit board -- No Heuristics + No AC3
test_cb_CSP_1 = CircuitBoardCSP(comp_dict, width, height)
test_BT_1 = BacktrackingSearch()
assignment_1 = test_BT_1.backtracking_search(test_cb_CSP_1, mrv=False, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST1: CircuitBoardCSP w/ no Heuristics + no AC3-----------"
      "----------------------------------------")
print((str(test_cb_CSP_1.animate_board(assignment_1)) + "\nint form: " + str(assignment_1) + "\nNodes visited: "
       + str(test_BT_1.nodes_visited)))
print()


# test 2: Given circuit board -- Only MRV Heuristic + No AC3
test_cb_CSP_2 = CircuitBoardCSP(comp_dict, width, height)
test_BT_2 = BacktrackingSearch()
assignment_2 = test_BT_2.backtracking_search(test_cb_CSP_2, mrv=True, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST2: CircuitBoardCSP w/ only MRV Heuristic + no AC3------"
      "--------------------------------------")
print((str(test_cb_CSP_2.animate_board(assignment_2)) + "\nint form: " + str(assignment_2) + "\nNodes visited: "
       + str(test_BT_2.nodes_visited)))
print()


# test 3: Given circuit board -- Only Degree Heuristic + No AC3
test_cb_CSP_3 = CircuitBoardCSP(comp_dict, width, height)
test_BT_3 = BacktrackingSearch()
assignment_3 = test_BT_3.backtracking_search(test_cb_CSP_3, mrv=False, degree=True, lcv=False, ac3=False)
print("-----------------------------------------------------TEST3: CircuitBoardCSP w/ only Degree Heuristic + no AC3---"
      "--------------------------------------")
print((str(test_cb_CSP_3.animate_board(assignment_3)) + "\nint form: " + str(assignment_3) + "\nNodes visited: "
       + str(test_BT_3.nodes_visited)))
print()


# test 4: Given circuit board -- Only LCV Heuristic + No AC3
test_cb_CSP_4 = CircuitBoardCSP(comp_dict, width, height)
test_BT_4 = BacktrackingSearch()
assignment_4 = test_BT_4.backtracking_search(test_cb_CSP_4, mrv=False, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST4: CircuitBoardCSP w/ only LCV Heuristic + no AC3------"
      "--------------------------------------")
print((str(test_cb_CSP_4.animate_board(assignment_4)) + "\nint form: " + str(assignment_4) + "\nNodes visited: "
       + str(test_BT_4.nodes_visited)))
print()


# test 5: Given circuit board -- MRV and LCV Heuristics + No AC3
test_cb_CSP_5 = CircuitBoardCSP(comp_dict, width, height)
test_BT_5 = BacktrackingSearch()
assignment_5 = test_BT_5.backtracking_search(test_cb_CSP_5, mrv=True, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST5: CircuitBoardCSP w/ MRV and LCV Heuristics + no AC3--"
      "--------------------------------------")
print((str(test_cb_CSP_5.animate_board(assignment_5)) + "\nint form: " + str(assignment_5) + "\nNodes visited: "
       + str(test_BT_5.nodes_visited)))
print()


# test 6: Given circuit board -- Degree and LCV Heuristics + No AC3
test_cb_CSP_6 = CircuitBoardCSP(comp_dict, width, height)
test_BT_6 = BacktrackingSearch()
assignment_6 = test_BT_6.backtracking_search(test_cb_CSP_6, mrv=False, degree=True, lcv=True, ac3=False)
print("-----------------------------------------------------TEST6: CircuitBoardCSP w/ Degree and LCV Heuristics + "
      "no AC3-------------------------------------")
print((str(test_cb_CSP_6.animate_board(assignment_6)) + "\nint form: " + str(assignment_6) + "\nNodes visited: "
       + str(test_BT_6.nodes_visited)))
print()


# test 7: Given circuit board -- No Heuristics but w/ AC3
test_cb_CSP_7 = CircuitBoardCSP(comp_dict, width, height)
test_BT_7 = BacktrackingSearch()
assignment_7 = test_BT_7.backtracking_search(test_cb_CSP_7, mrv=False, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST7: CircuitBoardCSP No Heuristics but w/ AC3------------"
      "--------------------------------------")
print((str(test_cb_CSP_7.animate_board(assignment_7)) + "\nint form: " + str(assignment_7) + "\nNodes visited: "
       + str(test_BT_7.nodes_visited)))
print()


# test 8: Given circuit board -- MRV Heuristic w/ AC3
test_cb_CSP_8 = CircuitBoardCSP(comp_dict, width, height)
test_BT_8 = BacktrackingSearch()
assignment_8 = test_BT_8.backtracking_search(test_cb_CSP_8, mrv=True, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST8: CircuitBoardCSP MRV Heuristic w/ AC3----------------"
      "--------------------------------------")
print((str(test_cb_CSP_8.animate_board(assignment_8)) + "\nint form: " + str(assignment_8) + "\nNodes visited: "
       + str(test_BT_8.nodes_visited)))
print()


# test 9: Given circuit board -- Degree Heuristic w/ AC3
test_cb_CSP_9 = CircuitBoardCSP(comp_dict, width, height)
test_BT_9 = BacktrackingSearch()
assignment_9 = test_BT_9.backtracking_search(test_cb_CSP_9, mrv=False, degree=True, lcv=False, ac3=True)
print("-----------------------------------------------------TEST9: CircuitBoardCSP Degree Heuristic w/ AC3-------------"
      "--------------------------------------")
print((str(test_cb_CSP_9.animate_board(assignment_9)) + "\nint form: " + str(assignment_9) + "\nNodes visited: "
       + str(test_BT_9.nodes_visited)))
print()


# test 10: Given circuit board -- LCV Heuristic w/ AC3
test_cb_CSP_10 = CircuitBoardCSP(comp_dict, width, height)
test_BT_10 = BacktrackingSearch()
assignment_10 = test_BT_10.backtracking_search(test_cb_CSP_10, mrv=False, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST10: CircuitBoardCSP LCV Heuristic w/ AC3---------------"
      "--------------------------------------")
print((str(test_cb_CSP_10.animate_board(assignment_10)) + "\nint form: " + str(assignment_10) +
       "\nNodes visited: " + str(test_BT_10.nodes_visited)))
print()


# test 11: Given circuit board -- MRV + LCV Heuristics w/ AC3
test_cb_CSP_11 = CircuitBoardCSP(comp_dict, width, height)
test_BT_11 = BacktrackingSearch()
assignment_11 = test_BT_11.backtracking_search(test_cb_CSP_11, mrv=True, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST11: CircuitBoardCSP MRV + LCV Heuristics w/ AC3--------"
      "--------------------------------------")
print((str(test_cb_CSP_11.animate_board(assignment_11)) + "\nint form: " + str(assignment_11) +
       "\nNodes visited: " + str(test_BT_11.nodes_visited)))
print()


# test 12: Given circuit board -- Degree + LCV Heuristics w/ AC3
test_cb_CSP_12 = CircuitBoardCSP(comp_dict, width, height)
test_BT_12 = BacktrackingSearch()
assignment_12 = test_BT_12.backtracking_search(test_cb_CSP_12, mrv=False, degree=True, lcv=True, ac3=True)
print("-----------------------------------------------------TEST12: CircuitBoardCSP Degree + LCV Heuristics w/ AC3-----"
      "--------------------------------------")
print((str(test_cb_CSP_12.animate_board(assignment_12)) + "\nint form: " + str(assignment_12) +
       "\nNodes visited: " + str(test_BT_12.nodes_visited)))
print()


# parameters for my own more complicated circuit board (assignment ex)
# ggfffff.ddddd
# ggfffff.ddddd
# eefffffbbbbbb
# eeh.cccbbbbbb
# eeh.cccbbbbbb
# aaaaaaabbbbbb

comp_dict_2 = {0: (7, 1), 1: (6, 4), 2: (3, 2), 3: (5, 2), 4: (2, 3), 5: (5, 3), 6: (2, 2)}
width_2 = 13
height_2 = 6


# test 13: My own circuit board -- MRV + LCV Heuristics w/ AC3
test_cb_CSP_13 = CircuitBoardCSP(comp_dict_2, width_2, height_2)
test_BT_13 = BacktrackingSearch()
assignment_13 = test_BT_13.backtracking_search(test_cb_CSP_13, mrv=True, degree=False, lcv=True, ac3=True)
print("-----------------------------------------------------TEST13: CircuitBoardCSP MRV + LCV Heuristics w/ AC3--------"
      "--------------------------------------")
print((str(test_cb_CSP_13.animate_board(assignment_13)) + "\nint form: " + str(assignment_13) +
       "\nNodes visited: " + str(test_BT_13.nodes_visited)))
print()


# test 14: My own circuit board -- MRV + LCV Heuristics, no AC3
test_cb_CSP_14 = CircuitBoardCSP(comp_dict_2, width_2, height_2)
test_BT_14 = BacktrackingSearch()
assignment_14 = test_BT_14.backtracking_search(test_cb_CSP_14, mrv=True, degree=False, lcv=True, ac3=False)
print("-----------------------------------------------------TEST14: CircuitBoardCSP MRV + LCV Heuristics, no AC3-------"
      "--------------------------------------")
print((str(test_cb_CSP_14.animate_board(assignment_14)) + "\nint form: " + str(assignment_14) +
       "\nNodes visited: " + str(test_BT_14.nodes_visited)))
print()


# test 15: My own circuit board -- No Heuristics, but w/ AC3
test_cb_CSP_15 = CircuitBoardCSP(comp_dict_2, width_2, height_2)
test_BT_15 = BacktrackingSearch()
assignment_15 = test_BT_15.backtracking_search(test_cb_CSP_15, mrv=False, degree=False, lcv=False, ac3=True)
print("-----------------------------------------------------TEST15: CircuitBoardCSP No Heuristics, but w/ AC3----------"
      "--------------------------------------")
print((str(test_cb_CSP_15.animate_board(assignment_15)) + "\nint form: " + str(assignment_15) +
       "\nNodes visited: " + str(test_BT_15.nodes_visited)))
print()


# test 16: My own circuit board -- No Heuristics, no AC3
test_cb_CSP_16 = CircuitBoardCSP(comp_dict_2, width_2, height_2)
test_BT_16 = BacktrackingSearch()
assignment_16 = test_BT_16.backtracking_search(test_cb_CSP_16, mrv=False, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST16: CircuitBoardCSP No Heuristics and no AC3----------"
      "--------------------------------------")
print((str(test_cb_CSP_16.animate_board(assignment_16)) + "\nint form: " + str(assignment_16) +
       "\nNodes visited: " + str(test_BT_16.nodes_visited)))
print()


# test 17: My own circuit board -- Only MRV Heuristic, no AC3
test_cb_CSP_17 = CircuitBoardCSP(comp_dict_2, width_2, height_2)
test_BT_17 = BacktrackingSearch()
assignment_17 = test_BT_17.backtracking_search(test_cb_CSP_17, mrv=True, degree=False, lcv=False, ac3=False)
print("-----------------------------------------------------TEST17: CircuitBoardCSP Only MRV Heuristic and no AC3------"
      "--------------------------------------")
print((str(test_cb_CSP_17.animate_board(assignment_17)) + "\nint form: " + str(assignment_17) +
       "\nNodes visited: " + str(test_BT_17.nodes_visited)))
print()
