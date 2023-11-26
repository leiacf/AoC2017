#Advent of Code 2017 Day 07

from tools import files
from tools import nodes
import time

def test():

    input = [
            "pbga (66)",
            "xhth (57)",
            "ebii (61)",
            "havc (66)",
            "ktlj (57)",
            "fwft (72) -> ktlj, cntj, xhth",
            "qoyq (66)",
            "padx (45) -> pbga, havc, qoyq",
            "tknk (41) -> ugml, padx, fwft",
            "jptl (61)",
            "ugml (68) -> gyxo, ebii, jptl",
            "gyxo (61)",
            "cntj (57)"
            ]
    
    return input

def create(line):

    line = line.replace("(", "")
    line = line.replace(")", "")
    line = line.replace("-> ", "")
    line = line.replace(",", "")
    
    split = line.split(" ")

    return nodes.Node(split[0], int(split[1]), split[2:])

def parse(input):

    tower = []
    children = []
        
    for line in input:
        node = create(line)
        tower.append(node)

    for node in tower:
        for x in range(0, len(node.children)):
            children.append(node.children[x])
            
            for inner in tower:
                if inner.name == node.children[x]:
                    node.children[x] = inner
                    break

    for node in tower:
        if node.name not in children:
            return node
    
    return None

def total(node):

    sum = 0

    for child in node.children:
        sum += total(child)

    sum += node.weight
    node.total = sum
    
    return sum

def calculate(node, x):

    if node.children[x].total == node.children[0].total:
        return node.children[x-1].weight - abs(node.children[x].total - node.children[x-1].total)
        
    else:
        if x >= 2:
            if node.children[x-1].total == node.children[x].total:
                return node.children[0].weight - abs(node.children[x].total - node.children[0].total)
            else:
                return node.children[x].weight - abs(node.children[x-1].total - node.children[x].total)
        
def check(node):

    diff = 0

    if len(node.children) > 0:
        last = node.children[0].total

    for x in range(0, len(node.children)):

        weight = check(node.children[x])

        if (weight > 0):
            return weight

        if node.children[x].total != 0 and node.children[x].total != last:
            return calculate(node, x)

        else:
            last = node.children[x].total

    return diff

def part1(input):

    #input = test()
    bottom = parse(input)

    print("Part 1: The program at the bottom is {}".format(bottom.name))

def part2(input):

    #input = test()
    bottom = parse(input)
    total(bottom)
    weight = check(bottom)
  
    print("Part 2: The program with the wrong weight need to be {}".format(weight))

filename = "input/07.txt"
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