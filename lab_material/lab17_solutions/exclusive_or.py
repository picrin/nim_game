# coding: utf-8
from __future__ import division, print_function
#The algorithm to optimally play the game of Nim uses bitwise exclusive-or to work.

#Before we understand how that works, we have to implement exclusive-or as a logic gate.

#Exclusive-or logic gates (XOR gates) work with two inputs, where each input can take either of two values: 0 or 1. That's why there are only four possible ways to use a XOR gate:

#exclusive_or(0, 0) → 0
#exclusive_or(1, 0) → 1
#exclusive_or(0, 1) → 1
#exclusive_or(1, 1) → 0

#Implement exclusive_or using if statements. Please do not use python-provided bitwise exclusive-or, ^ or equality opertator ==. Both of them would work, but we'd like you to practice a more general way of solving the task using if statements.

def exclusive_or(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    return 0

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass
    test_input = input("")
    a, b = [int(i) for i in test_input.split()]
    print(exclusive_or(a, b))

# When you're finished, please submit the file to http://grader.givegrade.me.uk
