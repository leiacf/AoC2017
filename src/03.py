#Advent of Code 2017 Day 03

import time
import math
from tools import points

def test():

    input = [
        1, 
        12, 
        23,
        1024
    ]

    return input

def change(dir):

    match dir:
        case "R":
            return "U"
        case "U":
            return "L"
        case "L":
            return "D"
        case "D":
            return "R"
        case _:
            exit(-1)

def ulam(input):

    if input == 1:
        return 0

    dir = "R"
    origo = [0, 0]
    number = 1
    size = 1
    steps = 0
    x = y = 0

    while True:

        if (steps > 0 and steps % 2 == 0):
            size += 1

        for _ in range(size):

            match dir:
                case "R":
                    x += 1
                case "U":
                    y -= 1
                case "L":
                    x -= 1
                case "D":
                    y += 1
                case _:
                    exit(-1)

            number += 1

            if number == input:
                return(points.calculate_manhattan(origo, [x, y]))

        dir = change(dir)
        steps += 1

def get(point, points):

    adjacent = {}
    x = point[0]
    y = point[1]

    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            if a == 0 and b == 0:
                pass
            else:
                if (x+a,y+b) in points:
                    adjacent[x+a, y+b] = points[x+a, y+b]

    return adjacent

def modified(input):

    if input == 1:
        return 1

    points = {}

    start = (0, 0)
    points[start] = 1

    dir = "R"
    size = 1
    steps = 0
    x = y = 0

    while True:

        if (steps > 0 and steps % 2 == 0):
            size += 1

        for _ in range(size):

            match dir:
                case "R":
                    x += 1
                case "U":
                    y -= 1
                case "L":
                    x -= 1
                case "D":
                    y += 1
                case _:
                    exit(-1)

            point = (x, y)
            adjacent = get(point, points)
            sum = 0

            for value in adjacent.values():
                sum += value

            points[point] = sum

            if sum > input:
                return sum

        dir = change(dir)
        steps += 1

def part1(input):

    #input = test()
    
    for line in input:

        result = ulam(line)

        print("Part 1: The number of steps we have to take are {}".format(result))

def part2(input):

    for line in input:

        result = modified(line)

        print("Part 2: The first number bigger than my input is {}".format(result))    

input = [347991]

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