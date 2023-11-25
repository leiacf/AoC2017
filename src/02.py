#Advent of Code 2017 Day 02

from tools import files
import time

def test():

    input = [
            "5 1 9 5", 
            "7 5 3", 
            "2 4 6 8"
            ]
    
    return input

def test2():

    input = [
            "5 9 2 8",
            "9 4 7 3", 
            "3 8 6 5", 
            ]
    
    return input

def parse(input):

    numbers = []

    for line in input:
        line = line.replace("\t", " ")
        new = [int(a) for a in line.split(" ")]

        numbers.append(new)

    return numbers

def calculate(line):

    for x in range(0, len(line)):
        for y in range(x+1, len(line)):

            a = line[x]
            b = line[y]

            if b != 0 and a % b == 0:
                return a//b

            if a != 0 and b % a == 0:
                return b//a

    return 0

def part1(input):
    
    #input = test()
    numbers = parse(input)
    sum = 0

    for line in numbers:
        line.sort()
        sum += line[-1] - line[0]

    print("Part 1: The sum of all numbers is {}".format(sum)) 

def part2(input):

    #input = test2()
    numbers = parse(input)
    sum = 0

    for line in numbers:
        sum += calculate(line)

    print("Part 2: The sum of all numbers is {}".format(sum)) 

filename = "input/02.txt"
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