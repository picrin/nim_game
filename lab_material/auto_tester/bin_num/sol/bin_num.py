# coding: utf-8
from __future__ import division, print_function
# In order to implement bitwise exclusive or we have to be able to convert numerals
# into their binary representations. For this purpose we can use python lists.

# Please implement the functions numeral_binary and binary_numeral

"""
>>> numeral_binary(6)
>>> [1, 1, 0]
>>> binary_numeral([1, 1, 1]):
>>> 7
"""

# Please do not use `bin()`. The purpose of this task is not to practice standard library
# skills but to practice the algorithm behind binary conversions, "from scratch", using basic
# functions, like modulo operator `%` and integer division `//`.

# Pro tip: double forward slash, `//`, denotes integer divison operator in python 3. Integer
# division ignores remainders, so for example 3//3 → 1 as expected, but 4//3 → 1 and
# 5//3 → 1 give the same answer, since the remainders 1 and 2 respectively are both ignored.

def numeral_binary(numeral):
    result = []
    while numeral:
        result.append(numeral%2)
        numeral //= 2
    return result[::-1]

def binary_numeral(binary):
    result = 0
    for i, value in enumerate(binary[::-1]):
        result += value * (2 ** i)
    return result

# You can use the following code to locally test your submission
assert binary_numeral(numeral_binary(9183742)) == 9183742

if __name__ == "__main__":
    import json, sys
    testcase = sys.stdin.read()
    testcase = json.loads(testcase)
    if testcase["type"] == "bin_num":
        print(json.dumps(binary_numeral(testcase["value"])))
    else:
        print(json.dumps(numeral_binary(testcase["value"])))

# When you're finished, please submit the file to http://grader.givegrade.me.uk