# coding: utf-8
from __future__ import division, print_function
# When a player wants to make a move, they have to specify from which row they want to remove elements
# and how many elements they want to remove. They can't remove elements from an empty row or remove 0
# elements from any row. For example, given the board:

"""
Nim:
1: X X X X
2: X X X
3: X
4: X X
"""

# A player can remove 3 elements from the first row, which results in the following position:

"""
Nim:
1: X
2: X X X
3: X
4: X X
"""

# Please implement `make_move(board, row, elements)`, which will return a new board with `elements`
# number of elements removed from `row`th row, and will return the tuple `new_board, success`, which
# are respectively a list representing a new board position and a boolean indicating if the move was
# successful or not.

# If the move is illegal, the function should return an exact copy of the original board and indicate that
# the move was not successful.

# Pro tip: `another_list = some_list[:]` creates a fresh copy of any given list.

def make_move(board, row, elements):
    # Your code goes here!
    pass


# You can test your code locally using the following test case:
board = [1, 2, 3]
assert make_move(board, 1, 1) == ([0, 2, 3], True)
assert board == [1, 2, 3]

if __name__ == "__main__":
    import sys, json
    testcase = sys.stdin.read()
    testcase = json.loads(testcase)
    board = testcase["board"]
    row = testcase["row"]
    elements = testcase["elements"]
    print(json.dumps(make_move(board, row, elements)))
    assert board == testcase["board"]

# When you're finished, please submit the file to http://grader.givegrade.me.uk