# coding: utf-8
from __future__ import division, print_function
import random

# Please implement the function `optimal_move(board)`.
# If the board is in N-position `optimal_move(board)` should return a random valid move.
# If the board is in P-position `optimal_move(board)` should return a random optimal move, as
# discussed in the pdf file.
# You need not to worry about the special case of the empty board. We will make sure that the
# empty board never enters the `optimal_move` function.

# Pro tip: you can use `random.randint` to draw random numbers.

# Your solution to nim_sum goes here:
def nim_sum(board):
    if board:
        i = board[0]
        for j in board[1:]:
            i ^= j
        return i
    else:
        return 0

# Your solution to the task goes here:
def optimal_move(board):
    X = nim_sum(board)
    if X == 0:
        non_empty_rows = [i for i,r in enumerate(board) if r != 0]
        random.shuffle(non_empty_rows)
        row_index = non_empty_rows[0]
        return row_index + 1, random.randint(1, board[row_index])
    else:
        lengths = [X ^ i for i in board]
        computed = [(i, (a, n)) for i, (a, n) in enumerate(zip(lengths, board)) if a < n]
        random.shuffle(computed)
        to_return = computed[0]
        return to_return[0] + 1, to_return[1][1] - to_return[1][0]

# You can use the following test case to test your solution locally:
result = optimal_move([5, 4, 3, 2, 1])
assert any([result == (5, 1), result == (3, 1), result == (1, 1)])

# Note: due to technical limitations, there is no automated feedback for this exercise. It's
# up to you to make sure that your function behaves correctly. Ask your tutor if in doubt.