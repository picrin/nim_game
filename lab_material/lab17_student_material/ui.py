# In our implementation of the game of Nim we would like to support 3 scenarios:

# 1. Human vs Human
# 2. Human vs Computer
# 3. Computer vs Computer

# One way to decide, which scenario our users want to engage in, would be based on
# case-insenstive inspection of player's names. If player's name contains the string
# "computer" in it, as for example in "Computer 1", we could treat them as a computer
# player and make optimal moves based on the optimal strategy. Otherwise, we will treat
# them as human players and gather their input using keyboard, mouse, VR headset, etc.

# Please implement this logic in `is_human(player_string)`

# Pro tip: use `.lower()` for case-insensitive comparisons. For example
# `"apple" in "bAnANA ApPLe RaspbERRY".lower()`

def is_human(player_string):
    # Your code goes here!
    pass

# We have to be able to correctly recognise the terminal position. In Nim the only possible
# terminal position is the empty board, for example `[0, 0, 0]`. Please implement
# `is_board_empty(board)`, which recognises the empty board.

def is_board_empty(board):
    # Your code goes here!
    pass

if __name__ == "__main__":
    import json, sys
    testcase = json.loads(sys.stdin.read())
    if testcase["type"] == "is_human":
        print(json.dumps(is_human(testcase["input"])))
    if testcase["type"] == "is_board_empty":
        print(json.dumps(is_board_empty(testcase["input"])))