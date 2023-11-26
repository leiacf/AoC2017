#Advent of Code 2017 Day 05

from tools import files
import time

def test():

    input = [ 0, 3, 0, 1, -3]

    return input

def part1(input):

    #input = test()
    
    steps = 0
    x = 0

    while True:
        a = input[x]
        input[x] += 1
        x += a
        steps += 1

        if x >= len(input):
            break

    print("Part 1: The number of steps taken are {}".format(steps))

def part2(input):

    #input = test()
    
    steps = 0
    x = 0

    while True:
        a = input[x]

        if a >= 3:
            input[x] -= 1
        else:
            input[x] += 1
        
        x += a
        steps += 1

        if x >= len(input):
            break

    print("Part 2: The number of steps taken are {}".format(steps)) 

filename = "input/05.txt"
input = files.input_as_list(filename)
input = [int(a) for a in input]

print()

start1 = time.perf_counter()
part1(input)
end1 = time.perf_counter()

input = files.input_as_list(filename)
input = [int(a) for a in input]

start2 = time.perf_counter()
part2(input)
end2 = time.perf_counter()

print()
print("Spent {:>7.2f} seconds on Part 1".format(end1-start1))
print("Spent {:>7.2f} seconds on Part 2".format(end2-start2))