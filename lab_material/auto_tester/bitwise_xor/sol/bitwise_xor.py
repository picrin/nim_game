# Now you are ready to implement bitwise exclusive or. The idea is that given any two numbers:
# 1. We'll first find their binary representations (using `binary_numeral`)
# 2. We'll make each representation to have equal length by padding the shorter representation
#    with 0s on the left.
# 3. We'll perform `exclusive_or` on pairs of corresponding binary digits.

# For example, to compute 3 xor 5 we will:
# 1. Represent 3 in binary as [1, 1] and 5 in binary as [1, 0, 1]
# 2. Pad [1, 1] on the left to get [0, 1, 1]
# 3. Compute bitwise exclusive or on [0, 1, 1] and [1, 0, 1] to get [1, 1, 0]
# 4. Represent [1, 1, 0] using arabic numeral

# Please **do not** use the python-provided xor `^` -- the point of this exercise is to learn
# how bitwise xor works at the algorithmic level, not learning the standard library.

# your solution to `exclusive_or` `numeral_binary` and `binary_numeral` go here:

def exclusive_or(a, b):
    if a == 0 and b == 0:
        return 0
    if a == 0 and b == 1:
        return 1
    if a == 1 and b == 0:
        return 1
    return 0

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

# Your solution to `bitwise_exclusive_or` goes here:

def bitwise_exclusive_or(a, b):
    a = numeral_binary(a)
    b = numeral_binary(b)
    if len(a) < len(b):
        a, b = b, a
    len_diff = len(a) - len(b)
    b = [0] * len_diff + b
    return binary_numeral([exclusive_or(i, j) for i, j in zip(a, b)])

# As you might have already realised python implements bitwise exclusive-or using the caret as an in-fix binary operator `^`. You can use python's native implementation to check your code.

assert bitwise_exclusive_or(3, 5)

# Pro tip: python-provided bitwise exclusive-or has very low precedence. Always surround it with brackets to
# avoid unpleasant surprises!

# 1 + 2 ^ 3 ← this doesn't do what you think it does!
# 1 + (2 ^ 3) ← this is OK.

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass
    testcase = input("")
    a, b = [int(i) for i in testcase.split()]
    print(bitwise_exclusive_or(a, b))

# When you're finished, please submit the file to http://grader.givegrade.me.uk