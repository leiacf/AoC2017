#Advent of Code 2017 Day 08

from tools import files
import time

def test():

    input = [
            "b inc 5 if a > 1",
            "a inc 1 if b < 5",
            "c dec -10 if a >= 1",
            "c inc -20 if c == 10"
            ]
    
    return input

def registry(input):

    regis = {}

    for line in input:
        if line.split(" ")[0] not in regis:
            regis[line.split(" ")[0]] = 0

    return dict(sorted(regis.items()))

def unwrap(regis, x):

    try:
        return int(x)
    except ValueError:
        return regis[x]
    
def check(regis, a, test, b):

    match test:
        case ">":
            if unwrap(regis, a) > unwrap(regis, b):
                return True
        case ">=":
            if unwrap(regis, a) >= unwrap(regis, b):
                return True
        case "<":
            if unwrap(regis, a) < unwrap(regis, b):
                return True
        case "<=":
            if unwrap(regis, a) <= unwrap(regis, b):
                return True
        case "==":
            if unwrap(regis, a) == unwrap(regis, b):
                return True
        case "!=":
            if unwrap(regis, a) != unwrap(regis, b):
                return True
        case _:
            print(test)
    
    return False

def do(regis, reg, ins, num, highest):

    match ins:
        case "inc":
            regis[reg] += unwrap(regis, num)
        case "dec":
            regis[reg] -= unwrap(regis, num)
        case _:
            print(ins)

    if regis[reg] not in highest:
        highest.append(regis[reg])

def calculate(line, regis, highest):
    
    reg, ins, num, cond, a, test, b = line.split(" ")
    
    if check(regis, a, test, b):
        do(regis, reg, ins, num, highest)

        
def part1(input):

    #input = test()
    regis = registry(input)
    highest = []

    for line in input:
        calculate(line, regis, highest)

    sort = sorted(regis.values())

    print("Part 1: The highest number is {}".format(sort[-1]))

def part2(input):

    #input = test()
    regis = registry(input)
    highest = []

    for line in input:
        calculate(line, regis, highest)
    
    highest.sort()
    
    print("Part 2: The highest number was {}".format(highest[-1]))  

filename = "input/08.txt"
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