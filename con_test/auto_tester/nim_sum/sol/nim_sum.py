# Please implement `nim_sum(board)` to compute the nim sum of a given board position.
# Please implement `is_n_position(board)` to determine whether the given board is in N-position.
# Please implement `is_p_position(board)` to determine whether the given board is in P-position.

# Please refer to the pdf document if you're not sure what nim sum, N-position or P-position are.

# From now on, please feel free to use python's built-in exclusive or `^`, but if prefer, you can
# copy and paste functions you've defined previously.

def nim_sum(board):
    if board:
        i = board[0]
        for j in board[1:]:
            i ^= j
        return i
    else:
        return 0

def is_n_position(board):
    return nim_sum(board) == 0

def is_p_position(board):
    return nim_sum(board) != 0

# You can test your solution locally using this test case:

assert nim_sum([5, 4, 3, 2, 1]) == 1

if __name__ == "__main__":
    import json, sys
    testcase = json.loads(sys.stdin.read())
    if testcase["type"] == "nim_sum":
        print(json.dumps(nim_sum(testcase["input"])))
    if testcase["type"] == "is_n_position":
        print(json.dumps(is_n_position(testcase["input"])))
    if testcase["type"] == "is_p_position":
        print(json.dumps(is_p_position(testcase["input"])))