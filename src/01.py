#Advent of Code 2017 Day 01

from tools import files
import time

def test():

    input = [
            "1122",
            "1111",
            "1234",
            "91212129"
            ]
    return input

def test2():

    input = [
            "1212",
            "1221", 
            "123425",
            "123123",
            "12131415"
            ]
    
    return input

def calculate(line):

    sum = 0

    for x in range(0, len(line)-1):

        if line[x] == line[x+1]:
            sum += int(line[x])

    if line[-1] == line[0]:
        sum += int(line[0])
    
    return sum

def calculate2(line):
    
    sum = 0

    half = len(line)//2
    
    for x in range(0, len(line)):
        
        if (x+half >= len(line)):
            half*= -1

        if line[x] == line[x+half]:
            sum += int(line[x])
    
    return sum

def part1(input):

    #input = test()
    sum = 0

    for line in input:        
        sum += calculate(line)

    print("Part 1: The captcha is {}".format(sum))

def part2(input):

    #input = test2()
    sum = 0

    for line in input:        
        sum += calculate2(line)

    print("Part 1: The captcha is {}".format(sum)) 

filename = "input/01.txt"
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