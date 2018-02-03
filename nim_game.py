nim = [[1, 1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1], [1, 1], [1]]

player1 = "Human 1"

player2 = "Computer 2"

players = player1, player2

def make_move(row, number):
    if row < 0 or row >= len(nim):
        print("Bad row")
        return False
    elif number <= len(nim[row]) and number > 0:
        for i in range(number):
            nim[row].pop()
        return True
    else:
        print("Bad number of elements")
        return False

def num_to_binary(num):
    bin_rep = []
    while num:
        bin_rep.append(num % 2)
        num //= 2
    return bin_rep[::-1]

def compute_nim_sum(heaps):
    heaps = [heap for heap in heaps if heap]
    i = len(heaps[0])
    for j in heaps[1:] :
        i ^= len(j)
    return i

def binary_to_num(binary):
    binary = binary[::-1]
    num = 0
    for i, elem in enumerate(binary):
        num += binary[i] * 2**i
    return num

import random
def compute_move(nim):
    X = compute_nim_sum(nim)
    good_heaps = []
    bad_heaps = []
    for i, heap in enumerate(nim):
        if heap and len(heap) ^ X < len(heap) and X != 0:
            good_heaps.append((i, len(heap) - (len(heap) ^ X)))
        elif heap:
            bad_heaps.append(i)
    random.shuffle(good_heaps)
    random.shuffle(bad_heaps)
    if good_heaps:
        return good_heaps[0]
    else:
        return bad_heaps[0], random.randint(1, len(nim[bad_heaps[0]]))
    return good_heaps

assert(5 == binary_to_num(num_to_binary(5)))
assert(12 == binary_to_num(num_to_binary(12)))
assert(0 == binary_to_num(num_to_binary(0)))

while True:
    print("Current board.", nim)
    if "Human" in players[0]:
        values = input(str(players[0]) + ". Make a move. Move is row, number, for example 0, 3:")
        row, number = values.strip().split(",")
        row = int(row)
        number = int(number)
        result = make_move(row, number)
        if not any(nim):
            print(players[0] + " won.")
            break
        if result:
            players = players[1], players[0]
    if "Computer" in players[0]:
        print(players[0] + " makes a move.")
        row, number = compute_move(nim)
        make_move(row, number)
        if not any(nim):
            print(players[0] + " won.")
            break
        players = players[1], players[0]
