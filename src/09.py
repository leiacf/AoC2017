#Advent of Code 2017 Day 09

from tools import files
import time

def test():

    input = [
            "{}",
            "{{{}}}",
            "{{},{}}",
            "{{{},{},{{}}}}",
            "{<a>,<a>,<a>,<a>}",
            "{{<ab>},{<ab>},{<ab>},{<ab>}}",
            "{{<!!>},{<!!>},{<!!>},{<!!>}}",
            "{{<a!>},{<a!>},{<a!>},{<ab>}}"
            ]

    return input

def remove(line, garbage):

    while "!" in line:
        start = line.index("!")
        end = start+1
        line = line[:start] + line[end+1:]

    while "<" in line:
        start = line.index("<")
        end = line.index(">", start)
        
        garbage.append(line[start:end+1])
        
        line = line[:start] + line[end+1:]
        
    return line

def count(line, garbage):

    line = remove(line, garbage)
    counter = 0    
    final = []

    for letter in line:
        if letter == "{":
            counter += 1
            final.append(counter)
        elif letter == "}":
            counter -= 1

    sum = 0

    for number in final:
        sum += number

    return sum

def part1(input):
    
    #input = test()
    sum = 0

    garbage = []

    for line in input:
        sum += count(line, garbage)

    print("Part 1: The total score for all groups are {}".format(sum))

def part2(input):
    
    #input = test()
    sum = 0

    garbage = []

    for line in input:
        count(line, garbage)

    for garb in garbage:
        sum += len(garb)-2

    print("Part 2: The number of characters in the garbage are {}".format(sum)) 

filename = "input/09.txt"
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