#Advent of Code 2017 Day 04

from tools import files
import time
import itertools

def test():

    input = [
        "aa bb cc dd ee",
        "aa bb cc dd aa",
        "aa bb cc dd aaa"
    ]

    return input

def valid(line):

    words = line.split(" ")

    for x in range(0, len(words)):
        for y in range(x+1, len(words)):
            
            if words[x] == words[y]:
                return False
            
    return True

def valids(line):

    words = line.split(" ")

    for x in range(0, len(words)):
        
        anagrams = ["".join(ana) for ana in itertools.permutations(words[x])]

        for y in range(x+1, len(words)):
            
            if words[x] == words[y]:
                return False
            
            if words[y] in anagrams:
                return False
            
    return True

def part1(input):

    #input = test()
    sum = 0

    for line in input:
        if valid(line):
            sum += 1

    print("Part 1: The number of valid passphrases are {}".format(sum))

def part2(input):

    sum = 0

    for line in input:
        if valids(line):
            sum += 1

    print("Part 2: The number of valid passphrases are {}".format(sum))

filename = "input/04.txt"
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