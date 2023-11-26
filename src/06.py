#Advent of Code 2017 Day 06

from tools import files
import time

def find(banks):
    return banks.index(max(banks))

def redistribute(banks, index):

    number = banks[index]
    banks[index] = 0
    index += 1

    while number > 0:

        if index >= len(banks):
            index -= len(banks)

        banks[index] += 1
        
        number -= 1
        index += 1

def part1(input):

    #input = ["0 2 7 0"]

    input[0] = input[0].replace("\t", " ")
    banks = [int(a) for a in input[0].split(" ")]

    combos = []
    cycles = 0

    while True:

        index = find(banks)
        redistribute(banks, index)
        cycles += 1

        temp = "".join([str(a) for a in banks])

        if temp in combos:
            break

        else:
            combos.append(temp)

    print("Part 1: The amount of cycles is {}".format(cycles))

def part2(input):
    #input = ["0 2 7 0"]

    input[0] = input[0].replace("\t", " ")
    banks = [int(a) for a in input[0].split(" ")]

    combos = []
    cycles = 0

    while True:

        index = find(banks)
        redistribute(banks, index)
        cycles += 1

        temp = "".join([str(a) for a in banks])

        if temp in combos:
            break

        else:
            combos.append(temp)

    before = combos.index(temp) +1
    result = cycles - before

    print("Part 2: The size of the loop is {}".format(result))

filename = "input/06.txt"
input = files.input_as_list(filename)

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))