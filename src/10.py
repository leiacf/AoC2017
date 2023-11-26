#Advent of Code 2017 Day 10

from tools import files
import time

def test():

    input = ["3,4,1,5"]

    return input

def calculate(lengths, numbers, times):

    current = 0
    skip = 0

    for _ in range(times):

        for num in lengths:

            #print(skip)

            if num > len(numbers):
                continue

            # rotate
            numbers = numbers[current:] + numbers[:current]

            temp = numbers[:num]
            temp.reverse()
            numbers = temp + numbers[num:]

            # rotate back
            back = len(numbers)-current
            numbers = numbers[back:] + numbers[:back]  

            current = current + num + (skip % len(numbers))

            if current >= len(numbers):
                current = (current % len(numbers))
            
            skip += 1

    return numbers

def convert(input):

    values = []

    if len(input) > 0:
        for letter in input[0]:
            values.append(ord(letter))

    return values

def xor(numbers):

    sum = numbers[0]

    for j in range(1, len(numbers)):
        sum ^= numbers[j]

    return sum

def part1(input):

    numbers = [x for x in range(256)]
    
    #numbers = [x for x in range(5)]
    #input = test()

    lengths = [int(x) for x in input[0].split(",")]
    final = calculate(lengths, numbers, 1)

    print("Part 1: The result is {}".format(final[0]*final[1]))

def part2(input):

    #input = ""
    
    numbers = [x for x in range(256)]

    values = convert(input)
    values += [17, 31, 73, 47, 23]

    numbers = calculate(values, numbers, 64)

    dense = []

    for i in range(0, 256, 16):
        dense.append(xor(numbers[i:i+16]))

    result = ""

    for value in dense:
        if value > 15:
            result += hex(value)[2:]
        else:
            result += "0" + hex(value)[2:]

    print("Part 2: The final hash is {}".format(result))    

filename = "input/10.txt"
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