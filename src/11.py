#Advent of Code 2017 Day 11

from tools import files
import time

def test():

    input = [
            "ne,ne,ne",
            "ne,ne,sw,sw",
            "ne,ne,s,s",
            "se,sw,se,sw,sw"
    ]

    return input

def dupes(track, a, b):

    if a in track and b in track:

        if track[a] == track[b]:
            del track[a]
            del track[b]

        elif track[a] > track[b]:
            track[a] -= track[b]
            del track[b]

        else:
            track[b] -= track[a]
            del track[a]

def pairs(track, a, b, c):

    if a in track and b in track:

        if c not in track:
            track[c] = 0

        if track[a] == track[b]:
            track[c] += track[a]

            del track[a]
            del track[b]

        elif track[a] > track[b]:
            track[c] += track[b]
            track[a] -= track[b]
            del track[b]

        else:
            track[c] += track[a]
            track[b] -= track[a]
            del track[a]

def cancel(track):

    dupes(track, "ne", "sw")
    dupes(track, "se", "nw")
    dupes(track, "n", "s")
    pairs(track, "ne", "s", "se")
    pairs(track, "se", "n", "ne")
    pairs(track, "nw", "s", "sw")
    pairs(track, "sw", "n", "nw")
    pairs(track, "sw", "se", "s")
    pairs(track, "nw", "ne", "n")

def calculate(line):

    steps = 0
    path = line.split(",")
    track = {}

    for step in path:
        if step in track:
            track[step] += 1
        else:
            track[step] = 1

    cancel(track)

    for value in track.values():

        steps += value

    return steps

def part1(input):

    #input = test()
    steps = 0

    for line in input:
        steps = calculate(line)

    print("Part 1: The number of steps are {}".format(steps))

def part2(input):

    print("Part 2: {}".format(1))    

filename = "input/11.txt"
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