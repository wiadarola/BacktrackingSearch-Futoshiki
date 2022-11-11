#!/usr/bin/python3

"""
CS 4613
William Iadarola
Project 2: Futoshiki with Backtracking-Search
5/17/2021
"""

import argparse
from copy import deepcopy


def forward_check(csp, asgmts, var):
    """
    Fills csp with domain constraints based on assignments and inequalities.
    Takes and returns a deepcopied csp to avoid removal of values from single
    csp.
        Parameters: 
            csp: dict -> int locations and lists of illegal values
            asgmts: dict -> int locations and int assigned value
            var: int -> location of assigned value that causes new constraints
        Return:
            Bool: False for early detected failure, True otherwise
            csp: dict -> int : list (same as above)
    """
    # constraints for assigned values
    row = var // 6
    col = var % 6
    for i in range(6):
        if i+6*row != var:
            csp[i+6*row].append(asgmts[var])
        if 6*i+col != var:
            csp[6*i+col].append(asgmts[var])

    # constraints for inequalities
    if var in csp['<']:  # i < i+1
        for val in range(1, asgmts[var]):
            csp[var+1].append(val)
    if var-1 in csp['<']:  # i-1 < i
        for val in range(asgmts[var]+1, 7):
            csp[var-1].append(val)
    if var in csp['>']:  # i > i+1
        for val in range(asgmts[var]+1, 7):
            csp[var+1].append(val)
    if var-1 in csp['>']:  # i-1 > i
        for val in range(1, asgmts[var]):
            csp[var-1].append(val)
    if var in csp['v']:  # i > i+6
        for val in range(asgmts[var]+1, 7):
            csp[var+6].append(val)
    if var-6 in csp['v']:  # i-6 > i
        for val in range(1, asgmts[var]):
            csp[var-6].append(val)
    if var in csp['^']:  # i < i+6
        for val in range(1, asgmts[var]):
            csp[var+6].append(val)
    if var-6 in csp['^']:  # i-6 < i
        for val in range(asgmts[var]+1, 7):
            csp[var-6].append(val)

    # clear duplicates
    for i in range(6):
        csp[var] = list(set(csp[var]))
        if i+6*row != var: csp[i+6*row] = list(set(csp[i+6*row]))
        if 6*i+col != var: csp[6*i+col] = list(set(csp[6*i+col]))

    # check for early failure with 0 values for a variable
    for loc in range(36):
        if len(csp[loc]) == 6 and loc not in asgmts:
            return False, csp
    return True, csp


def backtracking_search(csp, asgmts):
    """
    Modifies assignments to find solution to Futoshiki game.
        Parameters:
            csp: dict -> int locations and lists of illegal values
            asgmts: dict -> int locations and int assigned value
        Return:
            Bool: False only for failure to find solution
            asgmts: dict -> completed assignment of game
    """
    if len(asgmts) == 36:  # if assignment is complete: exit
        return asgmts
    var = select_unnassigned_variable(csp, asgmts)
    for value in order_domain_values(csp, var):
        asgmts.update({var : value})
        success, inferences = forward_check(deepcopy(csp), asgmts, var)
        if success:  # didnt detect failure
            result = backtracking_search(inferences, asgmts)
            if isinstance(result, dict):
                return result
        # remove inferences from csp and var:value from asgmts
        asgmts.pop(var)
    return False # failure in branch


def select_unnassigned_variable(csp, asgmts):
    """
    Selects the next value to be assigned in search.
    Uses minimum remaining values heuristic and then degree heuristic.
    Arbitrarily chooses first item found if multiple locations have equal
    MRV's and degrees.
        Parameters:
            csp: dict -> int locations and lists of illegal values
            asgmts: dict -> int locations and int assigned value
        Return:
            int: location of the next variable to be assigned
    """
    # min remaining values
    vars = [(-1, 7)]
    for loc in csp.keys():
        if loc not in asgmts and isinstance(loc, int):
            if len(csp[loc]) == vars[0][1]: vars.append((loc, len(csp[loc])))
            elif len(csp[loc]) < vars[0][1]: vars = [(loc, len(csp[loc]))]

    # if res > 1: degree heuristic
    if len(vars) > 1:
        max = (-1, -1)
        for var in vars:
            var = var[0]
            degree, row, col = 0, var // 6, var % 6
            for i in range(6): # count vars current would constrain
                if i+6*row != var and i+6*row not in asgmts: degree += 1
                if 6*i+col != var and 6*i+col not in asgmts: degree += 1
            if degree > max[1]: max = (var, degree)
        return max[0]
    return vars[0][0]


def order_domain_values(csp, var):
    """
    Yields values in increasing order to be assigned in
    backtracking-search
    """
    for value in range(1, 7): 
        if value not in csp[var]: yield value


def get_file():
    """
    Retrieve file from command line.
        Return:
            Namespace object
    """
    parser = argparse.ArgumentParser(description='Solve 6x6 \
        Futoshiki with Backtracking-Search')
    parser.add_argument('filename', help='The file containing \
        initial assignments and inequalities, typically with .txt suffix')
    return parser.parse_args()


def parse_file(text):
    """
    Parse text file for initial data.
        Parameters:
            text: IO - text file to be parsed
        Return:
            assignment: dict(int, int) - index, value
            inequalities: dict(char, list(int)) - inequality, list of indices
    """
    lines = text.readlines()
    assignment = {}
    inequalities = { '<' : [], '>' : [], '^' : [], 'v' : [] }

    # These indices correspond to location of initial asgmts
    for i in range(6): 
        for j in range(0,12,2):
            if lines[i][j] != '0':
                assignment.update( { (j//2+6*i) : int(lines[i][j]) } )

    for i in range(7,13):  # These indices correspond to j and j+1 [<, >]
        for j in range(0,10,2):
            if lines[i][j] != '0':
                inequalities[lines[i][j]].append(j//2+6*(i-7))

    for i in range(14,19):  # These indices correspond to i & i-1 [v, ^]
        for j in range(0,12,2):
            if lines[i][j] != '0':
                inequalities[lines[i][j]].append(j//2+6*(i-14))

    text.close()
    return assignment, inequalities


def write(asgmts):
    """
    Write final assignments to created output.txt at location of program.
        Parameters:
            asgmts: dict(int, int) - index, value
    """
    with open('output.txt', 'w') as output: 
        if isinstance(asgmts, dict):
            for index in range(36):
                if index % 6 == 0 and index:
                    output.write('\n')
                output.write(str(asgmts[index]) + ' ')
        else: output.write("Failure")
    output.close()


def main():
    cmdline = get_file()
    asgmts, csp = parse_file(open(cmdline.filename))
    for var in range(36): csp.update( {var : []} )
    for var in asgmts: forward_check(csp, asgmts, var, asgmts[var])
    backtracking_search(csp, asgmts)
    write(asgmts) if len(asgmts) == 36 else write(False)


if __name__ == "__main__":
    main()
