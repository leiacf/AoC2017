#Advent of Code 2017 Day 12

from tools import files
from tools import programs as p
import time

def test():
    return ["0 <-> 2", "1 <-> 1", "2 <-> 0, 3, 4", "3 <-> 2, 4", "4 <-> 2, 3, 6", "5 <-> 6", "6 <-> 4, 5"]

def parse(input):

    programs = []

    for line in input:
        line = line.replace(",", "")
        temp = line.split(" ")
        program = p.Program(temp[0], temp[2:])
        programs.append(program)

    for program in programs:
        for x in range(len(program.connections)):
            look = program.connections[x]
            for prog in programs:
                if look == prog.name:
                    program.connections[x] = prog
                    break

    return programs

def find(group, program):

    for connection in program.connections:
        if connection not in group and connection.used == False:
            group.append(connection)
            connection.used = True
            find(group, connection)

def part1(input):

    #input = test()
    programs = parse(input)
    group = []
    
    find(group, programs[0])

    print("Part 1: The amount of programs in the group that contains ID 0 are {}".format(len(group)))

def part2(input):

    programs = parse(input)
    groups = []
    
    for program in programs:
        group = []
        find(group, program)
        if len(group) > 0:
            groups.append(group)

    print("Part 2: The amount of groups are {}".format(len(groups)))    

filename = "input/12.txt"
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