# coding: utf-8
from __future__ import division, print_function

# Warning: each exercise file waits for test input on the standard input. It might appear like your program is stuck in an infite loop but it probably isn't! This is to aid automatic marking, and you can remove everything after `__name__ == "__main__"` if you don't want to submit your code to http://grader.givegrade.me.uk.

# We will use a Python list to represent the current state of the Nim Board. The list will
# contain only information about the length of each row. Let us first write a function which
# will pretty-print the board. The expected behaviour of the function is as follows:

"""
>>> board = [5, 4, 5, 2, 3, 1]
>>> result = present_board(board)
>>> print(result)
>>> Nim:
1: X X X X X
2: X X X X
3: X X X X X
4: X X
5: X X X
6: X
"""

# Warning! `board` is not limited to a fixed size of 5 or 6. It can have any size between 1 and
# 10000 inclusive. All elements of `board` are non-negative integers.

# Pro tip: `"\n".join(["a", "b", "c"])` allows you to join multiple strings efficiently using
# new line as separator.

def present_board(board):
    # Your code goes here!
    pass

# You can test your code locally using the following test case:

assert(present_board([4, 3, 1, 2]) == "Nim:\n1: X X X X\n2: X X X\n3: X\n4: X X")

# The code below is needed for the automatic tester. Do not modify it.
# When you run the code it might seem like it's stuck in an infite loop. It isn't, it
# just waits for keyboard input.

# If you don't want to use automated feedback, just remove everything below this point.
if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass
    board = input("")
    board = [int(i) for i in board.split()]
    print(present_board(board))

# When you're finished, please submit the file to http://grader.givegrade.me.uk

# Before you submit:

# 1. Make sure you remove all dangling prints you've used for debugging, etc. Automatic tester doesn't like them!
# 2. Make sure your solution works in Python 2 (for the automated grader) as well as Python 3 (official course requirement).
# 3. The software used for automated feedback was originally developed for programming contests, and terminology might be somewhat confusing. When you log in to the website, find the name of the exercise you've done on the left pane, and press Submission. You can then choose a file from your filesystem and press Submit. Your code will be automatically tested for correctness.
