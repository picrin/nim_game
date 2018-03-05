## Fully working game

# Please implement a fully working game of Nim. It's up to you how you achieve this.
# Command line is fine, but feel free to use Tkinter, Canvas, or even web programming or virtual reality (if you're adventurous)! 

# You can re-use any function defined so far.

# There's no automated feedback for this exercise.

# Regardless of how you deliver the final solution your program should:

# 1. Allow the players to choose any of the 3 required scenarios: Human vs Human, Human
#    vs Computer, Computer vs Computer.
# 2. Allow human players to enter user input (which row and how many elements).
# 3. Make computer players execute optimal strategy.
# 4. Change turns, but ONLY if the player made a legal move (give some meaningful error
#    message/ allow for input retry).
# 5. Announce the winner when the board is empty.

# If you decide to follow the path of least resistance, you can implement a fairly decent
# command line interface re-using existing modules in about 20 lines of code.

from present_board import *
from ui import *
from optimal_move import *
from make_move import *

def play_nim(player1, player2, board):
    # Your code goes here, or feel free to use any another method signature/ technology to
    # Sbuild the final product
    pass

# Can you beat Clever Computer?
you = "Put your name here"
computer = "Clever Computer"
print("I challenge you mighty", you, "for a duel of Nim!")
play_nim(you, computer, [5, 4, 3, 2, 1])